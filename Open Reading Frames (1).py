#!/usr/bin/env python
# coding: utf-8

# Problem
# Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.
# 
# An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.
# 
# Given: A DNA string s of length at most 1 kbp in FASTA format.
# 
# Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
# 
# Sample Dataset
# Rosalind_99
# AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
# 
# Sample Output
# MLLGSFRLIPKETLIQVAGSSPCNLS
# M
# MGMTPRLGLESLLE
# MTPRLGLESLLE

# In[2]:


#je récupère mon script ARN to protein je fais une fonction ADN to protein :

def dna_to_prot(Seq):
    result = ''
    dna_codon_table = """TTT F      CTT L      ATT I      GTT V
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
TGG W      CGG R      AGG R      GGG G """
    
    t = dna_codon_table.split()

    codon = []
    aa = []

    for i,j in enumerate(t):
        if i % 2 == 0 :
            codon.append(j)
        if i % 2 != 0 :
            aa.append(j)
        
    d = dict(zip(codon, aa))        

    for i in range(len(Seq)) :

        if i+2 < len(Seq) and i+1 < len(Seq):
            
            if i % 3 == 0: 
                    result += d[Seq[i:i+3]]                
                
    return result
  


# In[96]:


#c_seq est le brins complémentaire de seq

seq = 'ACCTGGCCCTTGTGGGGTGCAATTGGTAAAGCGAAGATCCGATGCTGTAAGGGTGGCTATCTCGAACGCCGTCTGCTCCTAAGTCGGTGGCGTTATACAGGTAGTTCAACCGTGAAAGCCGCTGAATGCGGGACGTTTATTGGTGCGCCACATTTGAATTCACCTTGTGTTAGGGTCGATCCCAACCTTTTGTTGAGGCACTCGAACGAGCATTTGTACGGTATACCGGTCCTTACGCATCATCACAAGATGGACAGCGAAGCCTCCAGCCAAGAAGGGCCAACAGCGGTAACTACTGTACAACATACTGCGGCAGTTTCATGCAAAAGTTCACAAACATTTACTATTACGTCGTGAGTCCCAAAACAGCCCTGACGCGGGATCGTACCCTGCTTTAGTGCATCCAGCCCAAGGCTACTTGTCCTCGATGCAAAACGTTCGAGTGTAATACTCTCCCGACTAGCTAGTCGGGAGAGTATTACACTCGAACGTTTTGCATAACCAGGTCCAACCGCTTTGGTGGCTACAGATATCGATCTGCAGTCGCCGGAGAACTCCAGTAAATCTGCCTCTCGATTCACTACGAGCGGTCAAGAGATAAAATAGATTTACGAGCTTTAGAGGGAGGCCGGAACGAGCTGAGAACAGTCACACATATTAATCGTCCGGCCCTATCTAAGCTTGCCTACGTCTCATGGTATTGATGCTGGGCATATCATTTGGTAGGGACTTCCATGTCGCCGTATAGGTAAATGAATAAATATGCGATATCAGCTATAACAACACGCAACGATGTGTCAAACACGCCGGGTAGCAAGACTCTTGCATAGTAAACAGTACGGCGAACAAACATATGGCGGGACGTTCTAAGCGTACTTGTAGGTGGTGTATACGCCAGACCTGAAGTTAGATGCATCATGAGCCCT'

c_seq = ""

for i in seq[::-1] :
    if i == 'A' :
        c_seq += 'T'
    if i == 'T' :
        c_seq += 'A'
    if i == 'C' :
        c_seq += 'G'
    if i == 'G' :
        c_seq += 'C'
        


# In[97]:


#all_reading_pos contient tous les cadres de lectures du brins forward et reverse (6 brins en tout)
all_reading_pos = []

for i in range(0,3):
    all_reading_pos.append(seq[i:])
    all_reading_pos.append(c_seq[i:])
    


# In[98]:


#je créer toutes les séquences traduite. Je remplace 'Stop' par X pour pouvoir parcourir plus facilement mes protéines ensuite.  
all_prot = []
for i in all_reading_pos:
    all_prot.append(dna_to_prot(i).replace("Stop","X"))


# In[100]:


#Je créer une fonction me permettant d'écrire les protéines commançant par une méthionine et finissant par X 

def find_poss_seq(Prots):
    #Je vais utiliser une liste qui index les codons start et une liste qui index les codons stop. 
    all_start = []
    all_stop = []
    

    for i, j in enumerate(Prots):
        if j == "M" : 
            all_start.append(i)
        if j == "X":
            all_stop.append(i)
            
    #Je print toutes résultats sauf si il y a un codon stop dedans. 
    for i in all_start : 
        a = Prots[i]
        for j in all_stop:
            if i < j :
                sous_result = Prots[i:j]
                if ("X" in sous_result) == False:
                    print(sous_result)


# In[101]:


#J'applique ma fonction sur toutes les séquences possible. Attention je dois retirer les doublons.
for i in all_prot:
   find_poss_seq(i)

