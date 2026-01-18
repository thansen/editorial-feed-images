#!/usr/bin/env python3
"""
Rename files based on the generated metadata
"""

import json
from pathlib import Path

# Paths
METADATA_FILE = Path("images_metadata.json")
IMAGE_DIR = Path("editorial_feed_images")

def main():
    # Load metadata
    if not METADATA_FILE.exists():
        print(f"Error: {METADATA_FILE} not found")
        print("Run the analysis first to generate metadata")
        return

    with open(METADATA_FILE) as f:
        metadata = json.load(f)

    print(f"Loaded metadata for {len(metadata)} images\n")

    # Rename files
    renamed_count = 0
    for item in metadata:
        old_filename = item['originalFilename']
        new_filename = item['newFilename']

        old_path = IMAGE_DIR / old_filename
        new_path = IMAGE_DIR / new_filename

        if not old_path.exists():
            print(f"⚠️  File not found: {old_filename}")
            continue

        if old_path == new_path:
            print(f"⏭️  Skipping (already named): {new_filename}")
            continue

        # Check for collisions
        if new_path.exists():
            print(f"⚠️  Collision detected: {new_filename} already exists")
            continue

        # Rename
        old_path.rename(new_path)
        renamed_count += 1
        print(f"✓ {old_filename}")
        print(f"  → {new_filename}\n")

    print(f"\nDone! Renamed {renamed_count} files")

if __name__ == "__main__":
    main()
