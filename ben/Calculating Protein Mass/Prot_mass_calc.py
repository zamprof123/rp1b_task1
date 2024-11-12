#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os # imports the os library
os.chdir("/home/jovyan") #changes to the appropriate working directory to access the .txt file containing the protein mass data

def create_mass_dict(): #this function creates a dictionary where the key is the individual letter code for an amino acid (AA) and the value is the corresponding molecular weight (MW) - the function takes no parameters
    with open("ben/prot_mass_table.txt") as f: #
            mass_dict_temp = {} #creates an empty dictionary that will later be populated.
            x = f.read() #reads the file saved as f and assigns it to a new temporary variable, x
            x = x.split() #overwrites the temporary variable x as a new string that contains the letter code, followed by the MW, for each amino acid
            for i in range(0, len(x), 2):
                mass_dict_temp[x[i]] = float(x[i + 1])
                # this for loop iterates through the string x and populates the dictionary mass_dictionary_temp so that the keys are the AA letter codes and the values are the corresponding MWs
    return mass_dict_temp

mass_dict = create_mass_dict() #assigns the returned value from the above function to the globabl variable mass_dict

def calculate_mass(md_par): #this function uses the dictionary created above to calculate the molecular weight of an AA sequence, the parameter given is the dictionary created above
    prot_mass_temp = 0
    with open("ben/prot_string.txt") as string: #opens the file containing the query protein sequence
        prot_seq = string.read() #assigns the protein sequence from the file to a variable
        for i in range(0, len(prot_seq)):
            AA = prot_seq[i]
            prot_mass_temp += mass_dict[AA]
            #this for loop iterates through the protein sequence one amino acid at a time, and using the dictionary accesses the MW value for each AA it reads in
            #the protein sequence, and adds that mass to the temporary protein mass variable which is returned by the function
    return prot_mass_temp

final_protein_mass = round(calculate_mass(mass_dict), 3) #with the protein mass dictionary as the parameter, the calculate mass function is called, and the return is rounded to 3 decmial places
print(final_protein_mass) #prints the final protein mass
           


# In[ ]:




