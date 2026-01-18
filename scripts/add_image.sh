#!/bin/bash
# Simple wrapper to add a new image to the collection
# Ensures API key is set and runs the integration script

cd "$(dirname "$0")/.."

# Check if API key is set
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "❌ ANTHROPIC_API_KEY not set"
    echo ""
    echo "Please set your API key:"
    echo "  export ANTHROPIC_API_KEY='your-key-here'"
    echo ""
    echo "Or run with the key inline:"
    echo "  ANTHROPIC_API_KEY='your-key' scripts/add_image.sh"
    exit 1
fi

echo "🖼️  Adding new image to collection..."
echo ""

# Run the integration script
python3 scripts/integrate_new_image.py

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Integration complete!"
    echo ""
    echo "Running tests to verify..."
    tests/run_all_tests.sh

    if [ $? -eq 0 ]; then
        echo ""
        echo "🎉 All done! Refresh your browser to see the new image."
    fi
else
    echo ""
    echo "❌ Integration failed. Check the error above."
    exit 1
fi
