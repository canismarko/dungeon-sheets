autoload -Uz compinit
compinit -i

# Settings from zsh-utils are here
bindkey -e

# Convenient path navigation, e.g., `cd vp`
setopt CDABLE_VARS

# Use Starship CLI
eval "$(starship init zsh)"
