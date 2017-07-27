#!/usr/bin/env bash

set -ex

pushd src
  git config user.name "CI"
  git config user.email "ci@ci.ci"
  git add --all
  git commit -m "$MESSAGE"
popd
