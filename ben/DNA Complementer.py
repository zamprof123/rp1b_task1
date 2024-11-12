#!/usr/bin/env python
# coding: utf-8

# In[3]:


def dna_complementer(dna_seq):
    complementary_strand = list(dna_seq) #takes the query sequence, which was inputed as a string, and converts it into a list
    strand_length = len(complementary_strand) #counts the number of nucleotides in the query sequence and assigns it to the variable strand_length
    
    for n in range(strand_length):
        if complementary_strand[n] == "A":
            complementary_strand[n] = "T"
        elif complementary_strand[n] == "T":
            complementary_strand[n] = "A"
        elif complementary_strand[n] == "G":
            complementary_strand[n] = "C"
        elif complementary_strand[n] == "C":
            complementary_strand[n] = "G"
    #this for loop iterates through the entire DNA sequence and replaces each nucleotide in the list with its complementary partner
            
    reversed_strand =complementary_strand[::-1] #inverts the above list created so that it is complementary to the strand entered by the user
    return reversed_strand




query_seq = "ATCGGTAAATTCGATCGATCAGCATG" #user can input their query sequence here


print("".join(dna_complementer(query_seq)))
#joins each nucleotide in the list so it can be outputted as a string and prints it


# In[ ]:




