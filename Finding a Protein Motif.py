#!/usr/bin/env python
# coding: utf-8

# Problem
# To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.
# 
# You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into
# 
# http://www.uniprot.org/uniprot/uniprot_id
# Alternatively, you can obtain a protein sequence in FASTA format by following
# 
# http://www.uniprot.org/uniprot/uniprot_id.fasta
# For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.
# 
# Given: At most 15 UniProt Protein Database access IDs.
# 
# Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
# 
# Sample Dataset
# A2Z669
# B5ZC00
# P07204_TRBM_HUMAN
# P20840_SAG1_YEAST
# Sample Output
# B5ZC00
# 85 118 142 306 395
# P07204_TRBM_HUMAN
# 47 115 116 382 409
# P20840_SAG1_YEAST
# 79 109 135 248 306 348 364 402 485 501 614

# In[9]:


from urllib.request import urlopen

#J'essaye tant bien que mal de définir une fonction qui importe les séquences protéique depuis uniprot
def url_vers_sequence(url):
    
    r = urlopen(url)
    seq_bytes = []
    seq_list = []
    seq = ""
    
    for line in r :
        seq_bytes.append(line)
    
    for lines in seq_bytes:
        seq_list.append(lines.decode())
    
    for indice, line in enumerate(seq_list) :
        if indice != 0:
            seq = seq + seq_list[indice]
            
    return seq


# In[11]:


fichier = open("file/rosalind_mprt.txt", "r")

#je boucle sur les protéines proposé et je vais chercher leur URL. Ensuite je cherche les indices qui remplisse la condition de N-glycosylation.
for line in fichier:
    r = 'http://www.uniprot.org/uniprot/' + line[:-1] + '.fasta'
    seq = url_vers_sequence(r).replace('\n', '')
    
    indexes = ""
    for i, j in enumerate(seq) :
        if i < (len(seq)-4):
            if seq[i] == "N" and seq[i+1] != "P" and (seq[i+2] == "S" or seq[i+2] == "T") and seq[i+3] != "P":
                t = i+1
                indexes = indexes + " "+ str(t)
                
    if indexes !="":
            
        print(line[:-1])
        print(indexes)


# In[ ]:




