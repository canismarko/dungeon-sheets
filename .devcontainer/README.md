# Dev Container Configuration

This directory contains the VS Code Dev Container configuration for the dungeon-sheets project.

## Features

- **Python 3.12**: Base development environment
- **TeX Live**: Minimal installation with required packages for PDF generation
- **pdftk-java**: For PDF form filling
- **Docker-in-Docker**: Build and test Docker images within the dev container
- **Git**: Version control tools

## TeX Live Packages

The setup installs a minimal TeX Live distribution with packages defined in `install-texlive-packages.sh`:

- `collection-latexrecommended`: Core LaTeX packages
- Fonts: `bookman`, `gillius`, `kpfonts`, `lettrine`, `contour`, `avantgar`
- Layout: `xcolor`, `fontaxes`, `booktabs`, `enumitem`, `needspace`, `geometry`, `fancyhdr`, `caption`
- Core utilities: `supertabular`, `etoolbox`, `hyperref`, `graphics-def`, `epstopdf-pkg`

This shared package list ensures consistency between the Dockerfile and dev container setup.

To add or remove packages, edit `.devcontainer/install-texlive-packages.sh`.

This keeps the installation small (~300MB) while providing all necessary functionality.

## Manual Installation

If you need to install TeX Live manually in the current container:

```bash
bash .devcontainer/setup.sh
source /etc/profile.d/texlive.sh
```

## Testing

After setup, verify installation:

```bash
# Check pdflatex is available
which pdflatex
pdflatex --version

# Run tests
pytest tests/

# Generate a character sheet
makesheets examples/wizard1.py
```

## Rebuilding the Container

To apply changes to the dev container configuration:

1. Open Command Palette (Ctrl+Shift+P / Cmd+Shift+P)
2. Select "Dev Containers: Rebuild Container"

This will recreate the container and run the setup script.
