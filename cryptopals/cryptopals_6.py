# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:55:37 2021

@author: ASUS
"""
from pwn import xor
import base64

frequency ={"a":8.34,"b":1.54,"c":2.73,"d":4.14,"e":12.60,"f":2.03 ,"g":1.92 ,"h":6.11 ,"i":6.71 ,"j":0.23 ,"k":0.87 ,"l":4.24,"m":2.53,"n":6.80,"o":7.70,"p":1.66,"q":0.09,"r":5.68,"s":6.11,"t":9.37,"u":2.85,"v":1.06,"w":2.34,"x":0.20,"y":2.04,"z":0.06}

def hamming(a,b):
    count=0
    for i in xor(a,b):
        for j in bin(i):
            if (j=='1'):
                count+=1
    return count

def score(what):
    score=0
    for i in what:
        if (ord(i) in range(97,123) ):
            score+=frequency[i]
        elif(ord(i) in range(65,91) ):
            score+=(frequency[i.lower()]*0.75)
        elif(i!=' '):
            score*=0.95
    return score

print(hamming("this is a test","wokka wokka!!!"))
mini=9999999
text = open("6.txt","r")
cipher=base64.b64decode(text.read())
for i in range(2,40):
    dist=0
    for j in range(1,int(len(cipher)/i+1)):
        dist+=hamming(cipher[0:i*j],cipher[i:i*j])
        dist/=len(cipher)
    if(dist<=mini):
        mini=dist
        leng=i
key=''
print(mini,leng)
for i in range(0,leng):
    maxi=0
    y=cipher[i::leng]
    for j in range(0,128):
        plain=''
        for k in y:
            plain+=chr(k^j)
        if(score(plain)>maxi):
            maxi=score(plain)
            plaintext=j
    key+=chr(plaintext)
for i in range(0,len(cipher)):
    print(chr(cipher[i]^ord(key[i%29])),end='')