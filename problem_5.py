# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:29:33 2016

@author: alexsingal
"""

from __future__ import division

factors = [11,13,14,16,17,18,19,20] #Checking any other factors is redundant

test = 2520 #the first number divisible by 1-10

while True:
    its = 0
    for i in factors:
        if test/i == int(test/i):
            its += 1
        else:
            break
    if its == 8:
        print test
        break
    else:
        test += 2520
        