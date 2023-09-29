#!/usr/bin/env bash
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

docker build --network=host -t grand_challenge_algorithm "$SCRIPTPATH"