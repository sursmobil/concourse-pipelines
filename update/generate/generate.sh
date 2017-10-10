#!/usr/bin/env bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pip install -r $DIR/requirements.txt

$DIR/generate.py
