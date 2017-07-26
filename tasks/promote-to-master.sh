#!/usr/bin/env bash

set -ex

pushd src-dev
  git checkout master
  git merge dev
popd
