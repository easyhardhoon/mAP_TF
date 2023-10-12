#!/bin/bash

for i in {0..6}; do
  source_folder="./input/DOT/choose_6/DOT_$i"
  python_script="main.py"

  copy_and_run() {
    cd "$1"
    cp -r *.txt ../../../detection-results
    cd ../../../../
    python3 "$2" --no-plot
    echo "Completed processing $1"
  }

  copy_and_run "$source_folder" "$python_script"
done

