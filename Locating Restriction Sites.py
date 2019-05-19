#!/usr/bin/env python
# coding: utf-8

# Problem
# Figure 2. Palindromic recognition site
# 
# A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.
# 
# Given: A DNA string of length at most 1 kbp in FASTA format.
# 
# Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
# Sample Dataset

# In[13]:


seq = 'GCGCCAGGTGCTGCATCCCCGAATCCGGCGAAACATGCTCTTAATCGATCCCAACAAGGTCGAAGTATTCTTCAACATTTCCCCATTCTTCGTGCAGCAGTGGATATGGTGCGACCCCACTGGTATAGGCTTTAATACTGGTATTGAGACTCGATAATAGAGAGATCGTCCGGCTCCTACATACCGGGGGGAGCCACTTATTCGACTAGAGTTAAGTGACGGTGCCAACCCACTGGAGAACTACTGACCAATAGTTCCAAGCACGCGTTATTATGCACAACGCCCTCCTGCATTATAGTAGCTGGGAAGGCCTAAATTTCCGTCCGAAAACCACTTCATAGCGCTCGACTGAAACGATGTACACTCAGCCTGTAGTCCAGAACTGAGACTCATTGGGGATCGATCCACATTAATGTGAAAGGGTATGTAAATTTTGCTTCTAGCCCACCCATCAAAATGTAAGCCAGCGAAGAAGACTCTCCGTCCACTGGAGGCCCTTGCTCTCTTTTCCCAGTTGCCGCATTTCACTGACAAGTTCGCACAACAGTAGCGTATGGGTAATGATCCCGTCTAATGTGGCGATAGCGACTATTAATTCATCCTGTACCAACTTTGCTAACTATATGGTTAGGACACGGTAATCAGCTGCTGATGTGGTGGAAAGGCCAGCTACACCCAAACGCAGAGGGGAGTAGGCGTATCCCTTCGTAACAGCCCTTGTACAAGGGGACTCGGACACGATGTAATAGGGTTAATAGTCTTTTATGATAGGCAACCTAACAATTTTCGAAGACGAAGAGACACTGGTTATAGGTTCTCGCG'
#je créer une fonction qui renvoie un brin reverse.  
def reverse_complement(seq):
    reverse_comp = ""
    for i in seq[::-1]:
        if i == 'T':
            reverse_comp += 'A'
        if i == 'A':
            reverse_comp += 'T'
        if i == 'G':
            reverse_comp += 'C'
        if i == 'C':
            reverse_comp += 'G'
        
    return reverse_comp


# In[14]:


for i in range(len(seq)):
    
    for k in range(4,13):
        a = seq[i:i+k]
        b = reverse_complement(a)
        
        if len(a) >= 4 and a == b and k <= len(a):
            print(i+1, len(a))

