#!/usr/bin/env python3
"""
Analyze actual colors in images and update metadata
"""

import json
from pathlib import Path
from PIL import Image
import colorsys
from collections import Counter

# Paths
IMAGE_DIR = Path("editorial_feed_images")
METADATA_FILE = Path("images_metadata.json")

def rgb_to_hex(rgb):
    """Convert RGB tuple to hex string"""
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def color_distance(c1, c2):
    """Calculate euclidean distance between two RGB colors"""
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5

def get_color_name(rgb):
    """Map RGB color to closest named color"""
    color_names = {
        # Reds
        (220, 20, 60): 'crimson',
        (255, 0, 0): 'red',
        (178, 34, 34): 'firebrick',
        (139, 0, 0): 'dark-red',
        (205, 92, 92): 'indian-red',
        (240, 128, 128): 'light-coral',
        (233, 150, 122): 'dark-salmon',
        (250, 128, 114): 'salmon',
        (255, 99, 71): 'tomato',
        (255, 69, 0): 'orange-red',
        (255, 140, 0): 'dark-orange',
        (255, 165, 0): 'orange',

        # Pinks
        (255, 192, 203): 'pink',
        (255, 182, 193): 'light-pink',
        (255, 105, 180): 'hot-pink',
        (255, 20, 147): 'deep-pink',
        (219, 112, 147): 'pale-violet-red',
        (199, 21, 133): 'medium-violet-red',

        # Purples
        (128, 0, 128): 'purple',
        (147, 112, 219): 'medium-purple',
        (138, 43, 226): 'blue-violet',
        (148, 0, 211): 'dark-violet',
        (153, 50, 204): 'dark-orchid',
        (186, 85, 211): 'medium-orchid',
        (221, 160, 221): 'plum',
        (216, 191, 216): 'thistle',
        (230, 230, 250): 'lavender',
        (238, 130, 238): 'violet',
        (218, 112, 214): 'orchid',
        (255, 0, 255): 'magenta',

        # Blues
        (0, 0, 255): 'blue',
        (0, 0, 139): 'dark-blue',
        (0, 0, 205): 'medium-blue',
        (25, 25, 112): 'midnight-blue',
        (0, 191, 255): 'deep-sky-blue',
        (30, 144, 255): 'dodger-blue',
        (100, 149, 237): 'cornflower-blue',
        (135, 206, 235): 'sky-blue',
        (135, 206, 250): 'light-sky-blue',
        (70, 130, 180): 'steel-blue',
        (176, 196, 222): 'light-steel-blue',
        (173, 216, 230): 'light-blue',
        (176, 224, 230): 'powder-blue',
        (175, 238, 238): 'pale-turquoise',
        (0, 206, 209): 'dark-turquoise',
        (64, 224, 208): 'turquoise',
        (72, 209, 204): 'medium-turquoise',
        (0, 255, 255): 'cyan',
        (224, 255, 255): 'light-cyan',
        (95, 158, 160): 'cadet-blue',

        # Teals/Aquas
        (0, 128, 128): 'teal',
        (32, 178, 170): 'light-sea-green',
        (47, 79, 79): 'dark-slate-gray',
        (102, 205, 170): 'medium-aquamarine',
        (127, 255, 212): 'aquamarine',

        # Greens
        (0, 128, 0): 'green',
        (0, 100, 0): 'dark-green',
        (34, 139, 34): 'forest-green',
        (0, 255, 0): 'lime',
        (50, 205, 50): 'lime-green',
        (144, 238, 144): 'light-green',
        (152, 251, 152): 'pale-green',
        (143, 188, 143): 'dark-sea-green',
        (0, 250, 154): 'medium-spring-green',
        (0, 255, 127): 'spring-green',
        (46, 139, 87): 'sea-green',
        (60, 179, 113): 'medium-sea-green',
        (32, 178, 170): 'light-sea-green',
        (152, 251, 152): 'pale-green',
        (0, 255, 127): 'spring-green',
        (124, 252, 0): 'lawn-green',
        (127, 255, 0): 'chartreuse',
        (173, 255, 47): 'green-yellow',
        (154, 205, 50): 'yellow-green',
        (85, 107, 47): 'dark-olive-green',
        (107, 142, 35): 'olive-drab',
        (128, 128, 0): 'olive',

        # Yellows
        (255, 255, 0): 'yellow',
        (255, 255, 224): 'light-yellow',
        (255, 250, 205): 'lemon-chiffon',
        (250, 250, 210): 'light-goldenrod-yellow',
        (255, 239, 213): 'papaya-whip',
        (255, 228, 181): 'moccasin',
        (255, 218, 185): 'peach-puff',
        (238, 232, 170): 'pale-goldenrod',
        (240, 230, 140): 'khaki',
        (189, 183, 107): 'dark-khaki',
        (255, 215, 0): 'gold',

        # Browns
        (210, 180, 140): 'tan',
        (210, 105, 30): 'chocolate',
        (205, 133, 63): 'peru',
        (244, 164, 96): 'sandy-brown',
        (222, 184, 135): 'burly-wood',
        (160, 82, 45): 'sienna',
        (139, 69, 19): 'saddle-brown',
        (165, 42, 42): 'brown',
        (128, 0, 0): 'maroon',

        # Grays
        (255, 255, 255): 'white',
        (245, 245, 245): 'white-smoke',
        (220, 220, 220): 'gainsboro',
        (211, 211, 211): 'light-gray',
        (192, 192, 192): 'silver',
        (169, 169, 169): 'dark-gray',
        (128, 128, 128): 'gray',
        (105, 105, 105): 'dim-gray',
        (119, 136, 153): 'light-slate-gray',
        (112, 128, 144): 'slate-gray',
        (47, 79, 79): 'dark-slate-gray',
        (0, 0, 0): 'black',
    }

    # Find closest color name
    min_distance = float('inf')
    closest_name = 'gray'

    for color_rgb, name in color_names.items():
        distance = color_distance(rgb, color_rgb)
        if distance < min_distance:
            min_distance = distance
            closest_name = name

    return closest_name

