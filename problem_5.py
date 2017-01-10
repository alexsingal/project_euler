# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:29:33 2016

@author: alexsingal
"""

from __future__ import division

factors = [11,13,16,17,19] #Checking any other factors is redundant

test = 2520 #the first number divisible by 1-10

while True:
    hits = 0
    for i in factors:
        if test/i == int(test/i):
            hits += 1
        else:
            break
    if hits == 5:
        print test
        break
    else:
        test += 2520

