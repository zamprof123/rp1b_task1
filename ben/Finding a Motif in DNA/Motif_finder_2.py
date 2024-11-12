#!/usr/bin/env python
# coding: utf-8

# In[6]:


dna_seqs = "TGTTTTAGTTTTTAGTTCAACTTTTAGTCGTCTTTTAGTTTTTAGTATTTTTAGTGGTTTTAGTGTTTTAGTATTTTAGTGTTTTTAGTGTTTTTAGTACTTTTAGTCAGCTTTTAGTTTTTAGTGTAGTCTTTTAGTTTTTAGTGACGCTTTTAGTCTTGCGAGGTTTTAGTTGCATTTTAGTTTTTAGTTGTTTTTTAGTTTTTAGTCACAATTTTAGTCATCCTGGTTTTAGTGGTTTTAGTCTTTTAGTCTATTTTAGTTTTTTTAGTGTGTTTTAGTTCTCATTTTTAGTCCTGAATTTTAGTGGTTTTAGTGTTTTAGTCAGTTTTAGTTTGTTATGTTTTAGTATACTTTTAGTCCTTTTAGTGCGGTTTTAGTTTTTAGTTTTTTAGTTTTTAGTGATTTTTAGTCTCAATTTTAGTTCACGTTTTAGTATTTTAGTGTCAGATGGTTTTAGTTTTTAGTTGTTTTAGTGCTATCCTTTTAGTCAATTTTAGTTTTTAGTCTTTTAGTTAACACTTTTAGTTTTTAGTTTTTAGTGTTTTTTAGTTTTTAGTAGTTTTAGTACCCCTTTTAGTTAAGTTTTAGTTTTTAGTGGCTTTTAGTGTTTTAGTGCACTTTTAGTGACTTTTAGTTTTTAGTTTTTAGTCAAACATTTTTAGTTAGCATTCGTTTTAGTTGGTCACATTTTAGTTATTTTAGTATTTTAGTTTTTAGTATTTTAGTGTTTTAGTAGATGAGGCGTTTTAGTTACCCATTTTAGTTTTTAGTTTTTAGTTTCCAGTTTTAGTTTTTTAGTTCATTTTAGTCTTTTAGTATTTTAGTATTTTTAGTGTTCCTCCTATTTTAGTTATCGACTTTTAGTGTATTTTTAGTAGAATTTTAGTTTTTTAGTCAAGTTTTTAGTTTTTAGTTTTTAGTATTTTAGTTTTTAGTACATTTTAGTCTTTTAGTGTTTTAGTTTTTAGT"
#assigns a sequence that you wish to find substrings within to the variable dna_seqs
substring = "TTTTAGTTT"
#use this to assign the motif you wish to locate within the dna sequence to the variable substring
subs_len = len(substring)
#counts the number of nucleotides in the motif you are searching for for use in the function motif_locator

def motif_locator(dna_seqs):
    count = 0 #creates a variable 'count' that will be used to move through the DNA sequence input
    temp_motif = "" #a temporary string that will be used an explained later
    motif_locs = [] #creates an empty list that will be populated by position of the first nucleotide in the substring each time the substring appears in dna_seq
    for motif in dna_seqs:
        temp_motif = dna_seqs[count:count+subs_len] #a temporary string of the same length as the query substring that will move one nucleotide downstream each time the program iterates through the for loop
        count += 1 #adds one to the count variable so the next time the program iterates through the for loop, the motif being queried is moved one nucleotide downstream in the DNA sequence
        if temp_motif == substring: 
            motif_locs.append(count) #if the motif being tested in this iteration of the for loop is equal to the query entered by the user, assigned to the variable 'substring' the the list 'motif_locs' will be appended with the position of the first nucleotide in the query substring.
            
    return motif_locs

print(motif_locator(dna_seqs)) #prints the return of the function motif_locator, which is the list the contains the position of the first nucleotide of the substring each time it appears in the string dna_seq


# In[ ]:




