import sys

seqtype=sys.argv[3]

with open(sys.argv[2], 'wt') as outfile:
    outfile.write("##gff-version 3\n")
    with open(sys.argv[1], 'rt') as matches:
        previous=""
        count=1
        start_prev=0
        end_prev=0
        for line in matches:
            seqid=line.split('\t')[1]
            seqid_mod=seqid.replace('.', '_')
            start=int(line.split('\t')[8])
            end=int(line.split('\t')[9])
            viralseq=line.split('\t')[0]
            percentage=line.split('\t')[2]
            length=int(line.split('\t')[3])
            direction=int(start)-int(end)
            #only keep sequences where the viral trimmed contig comes from the contig
            #print(viralseq)
            #print(seqid_mod)
            #print(previous)
            #break
            if (seqid_mod in viralseq):
                #print("here")
                #break
                #make sure it is an exact match
                if (percentage=='100.000'):
                    #print("passed homology cutoff")
                    #print(seqid_mod)
                    #print("here")
                    #break
                    #only keep viral contigs mapping in the correct direction (direction < 0)- most were included within the correct direction
                    if (direction<0):
                        strand="+"
                        #print("if")
                    else:
                        start_temp=end
                        end=start
                        start=start_temp
                        strand="-"
                        #print("else")
                    #print(viralseq)
                    #print(previous)
                    #break
                    if (viralseq!=previous):
                        #print("here")
                        #break
                        outfile.write("%s\tViral_Contigs\t%s\t%s\t%s\t.\t%s\t.\tID=%s\n" % (seqid, seqtype, start, end, strand, viralseq))
                        previous=viralseq
