"""
a lesson in making unreasonably large tables

input: a single nucleotide sequence
output: translated protein sequence

CLEAN VARS done
ADD FILE READING done
ADD ERROR HANDLING done
COMMENT done

i think i could've done this with a map.
"""

def extractSEQ(file_path): # i really should be making a separate py file with these file parsers as modules i can just call but A: i'm lazy, B: i dont really want to juggle multiple files when stuffs this small
    try:
        with open(file_path, 'r') as file:
            # read the first line and split it into parts
            seq = file.readlines()
            if not seq:
                ("EMPTY FILE.")
            if len(file.readlines()) > 1:
                raise ValueError("ONLY ONE SEQUENCE.")
            seq = seq[0].strip()

    except FileNotFoundError:
        print("NO FILE WAS FOUND, CHECK INPUT LOCATION FOR SPELLING MISTAKES")
        raise
    except ValueError:
        print("STRINGS ONLY.")
        raise
    except Exception as e:
        print(f"what did you even do? : {e}")
        raise
        #explanatory checks
        
    return seq

def translate_rna(seq):

    residuetable = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", #table of residues
        "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
        "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
        "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
        "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
        "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
        "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
        "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
        "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
        "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
        "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
        "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
        "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
        "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
        "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
        "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

    amino_acids = [] # initialize empty list
    for i in range(0, len(seq), 3): # for values in range of 1 - maxlength iterate in steps of 3
        codon = seq[i:i+3] # codon is equal to the current step of 3
        if codon in residuetable: # if the codon is in the table
            amino_acids.append(residuetable[codon]) #add to a list named aminoacids
    return amino_acids

file_path = "(translation) Example File.txt"

seq = extractSEQ(file_path)
translated_sequence = "".join(translate_rna(seq))
print("START", translated_sequence)