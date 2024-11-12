def parse_fasta(file_path):
    sequences = {}
    current_id = None
    current_sequence = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                # Save the previous sequence before starting a new one
                if current_id is not None:
                    sequences[current_id] = ''.join(current_sequence)
                # Start a new sequence
                current_id = line[1:]  # Skip the '>' character
                current_sequence = []
            else:
                # Add to the current sequence
                current_sequence.append(line)
        
        # Save the last sequence in the dictionary
        if current_id is not None:
            sequences[current_id] = ''.join(current_sequence)

    return sequences

def gc_content(sequence):
    """Calculate the GC content percentage of a DNA sequence."""
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

def find_highest_gc_content(sequences):
    highest_gc_id = None
    highest_gc_content = 0

    for seq_id, sequence in sequences.items():
        gc = gc_content(sequence)
        if gc > highest_gc_content:
            highest_gc_content = gc
            highest_gc_id = seq_id

    return highest_gc_id, highest_gc_content

# Updated file path
file_path = "rosalind_gc-3.txt"

# Parse the FASTA file and calculate GC content
sequences = parse_fasta(file_path)
highest_gc_id, highest_gc_content = find_highest_gc_content(sequences)

# Output the result
print(f"ID with highest GC content: {highest_gc_id}")
print(f"GC content: {highest_gc_content:.6f}%")
