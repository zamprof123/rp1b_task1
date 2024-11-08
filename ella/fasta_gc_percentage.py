def fasta_gc_percentage(fasta_file):
    """ Finds the GC percentage for a list of sequences. Input: DNA sequences in a fasta file format.
    Output: genes with their specific GC content & the gene with the highest GC content"""

#Fasta file dictionary creation
    gene_dictionary = {}
    for line in fasta_file:
        # Adding lines to a dictionary
        if ">" in line:
            gene_name = line.strip("\n")  # setting line as the key if it has >
            gene_dictionary[gene_name] = ""  # setting the value of the key to empty string  e.g >rosalind_xxxx : "",
        else:
            gene_dictionary[gene_name] += line.strip("\n")  # now adding each line after as the value to that key

# Computing max GC content
    gene_name_list = []
    gc_list = []

    for base in gene_dictionary:  # base will be each rosalind identifier
        nt_sequence = gene_dictionary[base].upper()  # calling the value of that key and setting it to a variable thats always uppercase

        # Calculating gc percentage
        gc_count = nt_sequence.count("G") + nt_sequence.count("C")
        gc_content = round(gc_count / len(nt_sequence) * 100, 2)  # rounding to 2 decimal places.
        # round function doesnt include 0 in the end .20 becomes .2

        print(f"""{base.strip(">")} = {gc_content}%""")  # lists all genes and their gc percentage
        # This is for my benefit when using this function.


# Identifying the gene with the highest GC percentage #
        gene_name_list.append(base)  # adding gene names to list
        gc_list.append((gc_content)) # adding all the percentages to a list sequentually


    max_gc = max(gc_list) # calling the highest percentage
    max_gc_position = gc_list.index(max_gc)  # finding the index of the highest gc
    max_gene_name = gene_name_list[max_gc_position]  # using index to find gene name of highest gc content

    print()  # adds gap btw outputs so easier to read
    print(f"""Gene with highest GC content: 
{max_gene_name.strip('>')}
{max_gc}%
    """)  # formatted nicely so you can clearly see gene with highest GC content


# Execitung the function
import os
with open(os.path.expanduser(r"C:\Users\Ella\Downloads\rosalind_gc.txt")) as oogy:
    fasta_gc_percentage(oogy)