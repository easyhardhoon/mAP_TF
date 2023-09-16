#!/bin/bash
start_number=0
end_number=6

for ((i = $start_number; i <= $end_number; i++)); do
  folder_name="DOT_$i"
  mkdir -p "$folder_name"
done

