#!/bin/bash

copy_and_run() {
  source_folder="$1"
  python_script="$2"

  cd "$source_folder"
  cp -r *.txt ../../../detection-results
  cd ../../../../
  python3 "$python_script" --no-plot

  echo "Completed processing $source_folder"
}

copy_and_run "./input/DOT/choose_1/DOT_0" "main.py"
copy_and_run "./input/DOT/choose_1/DOT_1" "main.py"
copy_and_run "./input/DOT/choose_1/DOT_2" "main.py"
copy_and_run "./input/DOT/choose_1/DOT_3" "main.py"
copy_and_run "./input/DOT/choose_1/DOT_4" "main.py"
copy_and_run "./input/DOT/choose_1/DOT_5" "main.py"
copy_and_run "./input/DOT/choose_1/DOT_6" "main.py"

