#!/usr/bin/env bash
set -e

rm -rf build/* || exit 0;
mkdir build;
pip install -U pip
pip install misaka==1.0.2
pip install mynt==0.2.3
mynt gen -f . build
( cd build
  git init
  git config user.name "Travis-CI"
  git config user.email "contact@travis-ci.com"
  cp ../CNAME ./CNAME
  git add .
  git commit -m "Deployed to Github Pages"
  git push --force --quiet "https://${GH_TOKEN}@${GH_REF}" master:gh-pages > /dev/null 2>&1
)
