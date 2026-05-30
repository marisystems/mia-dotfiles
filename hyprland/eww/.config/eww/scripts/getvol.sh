#!/bin/sh
# Small script to get the sound level using amixer
amixer -D pulse sget Master | grep 'Left:' | awk -F'[][]' '{ print $2 }' | tr -d '%' | head -1
