#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem

#In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

#The reverse complement of a DNA string s
#is the string sc formed by reversing the symbols of s

#then("taking", "the", "complement", "of", "each", "symbol", "(e.g.,", "the", "reverse", "complement", "of", ""GTCA"", "is", ""TGAC").")

#Given: A DNA string s

#of length at most 1000 bp.

#Return: The reverse complement sc
#of s.


# In[10]:


file = open('file/rosalind_revc_1_dataset.txt')
seq = file.read()


# In[17]:


comp_seq1= seq.replace('A','t').replace("T","a").replace("C","g").replace('G','c').upper()

reponse = "".join(reversed(comp_seq1))


# In[18]:


print(reponse)

