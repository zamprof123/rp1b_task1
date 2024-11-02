import os #load file from desktop

with open((os.path.expanduser('~/Desktop/rosalind_grph.txt')), 'r') as f:
    strings = f.read().replace('\n', '').split('>')[1:] #create list of strings

list = []
for x in strings:
    for y in strings:
        if x[-3:] == y[13:16] and x != y: #as per problem description, check which strings overlap by 'k' bases, k = 3
            list.append(x[:13] + ' ' + y[:13]) #append identifiers of overlapping strings to my list

for ans in list: #output solution in appropriate format
    print(ans)
