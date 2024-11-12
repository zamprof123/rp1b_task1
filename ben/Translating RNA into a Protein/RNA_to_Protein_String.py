#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os # imports the os library
rna_codon_dict = {} #creates an empty dictionary that will later be populated by RNA codon table 
os.chdir("/home/jovyan") #changes to the appropriate working directory to access the .txt file containing the RNA codon table
with open("ben/RNA_codon_table.txt") as table:
    for line in table:
        row = line.strip()
        row = row.split("    ")
        #the above to lines strip the RNA codon table of any /Ns and remove all the whitespace so that it can be transferred into a dicitonary in this program
        for i in range(0, len(row), 2):
            rna_codon_dict[row[i]] = row[i + 1]
        #this for loop iterates through the cleaned up RNA codon table and creates a dictionary where the keys are the each possible RNA codon and the values are the corresponding single letter amino acid abbreviations, or if the case may be a stop.
with open("ben/RNA_string.txt") as f:
    rna_seq = f.read() #opens the users query rna sequence and assigns it to the variable rna_seq

def rna_to_prot(rna_seq_par, diction):
    count = 0 #creates an integer variable which will be used to iterate through the users RNA sequence
    temp_codon = "" #creates a string that will be temporarily filled by each codon as a for loop iterates through the users query RNA sequence
    protein_seq = [] #creates an empty list that will later be populated by the final protein sequence
    for codon in rna_seq_par:
        temp_codon = rna_seq_par[count:count+3]
        count += 3
        AA = diction[temp_codon]
        # this for loop iterates through the users query protein one codon at a time by increaseing the variable count by
        # 3 for each iteration of the loop. The string 'temp_codon' is assigned the value of the current codon that the for
        # loop has iterated through, and then the variable AA is assigned the single letter code by calling the value of the
        # codon from the dictionary using the temp_codon string
        if diction[temp_codon] == "Stop":
            break
        else:
            protein_seq.append(AA)
        #if the temporary codon is a stop codon, this if statement will break the for loop and the protein sequence will be returned by the function
        # otherwise, the protein sequence list is appended with the single letter amino acid code currently help by the variable AA
        # the for loop will then iterate until it comes across a stop codon
    return protein_seq

protein_sequence = rna_to_prot(rna_seq, rna_codon_dict) 
#assigns the list returned by the rna_to_prot function to the variable protein_sequence
print("".join(protein_sequence)) #joins the list into a string and prints it        


# In[ ]:




