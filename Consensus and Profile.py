#!/usr/bin/env python
# coding: utf-8

# A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j
# 
# .
# 
# Say that we have a collection of DNA strings, all having the same length n
# . Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the j
# 
# th position, and so on (see below).
# 
# A consensus string c
# is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.
# 
# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# 
# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

# In[1]:


def parse_fasta(file):
    #On ouvre le file et on créer un dictionnaire et une variable header qui stock les indices du dico
    file = open(file, "r")
    header = ''
    dico = {}

    #On boucle sur les ligne du file
    for line in file:
    
    #On stock le nom de la séquence dans la variable header sans le > et on la stock dans le dico en face d'une case vide
        if line.startswith(">"):
            header = line[1:-1]
            dico[header] = ""
    #on additionne la ligne tant que dico[header] n'a pas changé 
        else:
            dico[header] += line[:-1]
    #!! j'ajoute pas le dernier caractère à chaque fois car c'est un \n
    
    return dico  


# In[5]:


q = parse_fasta('file/rosalind_cons_7_dataset.txt')


# In[6]:


all_seq = []

for letter, value in enumerate(q):
    all_seq.append(q[value])

Max = []
consensus =""
C_seq = "C:"
G_seq = "G:"
T_seq = "T:"
A_seq = "A:"

for k in range(len(all_seq[0])):

    a = []  
    
    for i in range(len(all_seq)):
        a.append((all_seq[i])[k])
        C = a.count("C")
        G = a.count("G")
        T = a.count("T")
        A = a.count("A")
        
        
    C_seq = C_seq + " " + str(C)
    G_seq = G_seq + " " + str(G)
    T_seq = T_seq + " " + str(T)
    A_seq = A_seq + " " + str(A) 
    
    if C >= G and C >= A and C >= T:
        consensus = consensus + "C"
    elif T >= G and T >= A and T >= C:
        consensus = consensus + "T"
    elif A >= C and A >= G and A >= T:
        consensus = consensus + "A"
    elif G >= C and G >= A and G >= T:
        consensus = consensus +"G"
    
print(consensus)   
print(A_seq)
print(C_seq)
print(G_seq)
print(T_seq)
    


# In[ ]:




