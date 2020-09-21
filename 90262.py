# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:41:32 2020

@author: cis-user
"""

string="I love you"
res=string.split(" ")
print(res)

##############################
string2=string[::-1]
res=string2.split(" ")
print(res)

##############################
stringso="so "
stringmuch="much"
print(string,stringso*100,stringmuch)

##############################
import random
a=random.randint(1, 100)
print(string,stringso*a,stringmuch)