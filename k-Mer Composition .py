#!/usr/bin/env python
# coding: utf-8

# Problem
# For a fixed positive integer k, order all possible k-mers taken from an underlying alphabet lexicographically.
# 
# Then the k-mer composition of a string s can be represented by an array A for which A[m] denotes the number of times that the mth k-mer (with respect to the lexicographic order) appears in s.
# 
# Given: A DNA string s in FASTA format (having length at most 100 kbp).
# 
# Return: The 4-mer composition of s.
# 
# Sample Dataset
# >Rosalind_6431
# CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
# CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
# TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
# AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
# GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
# CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
# CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG
# Sample Output
# 4 1 4 3 0 1 1 5 1 3 1 2 2 1 2 0 1 1 3 1 2 1 3 1 1 1 1 2 2 5 1 3 0 2 2 1 1 1 1 3 1 0 0 1 5 5 1 5 0 2 0 2 1 2 1 1 1 2 0 1 0 0 1 1 3 2 1 0 3 2 3 0 0 2 0 8 0 0 1 0 2 1 3 0 0 0 1 4 3 2 1 1 3 1 2 1 3 1 2 1 2 1 1 1 2 3 2 1 1 0 1 1 3 2 1 2 6 2 1 1 1 2 3 3 3 2 3 0 3 2 1 1 0 0 1 4 3 0 1 5 0 2 0 1 2 1 3 0 1 2 2 1 1 0 3 0 0 4 5 0 3 0 2 1 1 3 0 3 2 2 1 1 0 2 1 0 2 2 1 2 0 2 2 5 2 2 1 1 2 1 2 2 2 2 1 1 3 4 0 2 1 1 0 1 2 2 1 1 1 5 2 0 3 2 1 1 2 2 3 0 3 0 1 3 1 2 3 0 2 1 2 2 1 2 3 0 1 2 3 1 1 3 1 0 1 1 3 0 2 1 2 2 0 2 1 1

# In[13]:


import itertools
from parse_fa import parse_fasta


#je créer la list de tout les 4-mers possible
a = itertools.product('ATCG', repeat=4)
all_kmers = []
for i in a :
    all_kmers.append(list(i))
    
#je les met dans l'ordre lexicographique 
all_kmers_j = []

for i in sorted(all_kmers):
    all_kmers_j.append(''.join(i))

#je parse mon fasta

d = parse_fasta("file/rosalind_kmer_1_dataset.txt")
seq = d["Rosalind_0537"]

#J'attribue à chaque kmers la valeur de 0 que je ferais grossir en passant une fenetre sur ma séquence
dico = {}

for i in all_kmers_j:
    dico[i] = 0
    
for i,j in enumerate(seq):
    if len(seq[i:i+4]) == 4:
        dico[seq[i:i+4]] += 1
    
#j'affiche le résultat avec un join dans une liste des mes résultat en str 
a = list(dico.values())
b=[]
for i in a :
    b.append(str(i))
    
print(" ".join(b))

