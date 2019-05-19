#!/usr/bin/env python
# coding: utf-8

# Problem
# For positive integers a and n, a modulo n (written amodn in shorthand) is the remainder when a is divided by n. For example, 29mod11=7 because 29=11×2+7.
# 
# Modular arithmetic is the study of addition, subtraction, multiplication, and division with respect to the modulo operation. We say that a and b are congruent modulo n if amodn=bmodn; in this case, we use the notation a≡bmodn.
# 
# Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn, then a+c≡b+dmodn and a×c≡b×dmodn. To check your understanding of these rules, you may wish to verify these relationships for a=29, b=73, c=10, d=32, and n=11.
# 
# As you will see in this exercise, some Rosalind problems will ask for a (very large) integer solution modulo a smaller number to avoid the computational pitfalls that arise with storing such large numbers.
# 
# Given: A protein string of length at most 1000 aa.
# 
# Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

# In[21]:


trans_table = """UUU F      CUU L      AUU I      GUU V
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

a = trans_table.split()
seq = "MWFWTGYCHTENFMDTKRTSQEDIAAMDRDDEIDPFDMSGTDLFATQRCGKTLYWTWKSAHYPQMHLYNYFSYWFNDDYHPKWHRELVDPVTQSHGQMVNENWKQRPDDEEDPVLWYVQEYDYLRCHGNEMHWDCEDYQDIHIHMTSMSIESQWRENCNWCAPVQQLWCPAMPAAICAIIGAWWLWKMQNYGAPNQHQYKNGRKFPDPACAKIYRKAHSYHPDKSKYMGSASRCQLVHSIEIDLSREDNSCPDGPPQDVTVMWCKNLISNGGAECAPIFVTRTGDLGSMLECETWKWDMNNQHTHNKAKHTDEALDWGGNQFQVFLPERKVATSEYPCVQHDTIFRQNVGHNQTKGDVWYRVWPIPWMNKAGCSHQPNIKFSQMWYMAQRDFRVSMLKNIGGIEKKIYLGTADHIEDSDFDGEIMTQTVFLHQLVWQNIRYYTTKPEPCAQPDGQTPFEHWLDKVWWKMCSWGKGGFQQYNGQSYCFLFGNQIQTSKDIKPIVHWIVNKTMYHFFGLEGFLLQEVNKPPNWVHHFIEPIVHVGLWMIFQMFEHIFWVYPCSTVTHQDAHFWVSWDYNSDIYVCTGARQNHHGPACSNPHPECIDIFEWIPWPNKQDLWFQFHCYTMICFVEHVLITCVIDTMQYFSRCTDMHTEMGDDPRPWHDNDFNEDTPCYEGLPHQLMLLRPRDVWEHSIGSFPYIFESPDVGLMLYKVSMMNLMVRITDQWIEAPSHDCRILLLFAKYGVHEIEMIIVAEPDLCFIRSQVTLQDMWGFYEYSFIRWSDCHTIFPCNCIMVSCQQIWPYFSMDEVSRRMWLAVSMEAQTPHMNSNPTLPRRGCIAIGSQAKGNCPVTRFATAAKWLQFPCEWNQSDSMMKNSAKIMEYAEFMMIKTQVIPEENGFTQNTFYVYADWLDDHSVGQEEPFCPGFSFTDFDIPSNDHWKYNFTKEGGAQVFPRMRFAADASCSIKDQIRQEVEDDNMEKPFNRQSDKWVKWGPCMF"


# In[22]:


#Je créer une liste des acides aminés et je compte le nombre de leurs apparitions dans un dictionnaire d. 
aa = []
d = {}

for i in a :
    if len(i) == 1:
        aa.append(i)
        
for i in aa : 
    d[i] = a.count(i)


# In[23]:


#je créer une liste : chaque élément est le nombre de possiblités pour l'acide aminé. Attention : à la fin de cette liste, j'ajoute 3 car il y a 3 codons stop possible
s = []

for i in seq : 
    s.append(d[i])

s.append(3)

#Je n'ai plus qu'a multiplier les valeurs entres elle modulo 1000000

r = 1
for element in s :
    r *= element
    
print(r%1000000)

