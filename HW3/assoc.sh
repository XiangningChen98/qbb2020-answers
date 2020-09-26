plink \
  --vcf BYxRM_segs_saccer3.bam.simplified.vcf\
  --pheno BYxRM_PhenoData_encode.txt \
  --assoc \
  --allow-no-sex \
  --allow-extra-chr\
  --all-pheno\
  --covar plink.eigenvec \
  --covar-number 1-10
