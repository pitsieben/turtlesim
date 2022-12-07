#!/usr/bin/env bash

echo -e "Building moveit1_abb:lastest"

docker build --pull --rm -f ./.docker/Dockerfile_zsh  -t ros_tutorials:latest .