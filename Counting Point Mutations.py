#!/usr/bin/env python
# coding: utf-8
#Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), #is the number of corresponding symbols that differ in s and t

#. See Figure 2.

#Given: Two DNA strings s
#and t of equal length (not exceeding 1 kbp).

#Return: The Hamming distance dH(s,t)
.
# In[19]:


#j'utilise la fonction splitlines pour séparer les deux séquences du fichier textes
file = open('file/rosalind_hamm_1_dataset.txt')
seq = file.read().splitlines()


# In[28]:


n_mut = 0

#je boucle sur les caractères de la première séquence : s'il est différent du caractère de la deuxième séquence au même indice, j'ajoute 1
for j, i in enumerate(seq[0]) :
    
    if i != seq[1][j]:
        n_mut += 1
    
    indice += 1

print(n_mut)

