#!/bin/sh
# Little script to get percentage of used RAM using the 'free' util
printf "%.0f%%\n" $(free -m | grep Mem | awk '{print ($3/$2)*100}')
