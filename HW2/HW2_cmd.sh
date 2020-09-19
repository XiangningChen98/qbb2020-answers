step 1
(lab-week2) [~/qbb2020-answers/HW2/reference $]bwa index sacCer3.fa

step 2
(lab-week2) [~/qbb2020-answers/HW2/alignment $]bash alignment.bash 


step 3
(lab-week2) [~/qbb2020-answers/HW2/alignment $]bash sort.bash


step 4
(lab-week2) [~/qbb2020-answers/HW2/variant_calling $]freebayes -f ~/qbb2020-answers/HW2/reference/sacCer3.fa -p 1 --genotype-qualities ~/qbb2020-answers/HW2/alignment/A01_*.sorted.bam > var_A01_all.vcf

step 5
(lab-week2) [~/qbb2020-answers/HW2/variant_calling $]vcffilter -f "QUAL > 20" var_A01_all.vcf > var_A01_all.filtered.vcf

step 6
(lab-week2) [~/qbb2020-answers/HW2/variant_calling $]vcfallelicprimitives var_A01_all.filtered.vcf -k -g > var_A01_all.prim.vcf

step 7

(lab-week2) [~/qbb2020-answers/HW2/variant_calling $]snpEff ann R64-1-1.86 var_A01_all.prim.vcf > var_A01_all.ann.vcf