def extract_colors(image_path, num_colors=5):
    """Extract dominant colors from an image"""
    try:
        img = Image.open(image_path)

        # Convert to RGB if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Resize for faster processing
        img.thumbnail((300, 300))

        # Get all pixels
        pixels = list(img.getdata())

        # Remove very light (near white) and very dark (near black) colors
        # as they're often background/shadows
        filtered_pixels = []
        for pixel in pixels:
            r, g, b = pixel
            # Skip if too light or too dark
            if not (r > 240 and g > 240 and b > 240) and not (r < 15 and g < 15 and b < 15):
                filtered_pixels.append(pixel)

        if not filtered_pixels:
            filtered_pixels = pixels

        # Count color frequencies
        color_counts = Counter(filtered_pixels)

        # Get most common colors
        most_common = color_counts.most_common(num_colors * 3)

        # Group similar colors together
        unique_colors = []
        for color, count in most_common:
            is_similar = False
            for existing_color, _ in unique_colors:
                if color_distance(color, existing_color) < 40:  # Similarity threshold
                    is_similar = True
                    break
            if not is_similar:
                unique_colors.append((color, count))
            if len(unique_colors) >= num_colors:
                break

        # Calculate total pixels for percentage
        total_pixels = sum(count for _, count in unique_colors)

        # Separate dominant (>10%) and accent colors
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
            'dominant': dominant_colors[:3],  # Top 3 dominant
            'accent': accent_colors[:3],       # Top 3 accent
            'named': color_names[:6]           # Top 6 color names
        }

    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def main():
    """Main processing function"""
    # Load existing metadata
    with open(METADATA_FILE) as f:
        metadata = json.load(f)

    print(f"Analyzing colors for {len(metadata)} images...\n")

    updated_count = 0

    for i, item in enumerate(metadata, 1):
        image_path = IMAGE_DIR / item['newFilename']

        if not image_path.exists():
            print(f"[{i}/{len(metadata)}] Skipping {item['newFilename']} - file not found")
            continue

        print(f"[{i}/{len(metadata)}] Analyzing {item['newFilename']}")

        # Extract colors
        colors = extract_colors(image_path)

        if colors:
            # Keep original conceptual tags
            item['tags']['analyzed_colors'] = colors

            # Add named colors to the colors tag list if not already there
            for color_name in colors['named']:
                if color_name not in item['tags']['colors']:
                    item['tags']['colors'].append(color_name)

            updated_count += 1
            print(f"  Dominant: {colors['dominant']}")
            print(f"  Named: {colors['named']}")

    # Save updated metadata
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"\n✓ Updated {updated_count} images with color analysis")
    print(f"✓ Saved to {METADATA_FILE}")

if __name__ == "__main__":
    main()
