"""
one, two, three- three nucleotides!! - Nucleotide Counter

input: nucleotide sequence, single sequence ONLY
output:nucleotide counts, in the order ACGT

TO DO:
WRAP INTO FUNCTION done
CLEAN UP VARS done
ADD FILE READING/ERROR HANDLING

you might notice the answer prints twice, this is because i have both a single-line answer,
and a method that allows you to change the number of nucleotides you're counting- why would you ever want to do that? god only knows,
but i implemented it.
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

            if any(char not in nucleotides for char in seq):
                raise ValueError("INVALID CHARACTERS.")
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

nucleotides = (["A","C","G","T"]) #theres not much reason for this to change but if you want to, you can.
def seq_count(seq):

    occ = {i:0 for i in nucleotides} #useful but of code that sets up a dictionary with a key of 0- highly modular, use in future.
    for i in seq: #cycle through all letters in the sequence
        if i in occ: #if the letter is in the dictionary we set up...
            occ[i] += 1 #increment the value by one

    vlist = list(occ.values())
    return vlist

file_path = "(counting nucleotides) Example File.txt"
seq = extractSEQ(file_path)
vlist = seq_count(seq)
print(" ",' '.join(str(value) for value in vlist)) #1 CONVERT VALUES TO STRING (STRVALUE FOR VALUE IN VLIST) 2#JOIN ALL STR VALUES WITH A SPACE " ".JOIN #3 PRINT ALL

print("\n" + str(seq.count("A")), seq.count("C"), seq.count("G"), seq.count("T")) #you can do this in one line -NOT A SCALEABLE APPROACH, WORKS WELL FOR TRANSCRIPTS THOUGH

