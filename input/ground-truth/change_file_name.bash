i=1
for file in *.txt; do
  mv "$file" "${i}.txt"
  i=$((i+1))
done

