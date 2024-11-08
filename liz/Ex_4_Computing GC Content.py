#4
import screed # module screed parses FASTA and FASTQ files

def read_fasta(path):
    sequences = []
    with screed.open(path) as seqfile:
        for read in seqfile:
            sequences.append((read.name,read.sequence))
    return sequences    

fasta = read_fasta("rosalind_gc.txt")

def cal_gc(seq):
    g = seq.count("G")
    c = seq.count("C")
    gc_total = g + c
    gc = gc_total / len(seq) * 100
    return gc

def cal_highest_gc(seqs):
    highest_gc = 0
    highest_gc_name = ""
    for name, sequence in seqs:
        gc = cal_gc(sequence)
        if gc > highest_gc:
            highest_gc_name = name
            highest_gc = gc
    return highest_gc_name, round(highest_gc, 6)

for output in cal_highest_gc(fasta):
    print(output)
            