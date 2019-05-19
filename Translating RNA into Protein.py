#!/usr/bin/env python
# coding: utf-8

# Probability is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a random variable, which is simply a variable that can take a number of different distinct outcomes depending on the result of an underlying random process.
# 
# For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X
# represent the random variable corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by Pr(X=red)=35 and Pr(X=blue)=25
# 
# .
# 
# Random variables can be combined to yield new random variables. Returning to the ball example, let Y
# model the color of a second ball drawn from the bag (without replacing the first ball). The probability of Y being red depends on whether the first ball was red or blue. To represent all outcomes of X and Y, we therefore use a probability tree diagram. This branching diagram represents all possible individual probabilities for X and Y
# 
# , with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of probabilities along the path from the beginning of the tree; see Figure 2 for an illustrative example.
# 
# An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A
# be the event "Y is blue." Pr(A) is equal to the sum of the probabilities of two different outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 310+110=25
# 
# (see Figure 2 above).
# 
# Given: Three positive integers k
# , m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n
# 
# are homozygous recessive.
# 
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# In[87]:


codon_table = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G """


# In[90]:


#je split la table des codon puis je stock dans deux listes distinctes les codons et les acides aminés, puis je zip tout dans un dictionnaire.
t = condon_table.split()

codon = []
aa = []

for i,j in enumerate(t):
    if i % 2 == 0 :
        codon.append(j)
    if i % 2 != 0 :
        aa.append(j)
        
d = dict(zip(codon, aa))        


# In[100]:


seq = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
result = ""

#Je prend que les triplets qui code avec le modulo 3, je break si c'est un codon stop, sinon j'écris mon résultat 
for i in range(len(seq)) :
        
    if i % 3 == 0: 
        
        if d[seq[i:i+3]] == 'Stop':
            
            break
        
        else : 
            result += d[seq[i:i+3]]
result       


# In[ ]:




