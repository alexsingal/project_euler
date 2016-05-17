# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:11:27 2016

@author: alexsingal
"""

fib = [1, 2]

while True:
    if fib[-1] + fib[-2] < 4000000:
        fib.append(fib[-1] + fib[-2])
    else:
        break
    
print sum([i for i in fib if i % 2 == 0])