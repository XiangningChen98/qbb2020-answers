cd ~/qbb2020-answers/HW2/alignment/
for sample in 09 11 23 24 27 31 35 39 62 63
do
	samtools sort -o ~/qbb2020-answers/HW2/alignment/A01_${sample}.sorted.bam -O bam  A01_${sample}.sam
done
