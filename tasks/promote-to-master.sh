#!/usr/bin/env bash

set -ex

pushd src-dev
  git fetch origin master
  git checkout -b master origin/master
  git merge dev
popd
