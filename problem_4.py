# -*- coding: utf-8 -*-
"""
Created on Thu May 19 12:53:49 2016

@author: alexsingal
"""
from math import sqrt

#Create palindromes (with an even number of digits)
def makePals(numList):
    return [int(str(i)+str(i)[::-1]) for i in numList]
    
def factors(n):
    results = set()
    for i in xrange(1, int(sqrt(n)) + 1):
        if n % i == 0:
            results.add(i)
            results.add(int(n/i))
    return sorted(list(results))
    
pals = makePals(range(100,1000))

while True:
    factList = factors(pals[-1])
    nFacts = len(factList)
    if len(str(factList[nFacts/2])) == 3 and len(str(factList[(nFacts/2)-1])) == 3: #the middle two factors
        print pals[-1]
        break
    else:
        pals.pop()