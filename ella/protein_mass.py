
def protein_mass_calc(protein_sequence: str) -> float:
    """Calculate the mass of a protein string. Input: protein sequence. Output: float """

    amino_acid_weights = {
        "G": 57.021463735, "A": 71.037113805, "S": 87.032028435, "P": 97.052763875, "V": 99.068413945,
        "T": 101.047678505, "C": 103.009184505, "L": 113.084064015, "I": 113.084064015, "N": 114.042927470,
        "D": 115.026943065, "Q": 128.058577540, "K": 128.094963050, "E": 129.042593135,
        "M": 131.040484645, "H": 137.058911875, "F": 147.068413945, "R": 156.101111050, "Y": 163.063328575,
        "W": 186.079312980
    } # table of molecular weights for each single letter amino acid

    protein_mass = 0.0

    for amino_acid in protein_sequence.upper():  # iterate over each amino acid in seqeunce
        protein_mass += amino_acid_weights[amino_acid]  # find the value of the specifc amino acid
        # add the number to the protein mass

    return round(protein_mass, 3) # round number to 3 decimal places

# Executing
import os

with open(os.path.expanduser(r"C:\Users\Ella\Downloads\rosalind_prtm.txt")) as file:
    protein_sequence = file.read().replace("\n", "")
print(protein_mass_calc(protein_sequence))