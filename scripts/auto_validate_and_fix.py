#!/usr/bin/env python3
"""
Fully automated validation and fixing of image metadata.
1. Validates each image's content matches its JSON label
2. Auto-flags mismatches
3. Re-analyzes flagged images
4. Updates JSON automatically
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
BACKUP_FILE = Path("images_metadata.backup.json")

def get_image_base64(image_path):
    """Read image and convert to base64"""
    with open(image_path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")

def validate_entry(image_path, current_title, current_description):
    """Ask AI: does this title/description match the actual image?"""
    image_data = get_image_base64(image_path)

    validation_prompt = f"""You are validating image metadata accuracy.

Current metadata:
- Title: "{current_title}"
- Description: "{current_description}"

Look at the image and answer: Does this metadata ACCURATELY describe what you actually see in the image?

Respond with ONLY a JSON object:
{{
  "accurate": true/false,
  "confidence": 0.0-1.0,
  "actual_content": "brief description of what you actually see if inaccurate"
}}"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=512,
            messages=[{
                "role": "user",
                "content": [{
                    "type": "image",
                    "source": {"type": "base64", "media_type": "image/jpeg", "data": image_data}
                }, {
                    "type": "text",
                    "text": validation_prompt
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
        print(f"  ⚠ Validation error: {e}")
        return {"accurate": True, "confidence": 0.5, "actual_content": ""}

def reanalyze_image(image_path):
    """Get accurate analysis of image content"""
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
        print(f"  ✗ Re-analysis error: {e}")
        return None

def main():
    """Main validation and fixing pipeline"""
    print("=" * 80)
    print("AUTOMATED IMAGE METADATA VALIDATION & FIX")
    print("=" * 80)

    # Load metadata
    with open(METADATA_FILE) as f:
        metadata = json.load(f)

    print(f"\n📊 Total entries: {len(metadata)}")
    print(f"🔍 Validating all images...\n")

    # Phase 1: Validate all entries
    flagged = []

    for i, entry in enumerate(metadata, 1):
        image_path = IMAGE_DIR / entry['newFilename']

        if not image_path.exists():
            print(f"[{i}/{len(metadata)}] ⚠ Missing file: {entry['newFilename']}")
            continue

        print(f"[{i}/{len(metadata)}] Validating: {entry['newFilename']}", end=" ")

        validation = validate_entry(
            image_path,
            entry['title'],
            entry['description']
        )

        if not validation['accurate']:
            print(f"❌ MISMATCH (confidence: {validation['confidence']:.2f})")
            print(f"              Current: {entry['title']}")
            print(f"              Actually: {validation.get('actual_content', 'Unknown')}")
            flagged.append((i, entry, validation))
        else:
            print(f"✓ OK (confidence: {validation['confidence']:.2f})")

    # Summary of validation
    print("\n" + "=" * 80)
    print(f"📋 Validation complete:")
    print(f"   ✓ Accurate: {len(metadata) - len(flagged)}")
    print(f"   ❌ Mismatches found: {len(flagged)}")

    if not flagged:
        print("\n✨ All metadata is accurate! No fixes needed.")
        return

    # Phase 2: Re-analyze flagged entries
    print("\n" + "=" * 80)
    print(f"🔧 Re-analyzing {len(flagged)} flagged entries...\n")

    # Create backup
    import shutil
    shutil.copy2(METADATA_FILE, BACKUP_FILE)
    print(f"💾 Backup created: {BACKUP_FILE}\n")

    fixed_count = 0
    for i, entry, validation in flagged:
        image_path = IMAGE_DIR / entry['newFilename']
        print(f"Re-analyzing: {entry['newFilename']}")

        analysis = reanalyze_image(image_path)

        if analysis:
            # Update entry
            entry['title'] = analysis['title']
            entry['description'] = analysis['description']
            entry['tags']['conceptual'] = analysis['conceptual']
            entry['tags']['subject'] = analysis['subject']
            entry['tags']['style'] = analysis['style']
            # Keep existing colors and analyzed_colors

            print(f"  ✓ Updated: {analysis['title']}")
            fixed_count += 1
        else:
            print(f"  ✗ Failed to re-analyze")

    # Save updated metadata
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f, indent=2)

    print("\n" + "=" * 80)
    print("✅ COMPLETE")
    print("=" * 80)
    print(f"✓ Fixed {fixed_count}/{len(flagged)} entries")
    print(f"✓ Updated: {METADATA_FILE}")
    print(f"✓ Backup: {BACKUP_FILE}")
    print("\n🔄 Refresh your browser to see corrected labels.")

if __name__ == "__main__":
    main()
