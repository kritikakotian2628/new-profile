# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:56:26 2020

@author: kritika
"""
import re 
hand = open('regex_sum_396479.txt')
sum = 0
for line in hand:
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    for i in y:
        sum = sum + int(i)
print(sum)