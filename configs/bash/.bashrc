# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='[\u@\h \W]\$ '
#PS1='\[\033[1;36m\]\u\[\033[1;31m\]@\[\033[1;32m\]\h:\[\033[1;35m\]\w\[\033[1;31m\]\$\[\033[0m\] '

### ALIAS ### ---------------------------------------------------------
alias ba='nvim ~/.bashrc'
alias src='source ~/.bashrc'
alias ls='ls --color=auto'
alias grep='grep --color=auto'

alias coding='cd ~/Projects/Coding/ && y'

alias band='bandcamp-dl -ferku'

### Put my Scripts on path----------------------------------------------

export PATH=$PATH:~/Scripts/

### --------------------------------------------------------------------

# Function to make ranger quit and cd to the last dir
function ranger_dir {
    local IFS=$'\t\n'
    local tempfile="$(mktemp -t tmp.XXXXXX)"
    local ranger_cmd=(
        command
        ranger
        --cmd="map Q chain shell echo %d > "$tempfile"; quitall"
    )
    
    ${ranger_cmd[@]} "$@"
    if [[ -f "$tempfile" ]] && [[ "$(cat -- "$tempfile")" != "$(echo -n `pwd`)" ]]; then
        cd -- "$(cat "$tempfile")" || return
    fi
    command rm -f -- "$tempfile" 2>/dev/null
}

alias ranger=ranger_dir

### MISC ### -----------------------------------------------------------

# Color suport for less, man, etc.
export LESS="--RAW-CONTROL-CHARS"
[[ -f ~/.LESS_TERMCAP ]] && . ~/.LESS_TERMCAP

# Some misc exports
export EDITOR=nvim
