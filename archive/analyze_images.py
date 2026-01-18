#!/usr/bin/env python3
"""
Image Analysis and Renaming Script
Analyzes editorial feed images using Claude Vision API and generates metadata
"""

import os
import json
import base64
import re
from pathlib import Path
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Paths
IMAGE_DIR = Path("editorial_feed_images/editorial_feed_images")
OUTPUT_JSON = Path("editorial_feed_images/images_metadata.json")

def get_image_base64(image_path):
    """Read image and convert to base64"""
    with open(image_path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")

def sanitize_filename(text):
    """Convert text to safe filename format"""
    # Convert to lowercase
    text = text.lower()
    # Replace spaces and special chars with hyphens
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    # Limit length
    return text[:100]

def analyze_image(image_path):
    """Analyze a single image using Claude Vision API"""
    print(f"Analyzing: {image_path.name}")

    # Get image data
    image_data = get_image_base64(image_path)
    image_ext = image_path.suffix.lower()
    media_type = "image/jpeg" if image_ext in [".jpg", ".jpeg"] else "image/png"

    # Create analysis prompt
    prompt = """Analyze this editorial/design image and provide:

1. A literal, descriptive filename (3-6 words describing what's visually in the image)
2. A human-friendly title (2-4 words, title case)
3. A brief description (1-2 sentences describing the image)
4. Tags in these categories:
   - conceptual: abstract concepts the image represents (technology, healthcare, innovation, etc.)
   - subject: literal objects/subjects in the image (gears, syringe, person, etc.)
   - colors: dominant colors and color themes
   - style: visual style descriptors (modern, minimalist, corporate, 3D-render, etc.)

Provide 4-8 tags per category. Keep tags as single words or short phrases (2-3 words max), lowercase, hyphenated if needed.

Return ONLY valid JSON in this exact format:
{
  "literalFilename": "descriptive-name-here",
  "title": "Human Friendly Title",
  "description": "Brief description of the image",
  "tags": {
    "conceptual": ["tag1", "tag2"],
    "subject": ["tag1", "tag2"],
    "colors": ["tag1", "tag2"],
    "style": ["tag1", "tag2"]
  }
}"""

    # Call Claude API
    try:
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": media_type,
                                "data": image_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ],
                }
            ],
        )

        # Parse response
        response_text = message.content[0].text

        # Extract JSON from response (handle markdown code blocks)
        if "```json" in response_text:
            json_str = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_str = response_text.split("```")[1].split("```")[0].strip()
        else:
            json_str = response_text.strip()

        analysis = json.loads(json_str)

        return analysis

    except Exception as e:
        print(f"Error analyzing {image_path.name}: {e}")
        return None

def main():
    """Main processing function"""
    # Get all JPEG files
    image_files = sorted(IMAGE_DIR.glob("*.jpg")) + sorted(IMAGE_DIR.glob("*.jpeg"))
    print(f"Found {len(image_files)} images to analyze\n")

    metadata_list = []
    rename_map = {}  # Track original -> new filename mapping

    # Analyze each image
    for i, image_path in enumerate(image_files, 1):
        print(f"\n[{i}/{len(image_files)}]")

        analysis = analyze_image(image_path)

        if analysis:
            # Generate new filename
            literal_name = sanitize_filename(analysis["literalFilename"])
            new_filename = f"{literal_name}{image_path.suffix}"

            # Handle potential filename collisions
            new_path = IMAGE_DIR / new_filename
            counter = 1
            while new_path.exists() and new_path != image_path:
                new_filename = f"{literal_name}-{counter}{image_path.suffix}"
                new_path = IMAGE_DIR / new_filename
                counter += 1

            # Create metadata entry
            metadata = {
                "originalFilename": image_path.name,
                "newFilename": new_filename,
                "title": analysis["title"],
                "description": analysis["description"],
                "tags": analysis["tags"]
            }

            metadata_list.append(metadata)
            rename_map[image_path] = new_path

            print(f"  → {new_filename}")

    # Save metadata JSON
    OUTPUT_JSON.parent.mkdir(exist_ok=True)
    with open(OUTPUT_JSON, "w") as f:
        json.dump(metadata_list, f, indent=2)

    print(f"\n✓ Metadata saved to {OUTPUT_JSON}")
    print(f"  Total images processed: {len(metadata_list)}")

    # Rename files
    print("\nRenaming files...")
    for old_path, new_path in rename_map.items():
        if old_path != new_path:
            old_path.rename(new_path)

    print(f"✓ Renamed {len(rename_map)} files")
    print("\nDone!")

if __name__ == "__main__":
    main()
