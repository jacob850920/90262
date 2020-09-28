# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:45:14 2020

@author: cis-user
"""
print("1.")
score=['小徐',5,9,6,8,7,10,6]
a=score[1:]
print("(1)",max(a))
print("(2)",min(a))
score_min=sorted(a)
score_max=score_min[::-1]
print("(3)",score_max[0],score_max[1],score_max[2])
print("(4)",score_min[0],score_min[1],score_min[2])
print("(5)",sum(a)/len(a))

print("2.")
for x in range(1,10):
     for y in range(1,10):
         print("%d*%d=%2d" % (x,y,x*y),end=" ")
     print(" ")

print("3.")
import random
a="I love you"
c="much"
print(a,end=" ")
for b in range(random.randint(1, 100)):
    b="so"
    print(b,end=" ")
print(c)

