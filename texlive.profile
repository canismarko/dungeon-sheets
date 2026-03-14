# TeX Live installation profile for dungeon-sheets Docker container
# This configures a minimal TeX Live installation that we'll extend with tlmgr

# Use the basic scheme (minimal installation)
# This includes only essential LaTeX packages (~200MB vs ~7GB for full)
selected_scheme scheme-basic

# Don't automatically adjust PATH in shell profile files
# We handle this explicitly in the Dockerfile with ENV
instopt_adjustpath 0

# Skip documentation files to save space
# We can always refer to online docs at https://ctan.org
tlpdbopt_install_docfiles 0

# Skip source files to save space
# We only need the compiled packages, not their sources
tlpdbopt_install_srcfiles 0

# Set explicit installation paths to avoid year-based directory issues
# This makes the installation path predictable and simplifies PATH management
TEXDIR /usr/local/texlive
TEXMFLOCAL /usr/local/texlive/texmf-local
TEXMFSYSCONFIG /usr/local/texlive/texmf-config
TEXMFSYSVAR /usr/local/texlive/texmf-var
TEXMFCONFIG ~/.texlive/texmf-config
TEXMFVAR ~/.texlive/texmf-var
TEXMFHOME ~/texmf
