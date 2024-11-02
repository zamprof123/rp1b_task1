import os #load file from desktop

with open((os.path.expanduser('~/Desktop/rosalind_revp.txt')), 'r') as f:
    string = f.read().replace('\n', '')[14:] + 'N'*12 #a series of 12 character's are added to the end of the string to prevent unwanted behaviour once program reaches end of string


my_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'n'} #dictionary for complementary base's


def find_restriction(seq): #function to identify restriction sites
    sec = [seq[0:n] for n in range(4, 13, 2)] #define the window for section of string being analysed
    restriction_sites = []
    for x in sec:
        middle = int(0.5*len(x))
        rev = x[middle:]
        rev = ''.join(my_dict.get(x) for x in rev) #generate complementary reverse strand
        if x[:middle] == rev[::-1]: #check wether current sequence in the window is a reverse palindrome
            restriction_sites.append(x) #if a restriction site is found (i.e. reverse palindrome), the sequence of the restriction site is added to a list
    return restriction_sites


sites = []
counter, counters = 1, [] #counter to count iterations of proceeding loop, blank list to append locations of restriction sites
for x in string:
    while len(string) >= 12:
        sites.append(find_restriction(string)) #output of function is appended to new list, if no restriction site is found during current iteration, a blank value is added to the new list
        counters.append(counter) #as per the problem description, the location of each restriction site must be returned, so value of the counter is saved alongside each output of the above function
        string = string[1:] #string is shortened to allow window to traverse length of the string
        counter += 1 #update the counter

for x, y in zip(sites, counters): 
    if x: #exclude blank items in list of sites
        for site in x:
            print(y, len(site)) #print out lengths of restriction sites alongside locations 
