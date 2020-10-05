# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 07:55:47 2020

@author: cis-user
"""

v="Simon Peter John"
z=v.split(' ')
z1=z[0]
z2=z[1]
z3=z[2]
b1=(z1[0][0])
b2=(z2[0][0])
b3=(z3[0][0])

a1=["*"for i in z1[1:]]
s1="".join(a1)

a2=["*"for i in z2[1:]]
s2="".join(a2)

a3=["*"for i in z3[1:]]
s3="".join(a3)

y=[]
y.append(b1+s1)
y.append(b2+s2)
y.append(b3+s3)
print(y)

#####################################################
word=['Company 1','Company 2','Company 3']
word1=word[0]
word10=word1.replace(" ", "_")

word2=word[1]
word20=word2.replace(" ", "_")

word3=word[2]
word30=word3.replace(" ", "_")

nword=[]
nword.append(word10)
nword.append(word20)
nword.append(word30)

print(nword)
#######################################################
list1=[1,2,3,4,5,6]
list2=[]
for i in list1:
    list2.append(str(i)+"$")
print(list2)

########################################################
list3=[]
for i in list2:
    list3.append(str(i).replace("$", ""))
print(list3)

########################################################

list1=[1,2,3,4]
list2=[5,6,7,8]
print(list(zip(list1,list2)))

##########################################################

s='I love you and you love him and who loves who'
a=s.split(' ')
print(a)

#############################################################
b=set(a)
keys=b
values=[0 for i in b]
d={key: value for key,value in zip(keys,values)}
print(d)
#############################################################

for i in a:
    d[i] += 1
print(d)



















