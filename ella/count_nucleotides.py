
#Rosalind only wanted DNA bases but i added uracil becuase it seems useful to use for RNA as well
def nucleotide_counter(sequence):
    """ Counts the number of nucleotides in a DNA or RNA string. Input: string. Output: length of string &
    number of each base (A,T,C,G or U) """
    sequence = sequence.upper() # make entire seqeucne uppercase so even if you submit
    # lowercase letters counter still works
    a_count = sequence.count("A")
    t_count = sequence.count("T")
    c_count = sequence.count("C")
    g_count = sequence.count("G")
    u_count = sequence.count("U")
    seq_length = len(sequence)
    print(f"Length = {seq_length} nucelotides")
    print(f"Adenine count: {a_count}, Cytosine count: {c_count}, Guanine count: {g_count}, Thymine count: {t_count}, Uracil count: {u_count}")
    
# Executing file
import os

with open(os.path.expanduser(r"C:\Users\Ella\Downloads\rosalind_prot.txt")) as file:
    sequence = file.read().replace("\n", "")
nucleotide_counter(sequence)