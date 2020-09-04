#!/urs/bin/env python3
import fasta_iterator_class
import sys

# get the input 
target_file = sys.argv[1]
query_file = sys.argv[2]
k = int(sys.argv[3])

def main():
    # read the target file
    target_Reader = fasta_iterator_class.FASTAReader(open("subset.fa"))
    target_dict={}
    kmers_target={}
    for seqid_target, seq_target in target_Reader:
        target_dict[seqid_target]=seq_target
        kmer_list=[]
        for i in range(0,len(seq_target)-k+1):
    #     for i in range(0,1000-k+1):    
            kmer_target = seq_target[i:(i+k)].upper()
            kmers_target.setdefault(kmer_target,[])
    #         kmer_list.append([i,''.join(kmer)])
            kmers_target[kmer_target].append((i,''.join(seqid_target)))
    #import query file
    outputrows=[]
    query_Reader = fasta_iterator_class.FASTAReader(open("droYak2_seq.fa"))
    for seqid_query, seq_query in query_Reader :
        for i in range(0,len(seq_query)-k+1):
            if i%1000==0:
                print('finish',i/1000)
    #     for i in range(0,1000-k+1):        
            kmer_query = seq_query[i:(i+k)].upper()
            if kmer_query in list(kmers_target.keys()):
                for seqid in kmers_target[kmer_query]:
                    outputrow=[seqid[1],seqid[0],i,kmer_query]
                    outputrows.append(outputrow)

    with open('extend_kmer_match_result.txt', 'w') as f:
        for i in range(1000):
            print("{} {} {} {}".format(outputrows[i][0],outputrows[i][1],outputrows[i][2],outputrows[i][3]), file = f)



        

    
if __name__ == "__main__":
    main()    
        
    
