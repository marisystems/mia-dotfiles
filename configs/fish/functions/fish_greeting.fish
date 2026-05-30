function fish_greeting
  echo -ne '\x1b[38;5;16m'
  echo '						'
  echo ' _____         _             _                 	'
  echo '|     |___ ___|_|___ _ _ ___| |_ ___ _____ ___ 	'
  echo '| | | | .'|  _| |_ -| | |_ -|  _| -_|     |_ -|	'
  echo '|_|_|_|__,|_| |_|___|_  |___|_| |___|_|_|_|___|	'
  echo '                    |___|			'
  set_color normal
  fastfetch --key--padding-left 5
