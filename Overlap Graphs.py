#!/usr/bin/env python
# coding: utf-8

# Problem
# 
# A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.
# 
# A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v
# and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v)
# 
# .
# 
# For a collection of strings and a positive integer k
# , the overlap graph for the strings is a directed graph Ok in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t
# 
# to prevent directed loops in the overlap graph (although directed cycles may be present).
# 
# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# 
# Return: The adjacency list corresponding to O3
# . You may return edges in any order.
# 

# In[6]:


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

q = parse_fasta('file/rosalind_grph.txt')


# In[7]:


name_list = []

for name in q:
    name_list.append(name)  
    
    #print(name_list)
a = 0


for valeur in q.values():
    s = valeur[-3:]
    b = 0
    
    for valeur2 in q.values():
        t = valeur2[0:3]        
        if s == t and valeur2 != valeur:
            print(name_list[a], name_list [b])
        
        b = b + 1 
    
    a = a + 1  


# In[ ]:




