#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem

#A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

#An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

#Given: A DNA string s

#of length at most 1000 nt.

#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s

#.
#Sample Dataset

#AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

#Sample Output

#20 12 17 21


# In[10]:


file = open('file/rosalind_dna.txt')
seq = file.read()


# In[11]:


print(seq.count('A'),seq.count('C'),seq.count('G'),seq.count('T'))

