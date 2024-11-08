
# Complementary strand fucntion
# This is called in my restriction site function so the code is here so it works
def complementary_strand_unreversed(dna_sequence):
    complementary_sequence = []
    uppercase_sequence = dna_sequence.upper()

    for base in uppercase_sequence:
        if base == "G":
            complementary_sequence.append("C")
        elif base == "C":
            complementary_sequence.append("G")
        elif base == "A":
            complementary_sequence.append("T")
        elif base == "T":
            complementary_sequence.append("A")
        else:
            continue

    complementary_sequence = ''.join(complementary_sequence)
    return complementary_sequence




# Restrcition site finder function
def restriction_site_finder(fasta_file):
    """ Finds all the restriction site within a DNA sequence. Input: DNA sequences in a fasta file format.
    Output: list of the positions of each restriction site and their length"""
    # Fasta file dictionary
    gene_dictionary = {}
    for line in fasta_file:
        if '>' in line:
            f_key = line.strip("\n")
            gene_dictionary[f_key] = ""
        else:
            gene_dictionary[f_key] += line.strip("\n")  # has to be += to add each line to the last.
        # E.G >Rosalind_4632 : TGCTAGCTGATCGTATC


# Restriction site finder
    for gene in gene_dictionary: # gene = the key
        sequence = gene_dictionary[gene] # setting seq as the value
        comp_sequence = complementary_strand_unreversed(sequence) # calling the complementary strand function


        restriction_site_length = 4  # miminum size of a restriction site is 4 bps

        while restriction_site_length <= 12:   # max size of restriction site is 12 bps
            for a in range(0, len(sequence)): # iterating over from 1 to the end of seqeunce
                site = sequence[a:a + restriction_site_length] # calling the bases the length of the restriction site

                rev_site = ''.join(reversed(list(comp_sequence[a:a + restriction_site_length])))  # reversed complementary sequence of those positions
                # reverse function only works on list. so make str a list, reverse it, then join & remove all blank
                # spaces btw letters
                if len(site) < restriction_site_length:  # dont want sites of 3 bps or less
                    break
                elif site == rev_site:  # see if its a palindrome to complement seq
                    print(a + 1, len(site))  # if sequence is palindrome give position and length. Sorted by length
                    # of restriction site e..g all sites 4 bps long first, the 6,8,10,12.
                else:
                    continue
            restriction_site_length += 1



# Executing function
import os
with open(os.path.expanduser(r'C:\Users\Ella\Downloads\rosalind_revp.txt')) as restriction_file:
    restriction_site_finder(restriction_file)
