# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 08:15:05 2020

@author: cis-user
"""

l1 = [1,2,3,4,5]
l2 = [6,5,4,3,2]
l3=[]
for x in range(len(l1)):
    if l1[x]>l2[x]:
        l3.append(l1[x])
    else:
        l3.append(l2[x])

        
print(l3)        
#####################
l1 = [1,2,3,4,5]
l2 = [6,5,4,3,2]
l3 = [False,False,True,False,True]
l4=[]
for i in range(len(l3)):
    if l3[i]== True:
        l4.append(l1[i])
    else:
        l4.append(l2[i])
print(l4)