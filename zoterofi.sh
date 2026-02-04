#!/bin/bash

BASE_DIR=$(cd -- $(dirname -- "$BASH_SOURCE[0]") && pwd)

$BASE_DIR/venv/bin/python $BASE_DIR/zoterofi.py
