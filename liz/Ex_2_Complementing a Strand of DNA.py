#2 
import re #import re module for Regular expression

seq=""

def c_strand(seq):
    mapping=str.maketrans('ATCG','TAGC') #maketrans()returns a mapping table translate() replace ATCG to complementary.
    return seq.translate(mapping)[::-1]

print(c_strand(seq))