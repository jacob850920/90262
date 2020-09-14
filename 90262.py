# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:09:30 2020

@author: cis-user
"""

print("解ax**2+bx+c=0")
print("請輸入a,b,c值:")
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=(b**2)-(4*a*c)
x=(-b-d**0.5)/(2*a)
y=(-b+d**0.5)/(2*a)
print("ax**2+bx+c=0的解為:" )
print(x,y)

