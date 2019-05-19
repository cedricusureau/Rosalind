#!/usr/bin/env python
# coding: utf-8

# Problem
# 
# A permutation of length n
# is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5
# 
# .
# 
# Given: A positive integer n≤7
# 
# .
# 
# Return: The total number of permutations of length n
# , followed by a list of all such permutations (in any order).

# In[29]:


#J'utilise la fonction permutations de itertools
import itertools
n = 5


# In[30]:


#je convertie les tuples en liste. J'utilise la fonction join pour l'affichage. 

print(len(list(itertools.permutations(range(1,n+1), n))))

for i in list(itertools.permutations(range(1,n+1), n)):
    print(' '.join(map(str,i)))

