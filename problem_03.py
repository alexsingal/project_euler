# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:16:18 2016

@author: alexsingal
"""
from math import sqrt 
def eratosthenes(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))
 
primes = list(eratosthenes(int(sqrt(600851475143))))

i = -1

while True:
    if 600851475143 % primes[i] == 0:
        break
    else:
        i -= 1
        
print primes[i]
    
