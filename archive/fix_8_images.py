#!/usr/bin/env python3
"""Fix 8 specific mislabeled images"""

import json
import shutil
from pathlib import Path

METADATA_FILE = Path("images_metadata.json")

# Load metadata
with open(METADATA_FILE) as f:
    data = json.load(f)

# Backup
shutil.copy2(METADATA_FILE, "images_metadata.backup_fix8.json")

# Corrections
corrections = {
    "jade-gears-gradient.jpg": {
        "title": "Pink Purple Rectangles",
        "description": "Abstract 3D layered geometric rectangles in shades of pink and purple creating depth on a purple gradient background.",
        "conceptual": ["abstract", "geometry", "layers", "depth", "modern", "design"],
        "subject": ["rectangles", "geometric-shapes", "layers", "3d", "abstract"],
        "style": ["abstract", "modern", "3d-render", "geometric", "gradient", "minimalist"]
    },
    "rust-gears-gradient.jpg": {
        "title": "Orange Layered Rectangles",
        "description": "Abstract 3D layered geometric rectangles in shades of orange creating depth and shadow on an orange gradient background.",
        "conceptual": ["abstract", "geometry", "layers", "depth", "modern", "design"],
        "subject": ["rectangles", "geometric-shapes", "layers", "3d", "abstract"],
        "style": ["abstract", "modern", "3d-render", "geometric", "gradient", "minimalist"]
    },
    "cobalt-gears-gradient.jpg": {
        "title": "Blue Pink Rectangles",
        "description": "Abstract 3D layered geometric rectangles in blue, pink, and purple creating depth on a blue to purple gradient background.",
        "conceptual": ["abstract", "geometry", "layers", "depth", "modern", "design"],
        "subject": ["rectangles", "geometric-shapes", "layers", "3d", "abstract"],
        "style": ["abstract", "modern", "3d-render", "geometric", "gradient", "minimalist"]
    },
    "hot-pink-gears-gradient.jpg": {
        "title": "Golden Crown",
        "description": "3D rendered golden crown with spherical ornaments on points, tilted at an angle on an orange gradient background.",
        "conceptual": ["royalty", "success", "achievement", "winner", "leadership", "excellence"],
        "subject": ["crown", "gold", "royalty", "3d-render", "symbol"],
        "style": ["3d-render", "realistic", "metallic", "gradient", "modern", "clean"]
    },
    "cyan-gears-gradient.jpg": {
        "title": "Cyan Layered Rectangles",
        "description": "Abstract 3D layered geometric rectangles in shades of cyan and turquoise creating depth on a cyan gradient background.",
        "conceptual": ["abstract", "geometry", "layers", "depth", "modern", "design"],
        "subject": ["rectangles", "geometric-shapes", "layers", "3d", "abstract"],
        "style": ["abstract", "modern", "3d-render", "geometric", "gradient", "minimalist"]
    },
    "seafoam-gears-gradient.jpg": {
        "title": "Green Layered Rectangles",
        "description": "Abstract 3D layered geometric rectangles in shades of green and seafoam creating depth on a green gradient background.",
        "conceptual": ["abstract", "geometry", "layers", "depth", "modern", "design"],
        "subject": ["rectangles", "geometric-shapes", "layers", "3d", "abstract"],
        "style": ["abstract", "modern", "3d-render", "geometric", "gradient", "minimalist"]
    },
    "bronze-gears-gradient.jpg": {
        "title": "Pink Blue Brain",
        "description": "3D rendered human brain with left hemisphere in pink and right hemisphere in blue on a pink gradient background, representing dual thinking or creativity.",
        "conceptual": ["brain", "thinking", "creativity", "intelligence", "duality", "cognition"],
        "subject": ["brain", "anatomy", "hemispheres", "3d-render", "medical"],
        "style": ["3d-render", "modern", "clean", "gradient", "anatomical", "colorful"]
    },
    "raspberry-gears-gradient.jpg": {
        "title": "Green Checkmark Icon",
        "description": "3D rendered green checkmark symbol in a green framed box on a green to yellow gradient background, representing success or confirmation.",
        "conceptual": ["success", "confirmation", "approval", "complete", "verified", "correct"],
        "subject": ["checkmark", "checkbox", "icon", "symbol", "3d-render"],
        "style": ["3d-render", "modern", "clean", "gradient", "icon", "minimalist"]
    }
}

# Apply corrections
updated = 0
for i, entry in enumerate(data):
    if entry['newFilename'] in corrections:
        correction = corrections[entry['newFilename']]
        entry['title'] = correction['title']
        entry['description'] = correction['description']
        entry['tags']['conceptual'] = correction['conceptual']
        entry['tags']['subject'] = correction['subject']
        entry['tags']['style'] = correction['style']
        # Keep existing colors and analyzed_colors
        updated += 1
        print(f"✓ Updated {entry['newFilename']:50s} → {correction['title']}")

# Save
with open(METADATA_FILE, 'w') as f:
    json.dump(data, f, indent=2)

print(f"\n✅ Updated {updated}/8 entries")
print(f"✅ Backup: images_metadata.backup_fix8.json")
