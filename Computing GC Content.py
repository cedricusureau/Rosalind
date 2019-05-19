#!/usr/bin/env python
# coding: utf-8
#Problem

#The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or #'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any #DNA string has the same GC-content.

#DNA strings must be labeled when they are consolidated into a database. A commonly used method of #string labeling is called FASTA format. In this format, the string is introduced by a line that #begins with '>', followed by some labeling information. Subsequent lines contain the string #itself; the first line to begin with '>' indicates the label of the next string.

#In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", #where "xxxx" denotes a four-digit code between 0000 and 9999.

#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

#Return: The ID of the string having the highest GC-content, followed by the GC-content of that #string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise #stated; please see the note on absolute error below.
# In[21]:


#une fonction "maison" pour parse les FASTAs

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


# In[44]:


seqs = parse_fasta('file/rosalind_gc.txt')


# In[45]:


best_GC = 0

#je boucle sur les clés + valeur 

for i,j in seqs.items() :
    
    #je compte le %
    GC = (j.count('G') + j.count('C'))/len(j) * 100
    
    #j'imprime le résultat s'il est meilleur que le précédent
    if GC > best_GC:        
        
        best_GC = GC
        print(i)
        print(GC)
    


# In[ ]:




