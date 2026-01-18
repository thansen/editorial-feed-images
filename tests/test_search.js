#!/usr/bin/env node
/**
 * Test suite for search functionality
 * Run with: node test_search.js
 */

const fs = require('fs');
const path = require('path');

// Load metadata
const metadata = JSON.parse(
    fs.readFileSync('./images_metadata.json', 'utf8')
);

// Color keywords (same as in index.html)
const colorKeywords = [
    'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown',
    'black', 'white', 'gray', 'grey', 'cyan', 'magenta', 'lime', 'maroon',
    'navy', 'olive', 'teal', 'aqua', 'silver', 'gold', 'crimson', 'violet',
    'indigo', 'turquoise', 'coral', 'salmon', 'khaki', 'lavender', 'plum'
];

// Search implementation (matches index.html logic)
function searchImages(query) {
    if (!query) return metadata;

    const searchLower = query.toLowerCase().trim();

    // Check if search term is a color keyword
    const isColorSearch = colorKeywords.some(color =>
        searchLower.includes(color) || color.includes(searchLower)
    );

    if (isColorSearch) {
        // Color search with weighted scoring
        const scored = metadata.map(img => {
            let score = 0;

            if (img.tags.analyzed_colors) {
                const analyzed = img.tags.analyzed_colors;
                if (analyzed.named) {
                    analyzed.named.forEach((color, index) => {
                        if (color.toLowerCase().includes(searchLower)) {
                            score += 10 - (index * 2);
                        }
                    });
                }
            }

            const colorTags = img.tags.colors || [];
            if (colorTags.some(tag => tag.toLowerCase().includes(searchLower))) {
                score += 5;
            }

            return { img, score };
        }).filter(item => item.score > 0);

        scored.sort((a, b) => b.score - a.score);
        return scored.map(item => item.img);
    } else {
        // Non-color search
        return metadata.filter(img => {
            if (img.title.toLowerCase().includes(searchLower)) return true;
            if (img.description.toLowerCase().includes(searchLower)) return true;

            const searchableTags = [
                ...(img.tags.conceptual || []),
                ...(img.tags.subject || []),
                ...(img.tags.colors || []),
                ...(img.tags.style || [])
            ];

            return searchableTags.some(tag =>
                tag.toLowerCase().includes(searchLower)
            );
        });
    }
}

// Test framework
class TestRunner {
    constructor() {
        this.passed = 0;
        this.failed = 0;
        this.tests = [];
    }

    test(name, testFn) {
        try {
            const result = testFn();
            if (result.success) {
                console.log(`✓ ${name}`);
                if (result.message) {
                    console.log(`  → ${result.message}`);
                }
                this.passed++;
            } else {
                console.log(`✗ ${name}`);
                console.log(`  → ${result.message || 'Test failed'}`);
                this.failed++;
            }
        } catch (error) {
            console.log(`✗ ${name}`);
            console.log(`  → Error: ${error.message}`);
            this.failed++;
        }
    }

    summary() {
        console.log('\n' + '='.repeat(80));
        console.log('SUMMARY');
        console.log('='.repeat(80));
        console.log(`✓ Passed: ${this.passed}`);
        console.log(`✗ Failed: ${this.failed}`);
        console.log();

        if (this.failed > 0) {
            console.log('❌ TESTS FAILED');
            process.exit(1);
        } else {
            console.log('✅ ALL TESTS PASSED');
            process.exit(0);
        }
    }
}

// Tests
function runTests() {
    const runner = new TestRunner();

    console.log('='.repeat(80));
    console.log('SEARCH FUNCTIONALITY TESTS');
    console.log('='.repeat(80));
    console.log();

    console.log('🔍 Basic search tests:');

    // Test 1: Tennis search should only return tennis images
    runner.test('Search "tennis" returns only tennis images', () => {
        const results = searchImages('tennis');
        const hasNonTennis = results.some(img => {
            const text = JSON.stringify(img).toLowerCase();
            return !text.includes('tennis');
        });

        return {
            success: !hasNonTennis && results.length > 0,
            message: `Found ${results.length} result(s)${hasNonTennis ? ' (includes non-tennis images!)' : ''}`
        };
    });

    // Test 2: Search for specific title
    runner.test('Search finds exact title matches', () => {
        // Find an image with unique title
        const targetImage = metadata.find(img => img.title === 'Broken Heart');
        if (!targetImage) {
            return { success: false, message: 'Test image not found' };
        }

        const results = searchImages('Broken Heart');
        const found = results.some(img => img.title === 'Broken Heart');

        return {
            success: found,
            message: `${found ? 'Found' : 'Did not find'} "Broken Heart" in results`
        };
    });

    // Test 3: Color search returns color-relevant results
    runner.test('Search "red" returns red-colored images', () => {
        const results = searchImages('red');
        const hasRed = results.length > 0 && results.every(img => {
            const colors = img.tags.colors || [];
            const analyzedColors = img.tags.analyzed_colors?.named || [];
            return colors.some(c => c.toLowerCase().includes('red')) ||
                   analyzedColors.some(c => c.toLowerCase().includes('red'));
        });

        return {
            success: hasRed && results.length > 0,
            message: `Found ${results.length} red image(s)`
        };
    });

    // Test 4: Empty search returns all images
    runner.test('Empty search returns all images', () => {
        const results = searchImages('');
        return {
            success: results.length === metadata.length,
            message: `Returned ${results.length}/${metadata.length} images`
        };
    });

    // Test 5: Search doesn't match analyzed_colors object structure
    runner.test('Search does not match color hex codes', () => {
        // Search for a hex color that exists in analyzed_colors
        const results = searchImages('#ca387f');
        return {
            success: results.length === 0,
            message: results.length > 0 ? 'ERROR: Matched hex codes!' : 'Correctly ignored hex codes'
        };
    });

    console.log();
    console.log('🎯 Specific regression tests:');

    // Test 6: Blush Gears regression test
    runner.test('Entry 81 "blush-gears" is labeled as "Broken Heart"', () => {
        const entry = metadata.find(img => img.newFilename === 'blush-gears-gradient.jpg');
        if (!entry) {
            return { success: false, message: 'blush-gears-gradient.jpg not found' };
        }

        return {
            success: entry.title === 'Broken Heart',
            message: `Title is "${entry.title}"`
        };
    });

    // Test 7: Honeydew Gears regression test
    runner.test('Entry 109 "honeydew-gears" is labeled correctly', () => {
        const entry = metadata.find(img => img.newFilename === 'honeydew-green-gears-gradient.jpg');
        if (!entry) {
            return { success: false, message: 'honeydew-green-gears-gradient.jpg not found' };
        }

        const isTennis = entry.title.toLowerCase().includes('tennis') ||
                        entry.tags.subject.some(s => s.includes('tennis'));

        return {
            success: isTennis,
            message: `Title is "${entry.title}" (${isTennis ? 'correct' : 'should mention tennis'})`
        };
    });

    console.log();
    console.log('⚡ Performance tests:');

    // Test 8: Search performance
    runner.test('Search completes in reasonable time', () => {
        const start = Date.now();
        const iterations = 100;

        for (let i = 0; i < iterations; i++) {
            searchImages('test');
        }

        const elapsed = Date.now() - start;
        const avgTime = elapsed / iterations;

        return {
            success: avgTime < 50, // Should be < 50ms per search
            message: `Average: ${avgTime.toFixed(2)}ms per search`
        };
    });

    console.log();
    runner.summary();
}

// Run tests
if (require.main === module) {
    runTests();
}

module.exports = { searchImages };
