#!/usr/bin/env python
# coding: utf-8
#Problem

#Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2

#and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

#Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

#Given: Positive integers n≤100
#and m≤20
#
.

#Return: The total number of pairs of rabbits that will remain after the n
#-th month if all rabbits live for m months.
# In[11]:


def fibonacciRabbits(n, m):
    F = [0, 1, 1]
    for i in range(3, n + 1):
        if i <= m:
            total = F[i - 1] + F[i - 2]
        elif i == m + 1:
            total = F[i - 1] + F[i - 2] - 1
        else:
            total = F[i - 1] + F[i - 2] - F[i - m - 1]
        F.append(total)
    return F


# In[12]:


fibonacciRabbits(95, 17)[-1]






