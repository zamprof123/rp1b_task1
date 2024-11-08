import os # Import "os" library

f = open(os.path.expanduser("~/Desktop/rosalind_prot-2.txt")) # Open the relevant file and store it into a temporary variable in python, named "f".
file = f.read().replace("\n", "") # Combine all lines within the file into a single line and replace the individual "\n" by an empty string ("").


# Translation Function.
def RNA_AA_translation(seq): # Call translation function which takes only one argument ("seq").

    # Dictionary setting each codon equal to the relevant encoding amino acid.
    codon_aa_dictionary = {"AUG":"M","UUU":"F","UUC":"F",'UUA':'L','UUG':'L','UCU':'S',
                  'UCC':'S','UCA':'S','UCG':'S','CUU': 'L','AUU': 'I','GUU': 'V',
                  'CUC': 'L','AUC': 'I','GUC': 'V','CUA': 'L','AUA': 'I','GUA': 'V',
                  'CUG': 'L','GUG': 'V','CCU': 'P', 'ACU': 'T','GCU': 'A','CCC': 'P',
                  'ACC': 'T','GCC': 'A','CCA': 'P','ACA': 'T','GCA': 'A','CCG': 'P',
                  'ACG': 'T','GCG': 'A','UAU': 'Y','CAU': 'H','AAU': 'N','GAU': 'D',
                  'UAC': 'Y','CAC': 'H','AAC': 'N','GAC': 'D','UAA': '*','CAA': 'Q',
                  'AAA': 'K','GAA': 'E','UAG': '*','CAG': 'Q','AAG': 'K','GAG': 'E',
                  'UGU': 'C','CGU': 'R','AGU': 'S','GGU': 'G','UGC': 'C','CGC': 'R',
                  'AGC': 'S','GGC': 'G','UGA': '*','CGA': 'R','AGA': 'R','GGA': 'G',
                  'UGG': 'W','CGG': 'R','AGG': 'R','GGG': 'G'
                                }


    protein_translation = "" # Creating an empty string to append the final translated sequence.

    for nuc in range(0, len(seq), 3): # For nucleotide in the entire length of the sequence.
        codon = seq[nuc:nuc+3] # Codon = nucleotide of index of 1 nucleotide, make it of index 3.
        if codon in codon_aa_dictionary: # If the codon within "seq" is any of the keys within codon_protein_dictionary.
            protein_translation += codon_aa_dictionary[codon] # Append the encoded value for the amino acid of that codon into the empty string stored within the variable named "protein_translation".

    return protein_translation # Return protein_translation.


print(RNA_AA_translation(file)) # Print the file (RNA sequence) and pass the function "RNA_AA_translation".