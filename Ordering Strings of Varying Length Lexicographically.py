#!/usr/bin/env python
# coding: utf-8

# Problem
# Say that we have strings s=s1s2⋯sm and t=t1t2⋯tn with m<n. Consider the substring t′=t[1:m]. We have two cases:
# 
# If s=t′, then we set s<Lext because s is shorter than t (e.g., APPLE<APPLET).
# 
# Otherwise, s≠t′. We define s<Lext if s<Lext′ and define s>Lext if s>Lext′ (e.g., APPLET<LexARTS because APPL<LexARTS).
# 
# Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4).
# 
# Return: All strings of length at most n formed from A, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)
# 
# Sample Dataset
# D N A
# 3

# In[1]:


#Ceci n'est pas mon code mais j'ai perdu le miens après avoir résolu l'exercice 

input = """
D N A
3
""".strip('\n').split('\n')

alphabet, n = input[0].split(), int(input[1])

def generate(n, h=""):
    print (h)
    if n == 0:
        return
    for c in alphabet:
        generate(n-1, h+c)

generate(n)


# In[ ]:




