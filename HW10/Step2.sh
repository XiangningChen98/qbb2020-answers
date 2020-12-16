cd /Users/xiangning/qbb2020-answers/HW10/week13_data/

bwa index assembly.fasta

cd /Users/xiangning/qbb2020-answers/HW10/week13_data/READS/

for sample in SRR492183 SRR492186 SRR492188 SRR492189 SRR492190 SRR492193 SRR492194 SRR492197
do
	bwa mem -R "@RG\tID:${sample}\tSM:${sample}" -t 4 /Users/xiangning/qbb2020-answers/HW10/week13_data/assembly.fasta ${sample}_1.fastq ${sample}_2.fastq > /Users/xiangning/qbb2020-answers/HW10/week13_data/BAM/${sample}.sam
	
done