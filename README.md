# Editorial Feed Images Gallery

A curated collection of 133 editorial-style images with AI-powered metadata, programmatic color analysis, and an interactive web gallery.

![Gallery Preview](https://img.shields.io/badge/images-133-blue) ![Tests](https://img.shields.io/badge/tests-28%20passing-brightgreen)

## 🎨 Features

- **Interactive Web Gallery** - Browse 133 high-quality editorial images
- **Smart Search** - Search by title, description, subjects, concepts, colors, or styles
- **Color-Aware Search** - Weighted search prioritizes dominant colors
- **Randomized Display** - Fresh gallery order on each page load
- **Dual View Modes** - Toggle between Preview (1:1.3) and Full Image (1:1) aspect ratios
- **Programmatic Color Analysis** - Extracted dominant and accent colors from each image
- **Comprehensive Metadata** - AI-analyzed descriptions with detailed tagging
- **Automated Testing** - 28 tests ensure data integrity and search accuracy

## 🚀 Quick Start

### View the Gallery

1. Open `index.html` in your browser
2. Search for images by keyword (try "wizard", "tennis", "blue", "abstract")
3. Click any image for detailed view with download option
4. Toggle between Preview/Full Image modes in the top right

### Project Structure

```
editorial_feed_images/
├── index.html                     # Web gallery interface
├── images_metadata.json           # Image metadata (132 entries)
├── editorial_feed_images/         # Image files (132 .jpg files)
├── scripts/                       # Active utilities
│   ├── integrate_new_image.py     # Add new images to collection
│   ├── analyze_colors.py          # Extract colors from images
│   └── auto_validate_and_fix.py   # Validate and fix metadata
├── tests/                         # Test suite
│   ├── run_all_tests.sh           # Run all tests
│   ├── test_metadata_integrity.py # Data integrity tests (20 tests)
│   ├── test_search.js             # Search functionality tests (8 tests)
│   └── TESTING.md                 # Testing documentation
├── docs/                          # Additional documentation
│   ├── COLOR_ANALYSIS_README.md   # Color system documentation
│   └── CLEANUP_PLAN.md            # Project reorganization notes
└── archive/                       # Historical one-time scripts
```

## 📸 Adding New Images

To add a new image to the collection:

```bash
# 1. Place image in editorial_feed_images/ folder
cp your-new-image.jpg editorial_feed_images/

# 2. Set your Anthropic API key (one-time setup)
export ANTHROPIC_API_KEY='your-api-key-here'

# 3. Run the integration script
scripts/add_image.sh

# This will automatically:
# - Analyze image content with Claude Vision (~1-5¢ per image)
# - Extract dominant/accent colors
# - Generate clean filename
# - Add metadata entry
# - Rename file
# - Create backup
# - Run tests to verify

# 4. Refresh browser (Cmd+Shift+R) to see new image
```

**Cost**: ~1-5 cents per image for AI analysis. Totally worth it for accurate metadata!

## 🔍 Search Features

### Smart Search
- **Title & Description**: Direct text matching
- **Tags**: Searches conceptual, subject, color, and style tags
- **Color-Weighted**: Color searches prioritize dominant colors

### Color Search
Color searches use weighted scoring:
- **Dominant colors**: 10 points (highest priority)
- **Secondary colors**: 8 points
- **Accent colors**: 6 points
- **Color tags**: 5 points

Example: Search "blue" shows images with blue as the dominant color first.

### Supported Color Keywords
red, blue, green, yellow, orange, purple, pink, gold, crimson, navy, turquoise, teal, lime, coral, salmon, and 60+ more

## 🧪 Testing

Run the test suite to ensure data integrity:

```bash
# Run all tests
tests/run_all_tests.sh

# Run individual test suites
python3 tests/test_metadata_integrity.py  # Metadata integrity
node tests/test_search.js                  # Search functionality
```

**Current Test Coverage**: 28 tests
- ✅ File existence and JSON validity
- ✅ Required fields and data structure
- ✅ File-to-JSON mapping
- ✅ No duplicates or orphaned files
- ✅ Search accuracy and performance
- ✅ Regression tests for known issues

See [tests/TESTING.md](tests/TESTING.md) for detailed testing documentation.

## 📊 Metadata Structure

Each image has comprehensive metadata:

```json
{
  "originalFilename": "FLORA Image Color Editing.jpg",
  "newFilename": "wizard-football-purple.jpg",
  "title": "Wizard Football",
  "description": "A 3D rendered cartoon wizard in purple robes holding an American football",
  "tags": {
    "conceptual": ["magic", "sports", "fantasy", "fun"],
    "subject": ["wizard", "football", "character", "3d-render"],
    "colors": ["dodger-blue", "purple"],
    "style": ["3d-render", "cartoon", "cute", "gradient"],
    "analyzed_colors": {
      "dominant": ["#5B8FD8", "#7A3FD8"],
      "accent": ["#F4A460"],
      "named": ["dodger-blue", "medium-purple", "sandy-brown"]
    }
  }
}
```

## 🎨 Color Analysis System

The collection uses a hybrid color system:

1. **Programmatic Extraction** - PIL/Pillow analyzes actual pixel data
2. **Color Quantization** - Identifies dominant (>10% of image) and accent colors
3. **RGB to Named Color Mapping** - 80+ color names (crimson, dodger-blue, etc.)
4. **Weighted Search** - Prioritizes images by color relevance

See [docs/COLOR_ANALYSIS_README.md](docs/COLOR_ANALYSIS_README.md) for details.

## 🛠️ Maintenance Scripts

### Active Scripts (scripts/)

- **`integrate_new_image.py`** - Full pipeline for adding new images
- **`analyze_colors.py`** - Standalone color extraction utility
- **`auto_validate_and_fix.py`** - Validate metadata accuracy

### Archived Scripts (archive/)

Historical scripts used during initial setup and batch corrections. Kept for reference but not needed for normal operations.

## 📝 Image Collection

**Total Images**: 133
**File Format**: JPEG
**Naming Convention**: `descriptive-name-color.jpg`
**Themes**: Abstract art, sports, technology, nature, emojis, 3D renders, and more

### Sample Images
- Olympic Rings (multiple variations)
- Sports equipment (tennis rackets, footballs, baseball bats)
- Technology (game controllers, devices, DNA helixes)
- Characters (wizards, emojis, animals)
- Abstract patterns (waves, gradients, geometric shapes)

## 🚦 Status

✅ All systems operational
✅ 133 images integrated
✅ 28/28 tests passing
✅ Metadata validated
✅ Search functionality verified

## 📖 Documentation

- **[TESTING.md](tests/TESTING.md)** - Testing guide and test descriptions
- **[COLOR_ANALYSIS_README.md](docs/COLOR_ANALYSIS_README.md)** - Color system documentation
- **[CLEANUP_PLAN.md](docs/CLEANUP_PLAN.md)** - Project reorganization notes

## 🤝 Contributing

To add images or improve the system:

1. Add your image to `editorial_feed_images/` folder
2. Run `python3 scripts/integrate_new_image.py`
3. Run `tests/run_all_tests.sh` to verify
4. Ensure all tests pass before committing

## 🧹 Maintenance

**Validate metadata integrity:**
```bash
python3 scripts/auto_validate_and_fix.py
```

**Re-extract colors for all images:**
```bash
python3 scripts/analyze_colors.py
```

**Run tests before commits:**
```bash
tests/run_all_tests.sh
```

## 📜 License

Images and metadata for editorial use.

---

**Last Updated**: January 2026
**Image Count**: 133
**Test Coverage**: 28 tests passing
