#!/usr/bin/env bash
set -e
for f in examples/*.py; do
  echo
  echo "============================================================"
  echo "RUNNING: $f"
  echo "============================================================"
  python "$f"
done
