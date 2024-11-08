import os # Import "os" library.

with open(os.path.expanduser("~/Desktop/rosalind_subs.txt")) as f: # Open the file within the "Desktop" directory and store it as a temporary variable in Python, named "f".
    sequence = f.readline().replace("\n", "") # Replace the invisible newline character with an empty string.
    motif_seq = f.readline().strip() # Reads the second line of the file removing any newline (\n) characters.


# Motif encountering function.
def motif_in_seq(seq): # Calling "motif_in_seq" taking an input sequence (seq) as the unique argument.
    motif_indices = [] # Empty list to append all indices where the motif is found.
    motif_length = len(motif_seq) # Individualising motif length to whichever number of nucleotides the motif has.

    for nuc in range(len(seq) - motif_length + 1): # For nucleotide in sequence, set the appropriate length, specific to the length of the relevant motif.
        motif = seq[nuc:nuc+motif_length] # Setting one individual nucleotide to be equal to the specific length in nucleotides of the relevant motif.
        if motif == motif_seq: # If motif is equal to whichever string located in line 2 of file "f".
            motif_indices.append(nuc + 1) # Append the index of the motif + 1, given that indices in Python start at 0.

    return " ".join(map(str, motif_indices)) # Mapping the list of indices, turning them into strings, removing the brackets. Joining an empty string in order to separate them by spaces instead of commas.


print(motif_in_seq(sequence)) # Print list of indices where the motif is found within the sequence.
print(sequence.index(motif_seq)) # Print the index position of the motif we are looking for to ensure that is not part of the list. Avoiding potential bias!