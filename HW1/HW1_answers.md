### Q 1a. 
(week1_env) [~/qbb2020-answers/HW1/asm $]samtools faidx ref.fa 
The reference genome is 233806 bp.

### Q 1b.
(week1_env) [~/qbb2020-answers/HW1/asm $]fastqc frag180.1.fq 
(week1_env) [~/qbb2020-answers/HW1/asm $]fastqc frag180.2.fq 
(week1_env) [~/qbb2020-answers/HW1/asm $]fastqc jump2k.1.fq 
(week1_env) [~/qbb2020-answers/HW1/asm $]fastqc jump2k.2.fq 

frag180.1.fq: 35178 reads and 100 bp per read
frag180.2.fq: 35178 reads and 100 bp per read
jump2k.1.fq: 70355 reads and 50 bp per read
jump2k.2.fq: 70355 reads and 50 bp per read

### Q 1c.
coverage = [2*(35178 * 100) + 2*(70355 *50)] / 233806 ~= 60
so the coverage is around 60

### Q 1d.
See figures on Github
 

### Q 2a.
(week1_env) [~/qbb2020-answers/HW1/asm $]jellyfish count -m 21 -C -s 1000000 *.fq 
(week1_env) [~/qbb2020-answers/HW1/asm $]jellyfish histo mer_counts.jf > reads.histo

From the reads.histo file we could see that 1091 kmers occur exactly 50 times

### Q 2b.
(week1_env) [~/qbb2020-answers/HW1/asm $]jellyfish dump mer_counts.jf -c -t|sort -k 2 -n -r |head > dump.kmers.fa
(week1_env) [~/qbb2020-answers/HW1/asm $]less -S dump.kmers.fa 

GCCCACTAATTAGTGGGCGCC   105
CGCCCACTAATTAGTGGGCGC   104
CCCACTAATTAGTGGGCGCCG   104
ACGGCGCCCACTAATTAGTGG   101
CAGGCCAGCTTATAAGCTGGC   98
AACAGGCCAGCTTATAAGCTG   98
ACAGGCCAGCTTATAAGCTGG   97
AGGCCAGCTTATAAGCTGGCC   95
AGCATCGCCCACATGTGGGCG   83
GCATCGCCCACATGTGGGCGA   82

### Q 2c.
As in the result, the estimated length of genome is 233,468 bp bp to 233,805bp


### Q 2d.
The real length of the genome is 233,806 bp, just 1 bp longer the the maximum of the estimated genome length from Genome Scope, which indicated that Genome Scope could give the result that really close to the real length, but a little bit underestimated the length. 


### Q 3a.
(week1_env) [~/qbb2020-answers/HW1/asm $]spades.py --pe1-1 frag180.1.fq --pe1-2 frag180.2.fq --mp1-1 jump2k.1.fq --mp1-2 jump2k.2.fq -o spade_output -t 4 -k 31

(week1_env) [~/qbb2020-answers/HW1/asm/spade_output $]grep -c '>' contigs.fasta
It ended up to 4 contigs

### Q 3b.
(week1_env) [~/qbb2020-answers/HW1/asm/spade_output $]samtools faidx contigs.fasta
By summing up the length of each contigs, the whole length is 87284bp.

### Q 3c.
(week1_env) [~/qbb2020-answers/HW1/asm/spade_output $]sort contigs.fasta.fai -k2 -n -r
NODE_1_length_105831_cov_20.671371	105831	36	60	61
NODE_2_length_47861_cov_20.231319	47861	107666	60	61
NODE_3_length_41352_cov_20.588756	41352	156360	60	61
NODE_4_length_39423_cov_20.384723	39423	198437	60	61

So the largest contig is 105831bp

### Q 3d.
It is 47861bp

### Q 4a.
(week1_env) [~/qbb2020-answers/HW1/asm/spade_output $]dnadiff ~/qbb2020-answers/HW1/asm/ref.fa contigs.fasta
The report is as follows:
                               [REF]                [QRY]
[Sequences]
TotalSeqs                          1                    4
AlignedSeqs               1(100.00%)           4(100.00%)
UnalignedSeqs               0(0.00%)             0(0.00%)

[Bases]
TotalBases                    233806               234467
AlignedBases          233755(99.98%)       233755(99.70%)
UnalignedBases             51(0.02%)           712(0.30%)

[Alignments]
1-to-1                             5                    5
TotalLength                   233755               233755
AvgLength                   46751.00             46751.00
AvgIdentity                   100.00               100.00

M-to-M                             5                    5
TotalLength                   233755               233755
AvgLength                   46751.00             46751.00
AvgIdentity                   100.00               100.00

[Feature Estimates]
Breakpoints                       10                    2
Relocations                        0                    0
Translocations                     3                    0
Inversions                         0                    0

Insertions                         5                    1
InsertionSum                      51                  712
InsertionAvg                   10.20               712.00

TandemIns                          0                    0
TandemInsSum                       0                    0
TandemInsAvg                    0.00                 0.00

[SNPs]
TotalSNPs                          1                    1
AC                          0(0.00%)             0(0.00%)
AT                          0(0.00%)             0(0.00%)
AG                          0(0.00%)             0(0.00%)
CA                          0(0.00%)             0(0.00%)
CT                        1(100.00%)             0(0.00%)
CG                          0(0.00%)             0(0.00%)
TG                          0(0.00%)             0(0.00%)
TC                          0(0.00%)           1(100.00%)
TA                          0(0.00%)             0(0.00%)
GC                          0(0.00%)             0(0.00%)
GA                          0(0.00%)             0(0.00%)
GT                          0(0.00%)             0(0.00%)

