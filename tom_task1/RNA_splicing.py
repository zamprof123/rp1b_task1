import os #read file from desktop

with open(os.path.expanduser('~/Desktop/rosalind_splc.txt')) as f:
    content = f.read().replace('\n', '').split('>')

seq = content[1][13:] #define sequence
introns = [x[13:] for x in content[2:]] #create list of introns

for intron in introns: #remove introns from sequence
    seq = seq.replace(intron, '')
    

codons = {'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V', 'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V', 'TTA': 'L',
          'CTA': 'L', 'ATA': 'I', 'GTA': 'V', 'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V', 'TCT': 'S', 'CCT': 'P',
          'ACT': 'T', 'GCT': 'A', 'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 'TCA': 'S', 'CCA': 'P', 'ACA': 'T',
          'GCA': 'A', 'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
          'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'TAA': '', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'TAG': '',
          'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G', 'TGC': 'C', 'CGC': 'R',
          'AGC': 'S', 'GGC': 'G', 'TGA': '', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'TGG': 'W', 'CGG': 'R', 'AGG': 'R',
          'GGG': 'G'}


protein = ''.join(codons.get(seq[n:n + 3], '') for n in range(0, len(seq), 3)) #translate nucleotide sequence

print(protein)
