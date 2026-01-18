# Project Cleanup Plan

## Current Issues
- 23 Python scripts (many one-time use)
- Multiple backup files
- No clear project structure
- No main README

## Proposed Structure

```
editorial_feed_images/
├── README.md                          # Main documentation (NEW)
├── index.html                         # Web gallery
├── images_metadata.json               # Current metadata
├── editorial_feed_images/             # Image folder
├── scripts/                           # Active scripts (NEW)
│   ├── integrate_new_image.py         # Add new images
│   ├── analyze_colors.py              # Color extraction
│   └── auto_validate_and_fix.py       # Validation
├── tests/                             # Test suite (NEW)
│   ├── run_all_tests.sh
│   ├── test_metadata_integrity.py
│   ├── test_search.js
│   └── TESTING.md
├── archive/                           # One-time scripts (NEW)
│   ├── analyze_images.py
│   ├── reanalyze_images.py
│   ├── fix_metadata_batch.py
│   ├── update_first_30.py
│   ├── update_metadata_31_60.py
│   ├── update_entries_61_90*.py
│   ├── map_and_update.py
│   ├── extract_entries.py
│   ├── list_entries.py
│   ├── rename_files.py
│   ├── final_update_61_90.py
│   └── reanalyze_31_60.py
└── docs/                              # Documentation (NEW)
    ├── COLOR_ANALYSIS_README.md
    └── UPDATE_SUMMARY_31_60.md
```

## Files to Keep (Active Use)

### Core Files
- `index.html` - Web gallery interface
- `images_metadata.json` - Current metadata
- `test_search.js` - Search tests

### Active Scripts
- `integrate_new_image.py` - Full pipeline for adding new images
- `analyze_colors.py` - Color extraction utility
- `auto_validate_and_fix.py` - Metadata validation

### Tests
- `run_all_tests.sh` - Test runner
- `test_metadata_integrity.py` - Integrity tests
- `TESTING.md` - Test documentation

## Files to Archive (One-Time Use)

### Initial Setup Scripts
- `analyze_images.py` - Original image analysis (used once)
- `rename_files.py` - Initial file renaming (used once)
- `process_images.py` - Initial processing

### Batch Re-Analysis Scripts (Used During Fixes)
- `reanalyze_images.py`
- `reanalyze_31_60.py`
- `fix_metadata_batch.py`
- `update_first_30.py`
- `update_metadata_31_60.py`
- `update_entries_61_90.py`
- `update_entries_61_90_fixed.py`
- `final_update_61_90.py`
- `map_and_update.py`

### Helper Scripts
- `extract_entries.py`
- `list_entries.py`

## Files to Delete

### Backup Files (Keep Only Latest)
- `images_metadata.backup.json` (DELETE - old backup)
- Keep: `images_metadata.backup_before_new.json` (most recent)

## New Files to Create

### Main README.md
Complete project documentation including:
- Project overview
- How to use the gallery
- How to add new images
- Search features
- Testing

### .gitignore
Prevent committing unnecessary files:
- `*.backup*.json` (except explicitly tracked)
- `.DS_Store`
- `__pycache__/`
- `*.pyc`
- `validation_run.log`
- `/archive/` (if not tracking old scripts)

## Benefits of Cleanup

1. **Clearer structure** - Easy to find active vs archived scripts
2. **Better documentation** - Main README as entry point
3. **Easier maintenance** - Only active files in root
4. **New contributor friendly** - Clear what to use
5. **Reduced confusion** - Archive old one-time scripts

## Implementation Steps

1. Create new folders: `scripts/`, `tests/`, `archive/`, `docs/`
2. Move files to appropriate folders
3. Create main README.md
4. Create .gitignore
5. Delete old backup files
6. Update any path references in scripts
7. Test that everything still works
