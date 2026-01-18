# Test Suite Documentation

This project includes automated tests to prevent regressions and ensure data quality.

## Test Suites

### 1. Metadata Integrity Tests (`test_metadata_integrity.py`)

**What it tests:**
- ✅ Metadata file exists and is valid JSON
- ✅ All required fields present (title, description, tags, etc.)
- ✅ Every JSON entry has a corresponding image file
- ✅ Every image file has a JSON entry (no orphaned files)
- ✅ No duplicate filenames
- ✅ No empty/null required fields
- ✅ All tag arrays are populated
- ✅ `analyzed_colors` structure is valid

**Run standalone:**
```bash
python3 test_metadata_integrity.py
```

### 2. Search Functionality Tests (`test_search.js`)

**What it tests:**
- ✅ Basic search returns correct results
- ✅ Tennis search only returns tennis images
- ✅ Color searches return color-relevant images
- ✅ Empty search returns all images
- ✅ Search doesn't match internal data structures (like hex codes)
- ✅ Specific regression tests (Blush Gears → Broken Heart)
- ✅ Search performance (<50ms average)

**Run standalone:**
```bash
node test_search.js
```

### 3. Run All Tests

**Recommended:** Run all test suites together:
```bash
./run_all_tests.sh
```

This runs both test suites and provides a unified pass/fail status.

## When to Run Tests

### 1. Before Committing Changes
Always run tests before committing to catch issues early:
```bash
./run_all_tests.sh
```

### 2. After Re-analyzing Images
If you re-run image analysis scripts:
```bash
python3 analyze_images.py  # or any analysis script
./run_all_tests.sh         # verify integrity
```

### 3. After Manual Edits to JSON
If you manually edit `images_metadata.json`:
```bash
./run_all_tests.sh
```

### 4. After Adding New Images
When adding new images to the collection:
1. Run analysis scripts
2. Run tests to ensure everything is properly integrated

## Regression Tests

The test suite includes specific regression tests for known issues:

### Blush Gears → Broken Heart (Entry 81)
- **Issue**: Image file named "blush-gears-gradient.jpg" showed a broken heart, not gears
- **Test**: Verifies title is "Broken Heart"
- **Location**: `test_search.js` - "Entry 81 blush-gears is labeled as Broken Heart"

### Tennis Search Accuracy
- **Issue**: Search for "tennis" returned many non-tennis images
- **Test**: Verifies only tennis-related images are returned
- **Location**: `test_search.js` - "Search tennis returns only tennis images"

### Hex Code Search Bug
- **Issue**: Search was matching internal hex color codes in `analyzed_colors`
- **Test**: Verifies hex codes are not searchable
- **Location**: `test_search.js` - "Search does not match color hex codes"

## Adding New Tests

### For Metadata Issues:
Edit `test_metadata_integrity.py` and add a new test function:

```python
def test_my_new_check():
    tester = TestMetadataIntegrity()

    with open(METADATA_FILE) as f:
        data = json.load(f)

    # Your test logic here
    tester.test("My test name", condition, "Error message")

    return tester

# Then add to main():
all_results.append(test_my_new_check())
```

### For Search Issues:
Edit `test_search.js` and add to the `runTests()` function:

```javascript
runner.test('My test description', () => {
    const results = searchImages('my query');

    return {
        success: /* your condition */,
        message: 'Result description'
    };
});
```

## Continuous Integration

To integrate with CI/CD (GitHub Actions, etc.):

```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '18'
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Run tests
        run: ./run_all_tests.sh
```

## Test Results

Current test coverage:
- **Metadata Integrity**: 20 tests
- **Search Functionality**: 8 tests
- **Total**: 28 automated tests

All tests currently passing ✅

## Troubleshooting

### Tests fail with "node: command not found"
Install Node.js: `brew install node` (macOS) or use your package manager

### Tests fail with "ANTHROPIC_API_KEY not set"
The test suite doesn't require the API key - it only tests the metadata and search logic

### Orphaned file errors
Remove orphaned files:
```bash
# Find files not in JSON
ls editorial_feed_images/*.jpg | while read file; do
    filename=$(basename "$file")
    if ! grep -q "$filename" images_metadata.json; then
        echo "Orphaned: $filename"
        # rm "$file"  # Uncomment to delete
    fi
done
```

## Exit Codes

- `0`: All tests passed
- `1`: One or more tests failed

Use in scripts:
```bash
./run_all_tests.sh && echo "Deploy safe!" || echo "Fix tests first!"
```
