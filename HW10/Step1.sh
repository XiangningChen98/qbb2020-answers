cd week13_data/
cd KRAKEN
for file in *.kraken
do 
	echo "$file"
	cat $file | tr '[;]'  '[\t]' |sed 's/^..........//'>  "$file".txt
	KtImportText /Users/xiangning/qbb2020-answers/HW10/week13_data/KRAKEN/"$file".txt -o "$file".html
done