TotalGSNPs                         1                    1
GC                          0(0.00%)             0(0.00%)
GA                          0(0.00%)             0(0.00%)
GT                          0(0.00%)             0(0.00%)
CG                          0(0.00%)             0(0.00%)
CT                        1(100.00%)             0(0.00%)
CA                          0(0.00%)             0(0.00%)
AG                          0(0.00%)             0(0.00%)
AT                          0(0.00%)             0(0.00%)
AC                          0(0.00%)             0(0.00%)
TC                          0(0.00%)           1(100.00%)
TA                          0(0.00%)             0(0.00%)
TG                          0(0.00%)             0(0.00%)

TotalIndels                        0                    0
A.                          0(0.00%)             0(0.00%)
C.                          0(0.00%)             0(0.00%)
T.                          0(0.00%)             0(0.00%)
G.                          0(0.00%)             0(0.00%)
.T                          0(0.00%)             0(0.00%)
.A                          0(0.00%)             0(0.00%)
.C                          0(0.00%)             0(0.00%)
.G                          0(0.00%)             0(0.00%)

TotalGIndels                       0                    0
G.                          0(0.00%)             0(0.00%)
C.                          0(0.00%)             0(0.00%)
A.                          0(0.00%)             0(0.00%)
T.                          0(0.00%)             0(0.00%)
.T                          0(0.00%)             0(0.00%)
.A                          0(0.00%)             0(0.00%)
.C                          0(0.00%)             0(0.00%)
.G                          0(0.00%)             0(0.00%)

The average identify is 100 of assembly compared to 100 of reference.



### Q 4b.
(week1_env) [~/qbb2020-answers/HW1/asm/alignment $]show-coords out.delta
/Users/xiangning/qbb2020-answers/HW1/asm/ref.fa /Users/xiangning/qbb2020-answers/HW1/asm/spade_output/contigs.fasta
NUCMER

    [S1]     [E1]  |     [S2]     [E2]  |  [LEN 1]  [LEN 2]  |  [% IDY]  | [TAGS]
=====================================================================================
  127965   233795  |   105831        1  |   105831   105831  |    99.99  | Halomonas	NODE_1_length_105831_cov_20.671371
   40651    88511  |    47861        1  |    47861    47861  |   100.00  | Halomonas	NODE_2_length_47861_cov_20.231319
       3    26789  |    41352    14566  |    26787    26787  |   100.00  | Halomonas	NODE_3_length_41352_cov_20.588756
   26790    40642  |    13853        1  |    13853    13853  |   100.00  | Halomonas	NODE_3_length_41352_cov_20.588756
   88532   127954  |    39423        1  |    39423    39423  |   100.00  | Halomonas	NODE_4_length_39423_cov_20.384723



So the longest alignment is 105831bp long.

### Q 4c.

From the previous report we can know that there are 1 insertion and 5 deletions.

### Q 5a.
There is an easier way to check the insertion position by checking out.qdiff and out.rdiff file.
(week1_env) [~/qbb2020-answers/HW1/asm/diff $]cat out.qdiff
(week1_env) [~/qbb2020-answers/HW1/asm/diff $]cat out.rdiff

26790	26789

### Q 5b.
13854	14565 on NODE_3_length_41352_cov_20.588756:13854-14565
712

### Q 5c.
(week1_env) [~/qbb2020-answers/HW1/asm/decoding $]samtools faidx /Users/xiangning/qbb2020-answers/HW1/asm/spade_output/contigs.fasta NODE_3_length_41352_cov_20.588756:13854-14565 -i > decoding.fasta
>NODE_3_length_41352_cov_20.588756:13854-14565/rc
AGCCCCTTAGTCTTTTCTGAGTGACTTAAGGGAGTGCATACTGAAACGAGGTATAACGTT
CGCGCGTAGTAACTTACCCTCTTTCGAAAGTCTAAGCGGCTTGTATTCTGGCCGGGACGG
CCGACCCACGGTCGACCGGAGGGTCAGACAACCTTGATCCCGTCTACAAGTCCGCTAAGC
CAACACGTACGACAGGAACACCGTCATAACTGACCAAATAAACACTAACATGAGCCTTAG
AGACATCAATACACGCCCGAACCCATCACACACATACCAAAGAATATAATAAGAAAAGAG
CGCGACTCCAAACTTACAGTAGGCTGAAATTCACCTATGTCAGGAGGTAAGTACGACACG
CCGACACAACGACACACGCAGCTTATTCATATCTGACTATAGTTAAAACCGAACCACTTC
TGTGCGTATGTAACTACCACATGCTGCCATTATGTGCGGAGGTTAGGCGCGGCGTAGAAG
AGTCGTTCATTACTTGCCTACACAAGTCATTAATGCTGGGCGGTACGAACGCACAAAGTA
TGCCAGGCTAAGCGGGATACCTTTATCACTTCTGAACTGCAGCGAAGAAAACATTACTTG
AGGTACGAATTCATAGCTTCATAGATTATGGACCGCACCCCGTCACCGCTGCGTACCTTC
TAAGCTGAATATCTGCGTGAATTGCATTAAGCTTTCCCGATGTAAATCGTTA

### 5d.

(week1_env) [~/qbb2020-answers/HW1/asm/decoding $]python ported_decoder.py -d --input decoding.fasta 

The decoded message :  Congratulations to the 2020 CMDB @ JHU class!  Keep on looking for little green aliens...





