#!/usr/bin/env python3
"""
Test suite for metadata integrity and data quality.
Run with: python3 test_metadata_integrity.py
"""

import json
from pathlib import Path
import sys

# Paths
IMAGE_DIR = Path("editorial_feed_images")
METADATA_FILE = Path("images_metadata.json")

class TestMetadataIntegrity:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.warnings = 0

    def test(self, name, condition, error_msg=""):
        """Run a single test"""
        if condition:
            print(f"✓ {name}")
            self.passed += 1
            return True
        else:
            print(f"✗ {name}")
            if error_msg:
                print(f"  → {error_msg}")
            self.failed += 1
            return False

    def warn(self, name, condition, warning_msg=""):
        """Run a warning check"""
        if condition:
            print(f"✓ {name}")
            return True
        else:
            print(f"⚠ {name}")
            if warning_msg:
                print(f"  → {warning_msg}")
            self.warnings += 1
            return False

def test_file_exists():
    """Test that metadata file exists"""
    tester = TestMetadataIntegrity()
    tester.test(
        "Metadata file exists",
        METADATA_FILE.exists(),
        f"{METADATA_FILE} not found"
    )
    tester.test(
        "Image directory exists",
        IMAGE_DIR.exists(),
        f"{IMAGE_DIR} not found"
    )
    return tester

def test_json_structure():
    """Test JSON structure and required fields"""
    tester = TestMetadataIntegrity()

    try:
        with open(METADATA_FILE) as f:
            data = json.load(f)
    except Exception as e:
        tester.test("JSON is valid", False, str(e))
        return tester

    tester.test("JSON is valid", True)
    tester.test("JSON is a list", isinstance(data, list))
    tester.test("JSON has entries", len(data) > 0, f"Found {len(data)} entries")

    # Test required fields in first entry
    if data:
        entry = data[0]
        required_fields = ['originalFilename', 'newFilename', 'title', 'description', 'tags']
        for field in required_fields:
            tester.test(
                f"Entry has '{field}' field",
                field in entry,
                f"Missing in entry: {entry.get('newFilename', 'unknown')}"
            )

        # Test tags structure
        if 'tags' in entry:
            tags = entry['tags']
            required_tag_types = ['conceptual', 'subject', 'colors', 'style']
            for tag_type in required_tag_types:
                tester.test(
                    f"Tags has '{tag_type}' array",
                    tag_type in tags and isinstance(tags[tag_type], list),
                    f"Missing or invalid in entry: {entry.get('newFilename', 'unknown')}"
                )

            # analyzed_colors is optional but should be object if present
            if 'analyzed_colors' in tags:
                tester.test(
                    "analyzed_colors is an object",
                    isinstance(tags['analyzed_colors'], dict),
                    f"Should be object in entry: {entry.get('newFilename', 'unknown')}"
                )

    return tester

def test_file_image_mapping():
    """Test that all JSON entries have corresponding image files"""
    tester = TestMetadataIntegrity()

    with open(METADATA_FILE) as f:
        data = json.load(f)

    # Test each JSON entry has a file
    missing_files = []
    for i, entry in enumerate(data):
        filename = entry.get('newFilename')
        if not filename:
            tester.test(f"Entry {i+1} has newFilename", False)
            continue

        image_path = IMAGE_DIR / filename
        if not image_path.exists():
            missing_files.append(filename)

    tester.test(
        "All JSON entries have corresponding image files",
        len(missing_files) == 0,
        f"Missing files: {', '.join(missing_files[:5])}" +
        (f" and {len(missing_files)-5} more" if len(missing_files) > 5 else "")
    )

    # Test all image files have JSON entries
    json_filenames = {entry['newFilename'] for entry in data if 'newFilename' in entry}
    image_files = list(IMAGE_DIR.glob("*.jpg"))

    orphaned_files = []
    for image_file in image_files:
        if image_file.name not in json_filenames:
            orphaned_files.append(image_file.name)

    tester.test(
        "All image files have JSON entries",
        len(orphaned_files) == 0,
        f"Orphaned files: {', '.join(orphaned_files[:5])}" +
        (f" and {len(orphaned_files)-5} more" if len(orphaned_files) > 5 else "")
    )

    return tester

