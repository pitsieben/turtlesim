#!/bin/zsh
set -e

# setup ros environment
source "/opt/ros/noetic/setup.zsh"

exec "$@"