"""
Point mutations by any other name are just as , point mutatation-y.

input:two sequences, each on their own line.
output:the number of point mutations (differences) between each sequence

amusingly this took me far longer to do than i'd like to admit- almost instantly after solving it i realized you could solve this problem
in a handful of lines. Heres the better of the two solutions.


TO DO:
PUT INTO A FUNCTION - DONE
ERROR HANDLING - DONE
MAKE IT READ A FILE- DONE

please refrain from breaking my code too hard.
regards,
ted
"""

def extractSEQ(file_path): # i really should be making a separate py file with these file parsers as modules i can just call but A: i'm lazy, B: i dont really want to juggle multiple files when stuffs this small
    try:
        with open(file_path, 'r') as file:
            # read the first line and split it into parts
            seqa,seqb = (line.strip() for line in file)

            if not seqa or not seqb:
                raise ValueError("FILE NEEDS TWO LINES.")
            
        
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
        
    return seqa, seqb

def Ham(seqa, seqb):
    if len(seqa) != len(seqb):
        raise ValueError("Sequences must be of equal length!")
    temp = 0

    for a, b in zip(seqa, seqb): #this basically iterates both sequences simultaniously which is REALLY useful for this
        if a != b:
            temp += 1 #ticks up when A is DIFFERENT to B (positions arent the same)
    return(temp)
        
file_path = "(hamming distance) Example File.txt"

# seqa, seqb = extractSEQ(file_path)
# print(" POINT MUTATION COUNT: " ,Ham(seqa,seqb)) in case the try block breaks- WHICH IT SHOULDNT!!

try:
    seqa, seqb = extractSEQ(file_path)
    print("POINT MUTATION COUNT:", Ham(seqa, seqb))
except Exception as e:
    print(f"uh, oops: {e}")