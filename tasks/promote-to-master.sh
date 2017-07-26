#!/usr/bin/env bash

set -ex

pushd src-dev
  git fetch origin master 
  git checkout master
  git merge dev
popd
