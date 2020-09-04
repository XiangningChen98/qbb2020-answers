#!/urs/bin/env python3
import fasta_iterator_class
import sys

# get the input 
target_file = sys.argv[1]
query_file = sys.argv[2]
k = int(sys.argv[3])


def main():
    # read the target file
    target_Reader = fasta_iterator_class.FASTAReader(open(target_file))
    target_dict={}
    kmers_target={}
    kmers_query={}
    match_dict={}
    for seqid_target, seq_target in target_Reader:
        target_dict[seqid_target]=seq_target
        kmer_list=[]
        for i in range(0,len(seq_target)-k+1):
#         for i in range(0,5000-k+1):    
            kmer_target = seq_target[i:(i+k)].upper()
            kmers_target.setdefault(kmer_target,[])
    #         kmer_list.append([i,''.join(kmer)])
            kmers_target[kmer_target].append((i,''.join(seqid_target)))
    #import query file
    outputrows=[]
    query_Reader = fasta_iterator_class.FASTAReader(open(query_file))
    for seqid_query, seq_query in query_Reader :
        match_seqs_all=[]
        for i in range(0,len(seq_query)-k+1):
        
#         for i in range(0,5000-k+1):   
            kmer_query = seq_query[i:(i+k)].upper()
            if kmer_query in list(kmers_target.keys()):
                match_seqs=[]
                for seqid in kmers_target[kmer_query]:
                    whole_seq=kmer_query
                    target_seq=target_dict[seqid[1]]
                    target_start=seqid[0]
                    query_seq=seq_query
                    query_start=i
                    l_match = 1
                    r_match = 1
                    nl=0
                    nr=0
                    while l_match ==1:
                        if (target_start-nl-1>=0) and (target_seq[target_start-nl-1].upper() == query_seq[query_start-nl-1].upper()):
                            whole_seq = target_seq[target_start-nl-1]+whole_seq
                            nl+=1
                            l_match =1
                        else:
                            nl+=1
                            l_match = 0
                    while r_match ==1:
                        if (target_start+k+nr<len(target_seq)) and (query_start+k+nr<len(query_seq)):
                            if (target_seq[target_start+k+nr].upper() == query_seq[query_start+k+nr].upper()):
                                whole_seq = whole_seq + target_seq[target_start+k+nr]
                                nr+=1
                                r_match =1
                            else:
                                nr+=1
                                r_match = 0
                        else:
                            nr+=1
                            r_match = 0
                            
                    match_dict.setdefault(seqid[1],[])
                    match_dict[seqid[1]].append(whole_seq)


    for keys,v in list(match_dict.items()):
        v.sort(key=lambda s: len(s))
        v.reverse()
        print(keys)
        for item in v:
            print(len(item),': ',item)



                
                 

    
if __name__ == "__main__":
    main()    
        
    
