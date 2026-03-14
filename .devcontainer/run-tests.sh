#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

echo "======================================"
echo "Running Flake8 linting..."
echo "======================================"
uv run flake8 dungeonsheets/ --exit-zero

echo ""
echo "======================================"
echo "Testing makesheets (standard)..."
echo "======================================"
cd examples/
uv run makesheets --debug

echo ""
echo "======================================"
echo "Testing makesheets (fancy)..."
echo "======================================"
uv run makesheets --debug --fancy

echo ""
echo "======================================"
echo "Testing makesheets (epub)..."
echo "======================================"
uv run makesheets --debug --output-format=epub

echo ""
echo "======================================"
echo "Running pytest with coverage..."
echo "======================================"
cd ../
uv run pytest --cov=dungeonsheets tests/

echo ""
echo "======================================"
echo "All tests passed successfully!"
echo "======================================"
