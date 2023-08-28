#!/bin/bash

directory="/"

# 디렉토리로 이동
cd "$directory"

# 모든 파일 이름에서 "tvmonitor"를 "tvmonitor"로 변경
for file in *; do
    new_name=$(echo "$file" | sed 's/tvmonitor/tvmonitor/g')
    mv "$file" "$new_name"
done

echo "파일 이름 변경이 완료되었습니다."

