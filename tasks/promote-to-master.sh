#!/usr/bin/env bash

set -ex

pushd src-stable
  git remote add dev file://../src-dev
  git fetch dev dev
  git checkout master
  git merge dev/dev
popd
