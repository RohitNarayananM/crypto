# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:55:11 2021

@author: ASUS
"""
import binascii

text=open("8.txt","r")
cipher=[]
for line in text:
    cipher+=[binascii.unhexlify(line.strip())]
for i in cipher:
    for j in range(0,int(len(i)/16)):
        for k in range(j,int(len(i)/16)):
            if(i[j*16:(j+1)*16]==i[(k+1)*16:(k+2)*16]):
                encrypted=i
print(encrypted)