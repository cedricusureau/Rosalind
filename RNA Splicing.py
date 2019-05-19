#!/usr/bin/env python
# coding: utf-8

# Problem
# 
# After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.
# 
# Given: A DNA string s
# (of length at most 1 kbp) and a collection of substrings of s
# 
# acting as introns. All strings are given in FASTA format.
# 
# Return: A protein string resulting from transcribing and translating the exons of s
# 
# . (Note: Only one solution will exist for the dataset provided.)
# Sample Dataset
# 
# >Rosalind_10
# ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
# >Rosalind_12
# ATCGGTCGAA
# >Rosalind_15
# ATCGGTCGAGCGTGT
# 
# Sample Output
# 
# MVYIADKQHVASREAYGHMFKVCA
# 

# In[1]:


#Je parse
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
    #on remplis la case vide avec la bonne séquence, attention au [:-1] qui est important pour une raison qui m'échappe un peu (pour pas tenir compte du \n ?)
        else:
            dico[header] += line[:-1]
        
    return dico  

q = parse_fasta('file/rosalind_splc.txt')


# In[2]:


#Je prends les sequences dans mon dico
seq_list=[]
for i in q.values():
    seq_list.append(i)    

#je créer une str de la première séquence
all_gene = seq_list[0]


# In[3]:


index1 = []
index2 = []
spliced_gene = ''

#je récupère dans les liste 1 et 2 les positions de début et de fin des sequences à splicer.
#Attention, les introns sont pas donné dans l'ordre donc il faut trier les index

for i in seq_list[1:]:
    for k,j in enumerate(all_gene):
        if all_gene[k:k+len(i)] == i:
            a= k+len(i)
            index1.append(int(k))
            index2.append(int(a))
            
index1=sorted(index1)
index2=sorted(index2)
            
#je créer mon nouveau gène grâce aux indices stocké dans index1 et index2.
for j, i in enumerate(index1):
        if spliced_gene == '':
            spliced_gene += all_gene[0:i]
        else :
            b = index2[j-1]
            spliced_gene += all_gene[b:i]


#il manque la fin du gène, du dernier indice2 à la fin de all_gene
spliced_gene += all_gene[index2[-1]:]


#mon jolie gene splicé
print(spliced_gene)


# In[4]:


#Je traduis 

string = """TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G"""

coded = spliced_gene
decoded = ''

traL =  string.split()
traDict = dict(zip(traL[0::2], traL[1::2]))

for i in range(0, len(coded)-3, 3):
    decoded += traDict[coded[i:i+3]]

print (decoded)


# In[ ]:




