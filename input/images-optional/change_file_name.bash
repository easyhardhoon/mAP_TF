i=1
for file in *.jpg; do
  mv "$file" "${i}.jpg"
  i=$((i+1))
done