def test_data_quality():
    """Test data quality - duplicates, null values, etc."""
    tester = TestMetadataIntegrity()

    with open(METADATA_FILE) as f:
        data = json.load(f)

    # Test for duplicate filenames
    filenames = [entry.get('newFilename') for entry in data]
    unique_filenames = set(filenames)

    tester.test(
        "No duplicate newFilename values",
        len(filenames) == len(unique_filenames),
        f"Found {len(filenames) - len(unique_filenames)} duplicates"
    )

    # Test for null/empty required fields
    entries_with_issues = []
    for i, entry in enumerate(data):
        issues = []
        if not entry.get('title') or entry.get('title') == '':
            issues.append('empty title')
        if not entry.get('description') or entry.get('description') == '':
            issues.append('empty description')
        if not entry.get('newFilename') or entry.get('newFilename') == '':
            issues.append('empty filename')

        if issues:
            entries_with_issues.append(f"Entry {i+1} ({entry.get('newFilename', 'unknown')}): {', '.join(issues)}")

    tester.test(
        "No entries with empty required fields",
        len(entries_with_issues) == 0,
        f"\n  " + "\n  ".join(entries_with_issues[:3]) +
        (f"\n  and {len(entries_with_issues)-3} more" if len(entries_with_issues) > 3 else "")
    )

    # Test that tags arrays aren't empty
    entries_with_empty_tags = []
    for i, entry in enumerate(data):
        if 'tags' in entry:
            tags = entry['tags']
            for tag_type in ['conceptual', 'subject', 'colors', 'style']:
                if tag_type in tags and len(tags[tag_type]) == 0:
                    entries_with_empty_tags.append(
                        f"Entry {i+1} ({entry.get('newFilename', 'unknown')}): empty {tag_type}"
                    )

    tester.warn(
        "All entries have non-empty tag arrays",
        len(entries_with_empty_tags) == 0,
        f"\n  " + "\n  ".join(entries_with_empty_tags[:3]) +
        (f"\n  and {len(entries_with_empty_tags)-3} more" if len(entries_with_empty_tags) > 3 else "")
    )

    return tester

def test_analyzed_colors():
    """Test analyzed_colors field structure"""
    tester = TestMetadataIntegrity()

    with open(METADATA_FILE) as f:
        data = json.load(f)

    # Count entries with analyzed_colors
    entries_with_colors = sum(
        1 for entry in data
        if 'tags' in entry and 'analyzed_colors' in entry['tags']
    )

    tester.warn(
        "Most entries have analyzed_colors",
        entries_with_colors > len(data) * 0.8,
        f"Only {entries_with_colors}/{len(data)} have analyzed_colors"
    )

    # Validate analyzed_colors structure
    invalid_colors = []
    for i, entry in enumerate(data):
        if 'tags' not in entry or 'analyzed_colors' not in entry['tags']:
            continue

        colors = entry['tags']['analyzed_colors']
        required = ['dominant', 'accent', 'named']

        for field in required:
            if field not in colors:
                invalid_colors.append(
                    f"Entry {i+1} ({entry.get('newFilename', 'unknown')}): missing '{field}'"
                )
            elif not isinstance(colors[field], list):
                invalid_colors.append(
                    f"Entry {i+1} ({entry.get('newFilename', 'unknown')}): '{field}' is not a list"
                )

    tester.test(
        "analyzed_colors have valid structure",
        len(invalid_colors) == 0,
        f"\n  " + "\n  ".join(invalid_colors[:3]) +
        (f"\n  and {len(invalid_colors)-3} more" if len(invalid_colors) > 3 else "")
    )

    return tester

def main():
    """Run all tests"""
    print("=" * 80)
    print("METADATA INTEGRITY TESTS")
    print("=" * 80)
    print()

    all_results = []

    print("📁 File existence tests:")
    all_results.append(test_file_exists())
    print()

    print("📄 JSON structure tests:")
    all_results.append(test_json_structure())
    print()

    print("🔗 File-JSON mapping tests:")
    all_results.append(test_file_image_mapping())
    print()

    print("✨ Data quality tests:")
    all_results.append(test_data_quality())
    print()

    print("🎨 Color analysis tests:")
    all_results.append(test_analyzed_colors())
    print()

    # Summary
    total_passed = sum(r.passed for r in all_results)
    total_failed = sum(r.failed for r in all_results)
    total_warnings = sum(r.warnings for r in all_results)

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"✓ Passed: {total_passed}")
    print(f"✗ Failed: {total_failed}")
    print(f"⚠ Warnings: {total_warnings}")
    print()

    if total_failed > 0:
        print("❌ TESTS FAILED - Please fix the issues above")
        sys.exit(1)
    elif total_warnings > 0:
        print("⚠️  TESTS PASSED WITH WARNINGS")
        sys.exit(0)
    else:
        print("✅ ALL TESTS PASSED")
        sys.exit(0)

if __name__ == "__main__":
    main()
