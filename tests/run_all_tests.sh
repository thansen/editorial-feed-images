#!/bin/bash
# Run all test suites

# Change to project root directory
cd "$(dirname "$0")/.."

echo "================================================================================"
echo "RUNNING ALL TEST SUITES"
echo "================================================================================"
echo ""

EXIT_CODE=0

# Test 1: Metadata Integrity
echo "🔍 Running metadata integrity tests..."
python3 tests/test_metadata_integrity.py
if [ $? -ne 0 ]; then
    EXIT_CODE=1
fi
echo ""

# Test 2: Search Functionality
echo "🔍 Running search functionality tests..."
node tests/test_search.js
if [ $? -ne 0 ]; then
    EXIT_CODE=1
fi
echo ""

# Final summary
echo "================================================================================"
if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ ALL TEST SUITES PASSED"
else
    echo "❌ SOME TESTS FAILED - Please review the output above"
fi
echo "================================================================================"

exit $EXIT_CODE
