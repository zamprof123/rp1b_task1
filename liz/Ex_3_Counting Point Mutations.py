#3 Counting Point Mutations
s="" 

def hamming_dist(s,t):
    ham_dist=0
    for p in range(len(s)): #len() returns number of characters in s,range() returns a sequence of numbers, starting from 0 by default, and increments by 1.
       if s[p]!=t[p]: 
        ham_dist+=1
    return ham_dist