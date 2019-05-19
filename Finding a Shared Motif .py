#!/usr/bin/env python
# coding: utf-8

# Problem
# A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".
# 
# Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".
# 
# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
# 
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
# 
# Sample Dataset
# 
# >Rosalind_1
# GATTACA
# >Rosalind_2
# TAGACCA
# >Rosalind_3
# ATACA
# 
# Sample Output
# AC

# In[1]:


def parse_fasta(file):
    file = open(file, "r")
    header = ''
    dico = {}

    for line in file:
    
        if line.startswith(">"):
            header = line[1:-1]
            dico[header] = ""
    
        else:
            dico[header] += line[:-1]
    
    return dico  

q = parse_fasta('file/rosalind_lcsm.txt')


# In[2]:


#seq1 sert de séquence de référence, c'est la première séquence. All_seq est la liste des 99 autres séquences
all_seq = []

for i,j in enumerate(q.values()):
    if i == 0 :
        seq1 = j
    else : 
        all_seq.append(j)
        


# In[4]:


best_shared = ''

#Je commence par les grandes tailles puis je diminue avec reversed(range)
for lenght in reversed(range(len(seq1))):
   
    #Je vais tester toutes les possibilités de séquence dans seq1 de taille 'lenght'    
    for i in range(len(seq1)):      
        a = seq1[i:i+lenght]
        
        #je défini une boléen. Tant qu'elle est vrai, le motif testé se trouve dans toutes les séquences. Je break en cas de mismatch pour gagner du temps. 
        all_shared = True
        
        for k in all_seq :            
            
            if (a in k) == False:
                all_shared = False
                break
        
        #si je n'ai aucun mismatch, alors le motif testé est bon donc j'ai trouvé mon plus long motif partagé. Je break car ça sert à rien de chercher plus petit. 
        if all_shared == True and len(a) > len(best_shared): 
            best_shared = a 
            break

print(best_shared)


# In[ ]:




