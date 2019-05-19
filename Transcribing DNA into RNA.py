#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem

#An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

#Given a DNA string t
#corresponding to a coding strand, its transcribed RNA string u is formed by replacing all #occurrences of 'T' in t with 'U' in u

#.

#Given: A DNA string t
#
#having length at most 1000 nt.

#Return: The transcribed RNA string of t
#.


# In[3]:


file = open('file/rosalind_rna.txt')
seq = file.read()


# In[4]:


trans_seq = seq.replace('T','U')


# In[6]:


print(trans_seq)


# In[ ]:




