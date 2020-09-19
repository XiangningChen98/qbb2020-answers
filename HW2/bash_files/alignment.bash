cd ~/qbb2020-answers/HW2/sequencing_data/
for sample in 09 11 23 24 27 31 35 39 62 63
do
	bwa mem -R "@RG\tID:${sample}\tSM:${sample}" -t 4 ~/qbb2020-answers/HW2/reference/sacCer3.fa ~/qbb2020-answers/HW2/sequencing_data/A01_${sample}.fastq > ~/qbb2020-answers/HW2/alignment/A01_${sample}.sam
	
done
