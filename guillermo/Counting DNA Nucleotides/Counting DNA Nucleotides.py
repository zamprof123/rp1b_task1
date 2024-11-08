import os # Importing "os" library.
def open_file(file_location): # Calling the "open_file" function taking one argument.
    with open(os.path.expanduser(file_location), 'r') as file: # Open the relevant file location as "read" within a temporary file in Python "file".
        return file.readline()  # Return the file, red line by line.


# Variable to store the "open_file" function in order to open the relevant sequence file.
Sequence_file = open_file("~/Desktop/rosalind_dna-2.txt")

# List of all 4 DNA nucleotides.
DNA_nucleotides = ["A", "C", "G", "T"]


# Method 1
def counting_nuc(seq): # Calling the function "sequence_counter", taking one argument (sequence).
    nuc_dict = {"A": 0, "C": 0, "G": 0, "T": 0} # Dictionary creating a counter for each nucleotide, with each nucleotide being the key and setting an initial value of 0.

    # For Loop
    for nuc in seq: # For each nucleotide in the corresponding sequence
        if nuc in nuc_dict: # If the nucleotide is one of the 4 nucleotides within the dictionary "nuc_dict".
            nuc_dict[nuc] += 1 # Sum 1 the initial value of 0 attributed to each key within "nucleotide_dictionary".


    return " ".join(str(nuc_dict[nuc]) for nuc in DNA_nucleotides) # For nucleotide within "DNA_nucleotides" - join an empty string to the updated value from the dictionary "nuc_dict" converted into a string.


# Method 2
def nucleotide_counter(seq): # Accurate function to count DNA Nucleotides.

    A_counter = seq.count("A") # Count all "A"s within the corresponding sequence.
    C_counter = seq.count("C") # Count all "C"s within the corresponding sequence.
    G_counter = seq.count("G") # Count all "G"s within the corresponding sequence.
    T_counter = seq.count("T") # Count all "T"s within the corresponding sequence.


    return f"{A_counter} {C_counter} {G_counter} {T_counter}" # Return each counter separately as a separated string (+f string)


print(counting_nuc(Sequence_file)) # Print counter method 1
print(nucleotide_counter(Sequence_file)) # Print counter method 2