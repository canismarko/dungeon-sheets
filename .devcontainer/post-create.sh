#!/bin/bash
set -ex

echo "Initializing development environment..."

# Initialize git submodules
# If submodule init fails due to missing commits, try remote update
if ! git submodule update --init --recursive; then
    echo "Standard submodule update failed, trying remote update..."
    git submodule update --init --recursive --remote
fi

# Install dungeon-sheets in editable mode with dev dependencies
pip install -e ".[dev]"

echo "Development environment ready!"
