#HW6


## Getting data

The sample that data came from:

	STEM-seq_E4.0ICM_rep1
	- SRR3083926_1.chr6.fastq
	- SRR3083926_2.chr6.fastq

	STEM-seq_E5.5Epi_rep1
	- SRR3083929_1.chr6.fastq
	- SRR3083929_2.chr6.fastq
	

####Check the fastq files:
	less -S SRR3083926_1.chr6.fastq
	less -S SRR3083926_2.chr6.fastq
	less -S SRR3083929_1.chr6.fastq
	less -S SRR3083929_2.chr6.fastq

- They all look good.


####Run fastqc on one sample(SRR3083926_1.chr6.fastq):
	fastqc SRR3083926_1.chr6.fastq

- From teh fastqc result, we could see that the sequence length is 101, and there are 133075 sequences in all.
- The quality scores long the sequences are above 28, so the quality is fine.
- The outstanding thing is that C percentage in reads is really low, even near zero, and T percentage is really high. This is because C was converted to T in bisulfite‐convertion


##Bisulfite mapping with Bismark
####Get a reference genome and index it
	bismark_genome_preparation /Users/xiangning/qbb2020-answers/HW6/reference

####Map two experiments to the genome
	bismark /Users/xiangning/qbb2020-answers/HW6/reference -1 SRR3083926_1.chr6.fastq,SRR3083929_1.chr6.fastq -2 SRR3083926_2.chr6.fastq,SRR3083929_2.chr6.fastq
####Visualization in igv
sort the bam files:
	samtools sort -o SRR3083926_bismark.sorted.bam SRR3083926_1.chr6_bismark_bt2_pe.bam
	samtools sort -o SRR3083929_bismark.sorted.bam SRR3083929_1.chr6_bismark_bt2_pe.bam
index the bam files:
	samtools index SRR3083926_bismark.sorted.bam
	samtools index SRR3083929_bismark.sorted.bam
####extract methylation data
	bismark_methylation_extractor --comprehensive --bedGraph SRR3083926_1.chr6_bismark_bt2_pe.bam
	bismark_methylation_extractor --comprehensive --bedGraph SRR3083929_1.chr6_bismark_bt2_pe.bam
	
	



       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       ~~~   X   for methylated C in CHG context                      ~~~
       ~~~   x   for not methylated C CHG                             ~~~
       ~~~   H   for methylated C in CHH context                      ~~~
       ~~~   h   for not methylated C in CHH context                  ~~~
       ~~~   Z   for methylated C in CpG context                      ~~~
       ~~~   z   for not methylated C in CpG context                  ~~~
       ~~~   U   for methylated C in Unknown context (CN or CHN       ~~~
       ~~~   u   for not methylated C in Unknown context (CN or CHN)  ~~~
       ~~~   .   for any bases not involving cytosines                ~~~
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             OT      original top strand
             CTOT    complementary to original top strand
             OB      original bottom strand
             CTOB    complementary to original bottom strand
	
	
	
