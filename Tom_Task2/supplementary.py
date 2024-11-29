#basic program to calculate average read depth's for Question 2

import os
import re
import numpy as np

#see question 2.1 for commands for file generation
with open((os.path.expanduser('~/Desktop/info_n.txt')), 'r') as f:
    file = f.read().split('\n')
    lst = []
    for line in file:
        if line.startswith('N'):
            lst.append(line)

#separate 'indel' mutations
indels, lines = [], []
for x in lst:
    if 'INDEL' in x:
        indels.append(x)
    else:
        lines.append(x)

#create list containg read depths
def read_depths(lst):
    read_depth = []
    for x in lst:
        obj = re.search(r"DP=...",x)
        read_depth.append(int(obj.group()[3:].replace(';', '')))
    return read_depth


#print mean read depths
print(np.mean(read_depths(indels)))
print(np.mean(read_depths(lines)))
