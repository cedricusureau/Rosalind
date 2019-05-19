#!/usr/bin/env python
# coding: utf-8

# In[1]:



# coding: utf-8

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
    #on remplis la case vide avec la bonne séquence, attention au [:-1] qui est important pour une raison qui m'échappe un peu
        else:
            dico[header] += line[:-1]
        
    return dico  


# In[ ]:




