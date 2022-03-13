#!/bin/sh

if [ -d "venv" ]; then
  rm -rf venv
fi
if [ -d ".shadowenv.d" ]; then
  rm -rf .shadowenv.d
fi
python3 -m venv venv &&\
source venv/bin/activate &&\
pip install -U pip &&\
pip install -e . &&\
deactivate

mkdir .shadowenv.d &&\
cp shadowenv/* .shadowenv.d/ &&\
shadowenv trust
$SHELL
