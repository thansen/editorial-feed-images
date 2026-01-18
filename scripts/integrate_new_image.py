#!/usr/bin/env python3
"""
Integrate a new image into the system:
1. Analyze image content with Claude Vision
2. Extract colors programmatically
3. Generate clean filename
4. Add to metadata JSON
5. Rename file
"""

import json
import base64
from pathlib import Path
import os
import re
from anthropic import Anthropic
from PIL import Image
from collections import Counter

# Initialize client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Paths
IMAGE_DIR = Path("editorial_feed_images")
METADATA_FILE = Path("images_metadata.json")
BACKUP_FILE = Path("images_metadata.backup_before_new.json")

def get_image_base64(image_path):
    """Read image and convert to base64"""
    with open(image_path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")

def rgb_to_hex(rgb):
    """Convert RGB tuple to hex string"""
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def color_distance(c1, c2):
    """Calculate euclidean distance between two RGB colors"""
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5

def get_color_name(rgb):
    """Map RGB color to closest named color"""
    color_names = {
        (220, 20, 60): 'crimson', (255, 0, 0): 'red', (178, 34, 34): 'firebrick',
        (255, 192, 203): 'pink', (255, 105, 180): 'hot-pink', (255, 20, 147): 'deep-pink',
        (128, 0, 128): 'purple', (147, 112, 219): 'medium-purple', (138, 43, 226): 'blue-violet',
        (0, 0, 255): 'blue', (0, 191, 255): 'deep-sky-blue', (30, 144, 255): 'dodger-blue',
        (0, 128, 128): 'teal', (64, 224, 208): 'turquoise', (0, 255, 255): 'cyan',
        (0, 128, 0): 'green', (0, 255, 0): 'lime', (50, 205, 50): 'lime-green',
        (255, 255, 0): 'yellow', (255, 215, 0): 'gold', (255, 165, 0): 'orange',
        (255, 255, 255): 'white', (192, 192, 192): 'silver', (128, 128, 128): 'gray',
        (0, 0, 0): 'black'
    }

    min_distance = float('inf')
    closest_name = 'gray'

    for color_rgb, name in color_names.items():
        distance = color_distance(rgb, color_rgb)
        if distance < min_distance:
            min_distance = distance
            closest_name = name

    return closest_name

def extract_colors(image_path):
    """Extract dominant colors from image"""
    try:
        img = Image.open(image_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        img.thumbnail((300, 300))
        pixels = list(img.getdata())

        # Filter out very light and very dark colors
        filtered_pixels = [
            p for p in pixels
            if not ((p[0] > 240 and p[1] > 240 and p[2] > 240) or
                   (p[0] < 15 and p[1] < 15 and p[2] < 15))
        ]

        if not filtered_pixels:
            filtered_pixels = pixels

        color_counts = Counter(filtered_pixels)
        most_common = color_counts.most_common(15)

        # Group similar colors
        unique_colors = []
        for color, count in most_common:
            is_similar = False
            for existing_color, _ in unique_colors:
                if color_distance(color, existing_color) < 40:
                    is_similar = True
                    break
            if not is_similar:
                unique_colors.append((color, count))
            if len(unique_colors) >= 5:
                break

        total_pixels = sum(count for _, count in unique_colors)

        dominant_colors = []
        accent_colors = []
        color_names = []

        for color, count in unique_colors:
            percentage = (count / total_pixels) * 100
            hex_color = rgb_to_hex(color)
            color_name = get_color_name(color)

            if percentage > 10:
                dominant_colors.append(hex_color)
            else:
                accent_colors.append(hex_color)

            if color_name not in color_names:
                color_names.append(color_name)

        return {
            'dominant': dominant_colors[:3],
            'accent': accent_colors[:3],
            'named': color_names[:6]
        }

    except Exception as e:
        print(f"Error extracting colors: {e}")
        return {'dominant': [], 'accent': [], 'named': []}

def analyze_image(image_path):
    """Analyze image content with Claude Vision"""
    print(f"Analyzing image content...")
    image_data = get_image_base64(image_path)

    prompt = """Look at this image and describe EXACTLY what you see. Be literal and accurate.

Return ONLY valid JSON:
{
  "title": "Brief Title (2-4 words)",
  "description": "Accurate 1-2 sentence description of what's in the image",
  "conceptual": ["concept1", "concept2", "concept3", "concept4"],
  "subject": ["object1", "object2", "object3", "object4"],
  "style": ["style1", "style2", "style3", "style4"]
}"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": [{
                    "type": "image",
                    "source": {"type": "base64", "media_type": "image/jpeg", "data": image_data}
                }, {
                    "type": "text",
                    "text": prompt
                }]
            }]
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
        print(f"Error analyzing image: {e}")
        return None

def generate_filename(title, existing_filenames):
    """Generate a clean, unique filename from title"""
    # Convert to lowercase and replace spaces with hyphens
    base = re.sub(r'[^a-z0-9\s-]', '', title.lower())
    base = re.sub(r'\s+', '-', base.strip())

    filename = f"{base}.jpg"

    # Handle duplicates
    counter = 1
    while filename in existing_filenames:
        filename = f"{base}-{counter}.jpg"
        counter += 1

    return filename

def main():
    """Main integration function"""
    print("=" * 80)
    print("NEW IMAGE INTEGRATION")
    print("=" * 80)
    print()

    # Find the newest image
    image_files = sorted(IMAGE_DIR.glob("*.jpg"), key=lambda p: p.stat().st_mtime, reverse=True)

    if not image_files:
        print("❌ No images found in directory")
        return

    newest_image = image_files[0]
    print(f"📸 New image: {newest_image.name}")
    print()

    # Load existing metadata
    with open(METADATA_FILE) as f:
        metadata = json.load(f)

    existing_filenames = {entry['newFilename'] for entry in metadata}

    # Check if already in metadata
    if newest_image.name in existing_filenames:
        print(f"⚠️  Image already in metadata. Looking for next newest...")
        for img in image_files[1:]:
            if img.name not in existing_filenames:
                newest_image = img
                print(f"📸 Found: {newest_image.name}")
                break
        else:
            print("❌ No new images to add")
            return

    # Step 1: Analyze image content
    print("🔍 Step 1: Analyzing image content with Claude Vision...")
    analysis = analyze_image(newest_image)

    if not analysis:
        print("❌ Failed to analyze image")
        return

    print(f"   ✓ Title: {analysis['title']}")
    print()

    # Step 2: Extract colors
    print("🎨 Step 2: Extracting colors...")
    colors = extract_colors(newest_image)
    print(f"   ✓ Found {len(colors['dominant'])} dominant colors")
    print()

    # Step 3: Generate filename
    print("📝 Step 3: Generating clean filename...")
    new_filename = generate_filename(analysis['title'], existing_filenames)
    print(f"   ✓ New filename: {new_filename}")
    print()

    # Step 4: Create metadata entry
    print("💾 Step 4: Creating metadata entry...")

    # Combine analyzed color names with any additional color tags
    color_tags = list(colors['named'])

    new_entry = {
        "originalFilename": newest_image.name,
        "newFilename": new_filename,
        "title": analysis['title'],
        "description": analysis['description'],
        "tags": {
            "conceptual": analysis['conceptual'],
            "subject": analysis['subject'],
            "colors": color_tags,
            "style": analysis['style'],
            "analyzed_colors": colors
        }
    }

    # Backup existing metadata
    import shutil
    shutil.copy2(METADATA_FILE, BACKUP_FILE)
    print(f"   ✓ Backup created: {BACKUP_FILE}")

    # Add new entry
    metadata.append(new_entry)

    # Save updated metadata
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"   ✓ Added to metadata ({len(metadata)} total entries)")
    print()

    # Step 5: Rename file
    print("📂 Step 5: Renaming image file...")
    new_path = IMAGE_DIR / new_filename
    newest_image.rename(new_path)
    print(f"   ✓ Renamed: {newest_image.name} → {new_filename}")
    print()

    print("=" * 80)
    print("✅ INTEGRATION COMPLETE")
    print("=" * 80)
    print()
    print(f"New entry:")
    print(f"  Title: {analysis['title']}")
    print(f"  Filename: {new_filename}")
    print(f"  Colors: {', '.join(colors['named'][:3])}")
    print()
    print("Run tests to verify: ./run_all_tests.sh")

if __name__ == "__main__":
    main()
