import os #read file from desktop

with open((os.path.expanduser('~/Desktop/rosalind_gc.txt')), 'r') as f:
    file = f.read().replace('\n', '').split('>')[1:]


def get_gc_content(seq): #function to compute GC content
    return ((seq.count('G') + seq.count('C'))/len(seq)) * 100


dict = {} #dictionary created to store identifiers and appropriate GC content
for string in file:
    ID = string[:13]
    dict[ID] = get_gc_content(string[13:])


print(max(dict, key=dict.get))
print(max(dict.values()))
