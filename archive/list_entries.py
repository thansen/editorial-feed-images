#!/usr/bin/env python3
import json

with open('images_metadata.json', 'r') as f:
    data = json.load(f)

print("Entries 61-90 (indices 60-89) - newFilename mapping:")
print("=" * 80)
for i in range(60, 90):
    print(f"Entry {i+1} (index {i}): {data[i]['newFilename']}")
