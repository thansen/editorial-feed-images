#!/usr/bin/env python3
import json

# Load metadata
with open('images_metadata.json', 'r') as f:
    data = json.load(f)

print(f"Total entries: {len(data)}")
print("\nEntries 31-60:\n")

for i in range(30, min(60, len(data))):
    entry = data[i]
    print(f"{i+1}. {entry['newFilename']}")
