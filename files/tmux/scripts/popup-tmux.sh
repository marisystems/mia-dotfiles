width=${2:-80%}
height=${2:-80%}
if [ "$(tmux display-message -p -F "#{session_name}")" = "popup" ];then
  tmux detach-client
else
  #
  # Send output to /dev/null to avoid clunky behaviour
  tmux popup -d '#{pane_current_path}' -xC -yC -w80% -h75% -E "tmux attach -t popup || tmux new -s popup" >/dev/null || true
fi
