#!/usr/bin/env python3
"""
Fix metadata by re-analyzing images in batches
This script processes images in small batches to avoid token limits
"""

import json
import base64
from pathlib import Path
import os
import sys
from anthropic import Anthropic

# Initialize client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Paths
IMAGE_DIR = Path("editorial_feed_images")
METADATA_FILE = Path("images_metadata.json")
PROGRESS_FILE = Path("fix_progress.json")

def get_image_base64(image_path):
    """Read image and convert to base64"""
    with open(image_path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")

def analyze_image(image_path):
    """Analyze a single image for accurate content"""
    image_data = get_image_base64(image_path)

    prompt = """Look at this image and describe EXACTLY what you see. Be literal and accurate.

Return ONLY valid JSON:
{
  "title": "Brief Title",
  "description": "Accurate 1-2 sentence description of what's in the image",
  "conceptual": ["concept1", "concept2", "concept3", "concept4"],
  "subject": ["object1", "object2", "object3", "object4"],
  "style": ["style1", "style2", "style3", "style4"]
}"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=512,
            messages=[{
                "role": "user",
                "content": [{
                    "type": "image",
                    "source": {"type": "base64", "media_type": "image/jpeg", "data": image_data},
                }, {
                    "type": "text",
                    "text": prompt
                }],
            }],
        )

        response_text = message.content[0].text
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

def load_progress():
    """Load progress file if exists"""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"completed": []}

def save_progress(progress):
    """Save progress"""
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f)

def main():
    """Process images in batch"""
    batch_size = int(sys.argv[1]) if len(sys.argv) > 1 else 20

    # Load metadata
    with open(METADATA_FILE) as f:
        metadata = json.load(f)

    # Load progress
    progress = load_progress()
    completed = set(progress['completed'])

    # Filter to uncompleted items
    to_process = [item for item in metadata if item['newFilename'] not in completed]

    print(f"Total images: {len(metadata)}")
    print(f"Already completed: {len(completed)}")
    print(f"To process: {len(to_process)}")
    print(f"Processing batch of: {batch_size}\n")

    # Process batch
    processed_count = 0
    for item in to_process[:batch_size]:
        image_path = IMAGE_DIR / item['newFilename']

        if not image_path.exists():
            print(f"✗ Not found: {item['newFilename']}")
            completed.add(item['newFilename'])
            continue

        print(f"Analyzing: {item['newFilename']}")
        analysis = analyze_image(image_path)

        if analysis:
            item['title'] = analysis['title']
            item['description'] = analysis['description']
            item['tags']['conceptual'] = analysis['conceptual']
            item['tags']['subject'] = analysis['subject']
            item['tags']['style'] = analysis['style']
            print(f"  ✓ {analysis['title']}")
        else:
            print(f"  ✗ Failed")

        completed.add(item['newFilename'])
        processed_count += 1

    # Save updated metadata
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f, indent=2)

    # Save progress
    save_progress({"completed": list(completed)})

    print(f"\n✓ Processed {processed_count} images")
    print(f"✓ Total completed: {len(completed)}/{len(metadata)}")

    if len(completed) < len(metadata):
        print(f"\nRun again to process next batch: python3 {sys.argv[0]} {batch_size}")
    else:
        print(f"\n✓✓✓ ALL IMAGES COMPLETED! ✓✓✓")
        PROGRESS_FILE.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
