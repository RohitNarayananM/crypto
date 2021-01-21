# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 20:41:46 2021

@author: ASUS
"""
import base64
import binascii

plain=''
result='746865206b696420646f6e277420706c6179'
x='1c0111001f010100061a024b53535009181c'
y=binascii.unhexlify(x)
print(y)
a= '686974207468652062756c6c277320657965'
b=binascii.unhexlify(a)
print(b)
for i in range (len(y)):
    plain+=(chr(y[i]^b[i]))
print(plain)
print(plain.encode("utf-8").hex())
print(result==(plain.encode("utf-8").hex()))