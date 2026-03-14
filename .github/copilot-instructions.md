# AI Agent Instructions for dungeon-sheets

This document guides AI coding agents on effectively working with the dungeon-sheets codebase, a tool for creating D&D 5e character sheets and session notes.

## Project Overview

dungeon-sheets is a Python package that:

- Generates character sheets and GM notes for D&D 5th Edition
- Supports multiple output formats (PDF, ePub)
- Handles character data from Python files and VTT JSON exports
- Requires Python 3.9+ and uses modern Python features

## Development Workflow (GitHub Flow)

This project follows the **GitHub Flow** model. All changes must be made on a feature branch before raising a pull request:

1. **Create a Feature Branch**:

   ```bash
   # Ensure you're on main and up to date
   git checkout main
   git pull origin main

   # Create a new branch with a descriptive name
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   # or
   git checkout -b perf/performance-improvement
   ```

2. **Make Changes**:

   - Implement your feature or fix
   - Write/update tests as needed
   - Ensure all tests pass locally

3. **Commit and Push**:

   ```bash
   git add .
   git commit -m "Descriptive commit message"
   # First push of a new branch - set upstream
   git push -u origin feature/your-feature-name
   # Subsequent pushes
   git push
   ```

4. **Create Pull Request**:

   - Set default repository for GitHub CLI (first time only):
     ```bash
     gh repo set-default stiffneckjim/dungeon-sheets
     ```
   - Open a PR from your branch to `main`:
     ```bash
     gh pr create --title "Your PR title" --body "PR description" --base main
     ```
   - CI/CD workflows will automatically run
   - Address any review feedback

5. **Branch Naming Conventions**:
   - `feature/` - New features or enhancements
   - `fix/` - Bug fixes
   - `perf/` - Performance improvements
   - `docs/` - Documentation updates
   - `refactor/` - Code refactoring

**Never commit directly to `main`**. Always work on a feature branch and use pull requests for code review and CI validation.

## Core Architecture

The project follows a modular architecture with these key components:

1. **Character Model** (`dungeonsheets/character.py`):

   - Base `Character` class that other classes inherit from
   - Handles core character attributes, calculated stats, and feature management

2. **Content System** (`dungeonsheets/content_registry.py`, `dungeonsheets/content.py`):

   - Registry pattern for D&D content (spells, items, features)
   - Use `content_registry.register_X()` for adding new content

3. **Output Generation** (`dungeonsheets/make_sheets.py`):
   - Entry point for sheet generation via `makesheets` command
   - Supports PDF (via pdftk/pypdf), LaTeX, and ePub formats

## CI/CD Pipeline

The project uses GitHub Actions for continuous integration and deployment:

### Manual Workflow Triggers

Both workflows support manual triggering through GitHub's UI:

1. **Triggering Workflows**:

   - Go to Actions tab in the repository
   - Select the workflow (Python package or Docker)
   - Click "Run workflow" button
   - Choose:
     - Branch to run against
     - Input parameters (if any)

2. **Use Cases**:

   - Testing changes before committing
   - Rebuilding failed runs
   - Generating container images for testing
   - Validating specific Python versions

3. **Monitoring**:

   ```bash
   # Check status of PR checks
   gh pr checks 1

   # View workflow run logs
   gh run view <run-id>

   # Download artifacts from a run
   gh run download <run-id>
   ```

### Python CI Workflow

Tests run on all supported Python versions (3.9-3.12):

1. **Environment Setup**:

   - Installs system dependencies (pdftk, texlive)
   - Configures Python environment

   ```yaml
   sudo apt-get -y install pdftk texlive-latex-base texlive-latex-extra texlive-fonts-recommended
   ```

2. **Test Suite**:

   - Runs pytest with coverage reporting
   - Validates code style with flake8
   - Tests example character generation

   ```bash
   pytest --cov=dungeonsheets tests/
   flake8 dungeonsheets/ --exit-zero
   ```

3. **Output Format Validation**:
   ```bash
   makesheets --debug          # Standard PDF
   makesheets --debug --fancy  # Enhanced formatting
   makesheets --debug --output-format=epub  # ePub generation
   ```

### Docker Workflow

Builds and publishes container images:

1. **Multi-architecture Support**:

   - Builds for amd64 and arm64
   - Uses QEMU and Docker Buildx

2. **Container Registry**:

   - Publishes to GitHub Container Registry (GHCR)
   - Tags: `main` (latest development), version tags for releases

   ```bash
   docker pull ghcr.io/stiffneckjim/dungeon-sheets:main
   ```

3. **Container Features**:
   - Ubuntu-based with all dependencies pre-installed
   - Mounts current directory as `/build` for character files
   - Includes latest package version from branch/tag

## Key Workflows

### Dependency Management

This project uses **[uv](https://docs.astral.sh/uv/)** for fast, reliable Python package management:

```bash
uv sync              # Install all dependencies from uv.lock
uv sync --all-extras # Install with all optional dependencies (dev, etc.)
uv add package-name  # Add a new dependency
uv remove package-name # Remove a dependency
uv lock              # Update uv.lock after changing pyproject.toml
```

**Important**: Always use `uv` commands instead of `pip` for consistency. The `uv.lock` file ensures reproducible builds and is automatically used in CI/CD and devcontainers.

### Testing

```bash
uv sync --all-extras # Install dev dependencies
pytest tests/        # Run test suite
pytest tests/ -k test_name  # Run specific test
```

### Development Setup

```bash
uv sync              # Install in editable mode with locked dependencies
sudo apt-get -y install pdftk texlive-latex-base texlive-latex-extra texlive-fonts-recommended  # Optional: PDF dependencies
```

## Project Conventions

1. **Class Creation**:

   - Character classes (Fighter, Wizard, etc.) inherit from `Character`
   - New features should be registered via `content_registry`
   - Example: See `dungeonsheets/classes/wizard.py`

2. **Testing**:

   - Tests are organized by component in `tests/`
   - Use `TestCase` for test classes
   - Mock external dependencies (pdftk, latex)

3. **Content Addition**:

   ```python
   from dungeonsheets.content_registry import register_spell

   @register_spell
   class NewSpell:
       """Follow existing spell pattern"""
       pass
   ```

## Integration Points

1. **PDF Generation**:

   - Primary: pdftk for form filling
   - Fallback: pypdf library
   - LaTeX for spell pages (optional)

2. **Data Import**:
   - Python character files (primary)
   - VTT JSON exports (supported formats in `dungeonsheets/readers.py`)

## Common Pitfalls

1. **PDF Generation**: Always check `pdftk` availability before using PDF-specific features
2. **Python Files**: Character files require exact class/feature names matching registry
3. **Dependencies**: Some features need external tools (pdftk, latex) - handle gracefully

## Example Files

Check these files to understand common patterns:

- Basic character: `examples/wizard1.py`
- Complex character: `examples/multiclass1.py`
- GM notes: `examples/gm-campaign-notes.py`
- Test patterns: `tests/test_character.py`


## Command Formatting Preference

When providing terminal commands, present them individually in separate code blocks rather than grouped together. This makes it easier to copy and paste commands one at a time for execution.

Example of preferred format:
```bash
cd /some/directory
```

```bash
git status
```

Rather than:
```bash
cd /some/directory
git status
```

