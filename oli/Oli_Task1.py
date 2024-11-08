

"""REVP: Locating Restriction Sites"""
#below section will take a fasta file with a sequence and will append a list with the lines containing the sequence#
list_seq=[]
with open("Downloads/rosalind_revp.txt") as seq_file:
    for line in seq_file:
        if line[0] == ">":
            continue
        else:
            list_seq.append(line.strip("\n"))
seq=''.join(list_seq)

#compl_code will allow to convert the given sequence into its complement#
Compl_Code = {"A": "T", "C": "G", "G": "C", "T": "A"}

#first loop will select a palindrome length (called pal_length, and defines the search window size) 
#and will be used by the next loop to define at what position in the sequence the search must stop and thus the range of the loop
#reverse strand (rev_strand, selected by indexing (with end point defined by current possition + window size)) is then produced via a list comprehension using compl_code dictionary and via a negative index to reverse it
for pal_len in range (4,13):
    for position in range((len(seq)-(pal_len-1))):
        rev_seq=''.join([Compl_Code[nuc] for nuc in seq[position:(position+pal_len)]][::-1])
        #if statement is then used to see if the first index position to the end index (defined by the window) 
        #is palindromic to its reversed sequence (rev_strand), and thus the position and palindrome length are printed
        if seq[position:(position+pal_len)]== rev_seq:
            print((position+1), pal_len)

"""GRPH: Overlap Graphs"""
#section below will make a dictionary of the sequences called seq_dict
seq_dict={}
with open("Downloads/rosalind_grph.txt") as fasta_file:
    for line in fasta_file:
        if line[0]==">":
            seq_index= line.strip(">").strip("\n")
            seq_dict[seq_index]=""
        elif line[0] !=">":
            seq_dict[seq_index]+=line.strip("\n")
#each sequence (here defined as the Fasta ID, will be looped through, with each sequence being compared to
#the rest of the sequences
for sequence in seq_dict:
    for sequence2 in seq_dict:
        #to ensure a sequence is not compared to itself, a If statement with a continue response is used
        #the keys of the dictionary is used to select the sequence
        if seq_dict[sequence] == seq_dict[sequence2]: 
            continue
        elif seq_dict[sequence][-3:] == seq_dict[sequence2][0:3]:
            print(sequence,sequence2)
#finally an elif statement is used to see if the 3 nucleotides at the end of a sequence are identical to
#the 3 nucleotides at the beginning of the other sequece compared (sequence2) (done via indexing e.i. [0:3] and [-3:])
            

"""CONS: Consensus and Profile"""
#below code maks  dictionary of the sequences and then extracts the sequences alone into a list
seq_dict = {}
with open("Downloads/rosalind_cons.txt") as seq_file:
    for line in seq_file:
        if line[0] == ">":
            seq_index = line.strip("\n")
            seq_dict[seq_index] = ""
        elif line[0] != ">":
            seq_dict[seq_index] += line.strip("\n")
seq_data = list(seq_dict.values())
#first lists of the length of the first sequence are made (all sequences are equal length), corresponding to the positions in the sequences
A_frequency = [0]*len(seq_data[0])
T_frequency = [0]*len(seq_data[0])
C_frequency = [0]*len(seq_data[0])
G_frequency = [0]*len(seq_data[0])
# Then the sequnces are looped through
#adding 1 to the nucleotide frequency lists at the correct position (with n denoting the nucleotide position) via If statements
for sequence in seq_data:
    for n in range(len(sequence)):
        if sequence[n] == "A":
            A_frequency[n] += 1
        elif sequence[n] == "T":
            T_frequency[n] += 1
        elif sequence[n] == "C":
            C_frequency[n] += 1
        elif sequence[n] == "G":
            G_frequency[n] += 1
# the above section has now made lists of each nucleotides frequency at each position
#now the above lists are used to make a consensus sequence via finding the largest value at a certain position across the lists
# this is done using a  for loop to move along the sequence (with p denoting the position (index) across the lists)
#and if the if statement is true, the nucleotide type (A,G,C,T) is inserted into the string
consensus_sequence = ""
for p in range(len(seq_data[0])):
    if max(G_frequency[p], C_frequency[p], T_frequency[p], A_frequency[p]) == A_frequency[p]:
        consensus_sequence += "A"
    elif max(G_frequency[p], C_frequency[p], T_frequency[p], A_frequency[p]) == C_frequency[p]:
        consensus_sequence += "C"
    elif max(G_frequency[p], C_frequency[p], T_frequency[p], A_frequency[p]) == T_frequency[p]:
        consensus_sequence += "T"
    elif max(G_frequency[p], C_frequency[p], T_frequency[p], A_frequency[p]) == G_frequency[p]:
        consensus_sequence += "G"
#finally the lists are inserted into a dictionary for better presentation and are printed without brackets and commas and with the consensus sequence
Base_frequency = {"A": {}, "C": {}, "T": {}, "G": {}}
Base_frequency["A"] = A_frequency
Base_frequency["C"] = C_frequency
Base_frequency["T"] = T_frequency
Base_frequency["G"] = G_frequency
print(consensus_sequence)
for key in Base_frequency:
    print(
        key+":", str(Base_frequency[key]).replace("[", "").replace(",", "").replace("]", ""))

"""GC: Computing GC Content"""
# below section will tun a fasta file into a dictionary, with the ID and sequence paired
fasta_dict = {}
with open("Downloads/rosalind_GC.txt") as seq_file:
    for line in seq_file:
        if line[0] == ">":
            seq_index = line.strip(">").strip("\n")
            fasta_dict[seq_index] = ""
        elif line[0] != ">":
            fasta_dict[seq_index] += line.strip("\n")
#the IDs (keys) are looped through, and used to count the C and G via the count() function, with GC converted into percentages
#With the ID inserted into a GC dictionry (GC_Dict) with the calculaed GC%
GC_dict = {}
for id in fasta_dict:
    GC_dict[id] = ((fasta_dict[id].count("C")+fasta_dict[id].count("G"))/len(fasta_dict[id]))*100
#The sequenc ID with the largest GC% is printed with the GC% (seperated on differnet lines via sep=\n)
print(max(GC_dict,key=GC_dict.get), max(GC_dict.values()), sep="\n")


