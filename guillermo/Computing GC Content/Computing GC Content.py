import os # Importing "os" library.

def read_file(path_of_file): # Calling a function named "read_file" which takes one argument "path_of_file".
    f = open(os.path.expanduser(path_of_file), 'r') # Set the interchangeable argument to a temporary variable ("f") using the functions within the "os" library to open whichever file falls under the argument.

    return [line.strip() for line in f.readlines()] # List of comprehension which returns the file "f" line by line, stripping any whitespaces and the invisible \n at the end of each line, excluding the last one.


def GC_counter(seq): # Calling a function named "GC_counter" with takes one argument, this being "seq".

    # Calculate the percentage of Guanine and Cytosine bases within "seq" by counting each nucleotide and dividing it by the length of "seq". The corresponding value is then multiplied by 100.
    total_gc_counter_percentage = (seq.count("G") + seq.count("C")) / len(seq) * 100

    return total_gc_counter_percentage # Return the variable "total_gc_counter_percentage".


# Variables for data storage.

# Variable that uses the function "read_file" to read the required FASTA file from Rosalind, in order to analyse it.
FASTA_file_read = read_file("~/Desktop/rosalind_gc.txt")

# Dictionary to store the "labels" of each sequence and their respective sequences as keys and values.
FASTA_dictionary = {}

# Empty string which was used to temporarily store teh label pertaining to each individual sequence.
FASTA_labels = ""


# Conversion of FASTA file stored as a list into a dictionary, via using a for loop.
for line in FASTA_file_read: # For each line in the FASTA file stored within the variable "FASTA_file_read".
    if ">" in line: # For every entry in the lhe list (does it have a ">"?). If there is a ">" in the line.
        FASTA_labels = line # The line which contains a ">", will be stored as a string within FASTA_labels.
        FASTA_dictionary[FASTA_labels] = "" # New entry in FASTA_dictionary, using the label stored in FASTA_labels as the key. Value is set to an empty string ("") to then store the corresponding DNA sequence.
    else: # If the previous condition = not TRUE
        FASTA_dictionary[FASTA_labels] += line # If = FALSE -> Accumulate the line (which will be its respective DNA sequence) to the dictionary as a value.

# Filter through the FASTA_dictionary (both keys and values). Apply GC counter function to the values within the dictionary
Result_Dictionary = {key: GC_counter(value) for key, value in FASTA_dictionary.items()} # Dictionary comprehension, outputs sequence label (KEY) and "G & C percentage" as the value.

Max_GC_value_output = max(Result_Dictionary.values()) # Look within Result_Dictionary (values) and output the maximum value.
Max_GC_key = [key for key, value in Result_Dictionary.items() if value == Max_GC_value_output] # List comprehension - for a key out of all keys, accumulate the one with the highest "G & C percentage" from the variable "Max_GC_value_output".
Max_GC_key_output = " ".join(map(str, Max_GC_key)) # Joining an empty string to a mapped function of the variable "Max_GC_key", although using "str" is not really necessary as Max_GC_key is already accumulating a string. " " = delimiter.


# print(FASTA_dictionary) # Prints the name of the sequence as the key and the actual sequence as the value.
# print(Result_Dictionary) # Prints "key" + GC_counter(value) as a %.
print(Max_GC_key_output.strip(">")) # Prints key for the "max" GC (%), without the brackets and strip the ">" off.
print(Max_GC_value_output) # Print value with "max" for GC (%).