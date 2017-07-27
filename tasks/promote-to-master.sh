#!/usr/bin/env bash

set -ex

pushd src
  git fetch origin master
  git checkout -b master
  git merge dev
popd
