#!/usr/bin/env python3
"""
Re-analyze images 31-60 to get accurate descriptions based on actual content
"""

import json
import base64
from pathlib import Path
import os
from anthropic import Anthropic

# Initialize client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Paths
IMAGE_DIR = Path("editorial_feed_images")
METADATA_FILE = Path("images_metadata.json")

def get_image_base64(image_path):
    """Read image and convert to base64"""
    with open(image_path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")

def analyze_image_content(image_path):
    """Get accurate description of what's actually in the image"""
    print(f"Analyzing: {image_path.name}")

    image_data = get_image_base64(image_path)

    prompt = """Look at this image and describe EXACTLY what you see. Be literal and accurate.

Provide:
1. A short title (2-4 words) describing the main subject
2. A literal description (1-2 sentences) of what's actually in the image
3. Conceptual tags (4-6 tags) - what concepts does this represent?
4. Subject tags (4-6 tags) - what literal objects/subjects are in the image?
5. Style tags (4-6 tags) - visual style descriptors

Return ONLY valid JSON:
{
  "title": "Tennis Racket Gradient",
  "description": "A tennis racket with a yellow tennis ball on a lime green gradient background",
  "conceptual": ["sports", "athletics", "recreation", "competition"],
  "subject": ["tennis-racket", "tennis-ball", "racket", "sports-equipment"],
  "style": ["modern", "clean", "3d-render", "gradient", "professional"]
}"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": [{
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": image_data,
                    },
                }, {
                    "type": "text",
                    "text": prompt
                }],
            }],
        )

        response_text = message.content[0].text

        # Extract JSON
        if "```json" in response_text:
            json_str = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_str = response_text.split("```")[1].split("```")[0].strip()
        else:
            json_str = response_text.strip()

        return json.loads(json_str)

    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    """Re-analyze images 31-60 (indices 30-59)"""
    # Load existing metadata to preserve colors and filenames
    with open(METADATA_FILE) as f:
        metadata = json.load(f)

    print(f"Total images: {len(metadata)}")
    print(f"Processing entries 31-60 (indices 30-59)\n")

    # Process only entries 31-60
    for i in range(30, min(60, len(metadata))):
        item = metadata[i]
        print(f"\n=== Entry {i+1} ===")
        image_path = IMAGE_DIR / item['newFilename']

        if not image_path.exists():
            print(f"Skipping {item['newFilename']} - not found")
            continue

        # Get accurate analysis
        analysis = analyze_image_content(image_path)

        if analysis:
            # Update with accurate content
            item['title'] = analysis['title']
            item['description'] = analysis['description']
            item['tags']['conceptual'] = analysis['conceptual']
            item['tags']['subject'] = analysis['subject']
            item['tags']['style'] = analysis['style']
            # Keep existing colors and analyzed_colors

            print(f"  ✓ Updated: {analysis['title']}")
            print(f"  Description: {analysis['description'][:80]}...")
        else:
            print(f"  ✗ Failed to analyze")

    # Save updated metadata
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"\n✓ Re-analyzed entries 31-60")
    print(f"✓ Saved to {METADATA_FILE}")

if __name__ == "__main__":
    main()
