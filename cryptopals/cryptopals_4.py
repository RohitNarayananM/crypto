# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:10:10 2021

@author: ASUS
"""
import binascii

frequency ={"a":8.34,"b":1.54,"c":2.73,"d":4.14,"e":12.60,"f":2.03 ,"g":1.92 ,"h":6.11 ,"i":6.71 ,"j":0.23 ,"k":0.87 ,"l":4.24,"m":2.53,"n":6.80,"o":7.70,"p":1.66,"q":0.09,"r":5.68,"s":6.11,"t":9.37,"u":2.85,"v":1.06,"w":2.34,"x":0.20,"y":2.04,"z":0.06}
text = open("4.txt",'r')

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
max=0
for i in text:
    y=binascii.unhexlify(i.strip())
    for i in range(0,128):
        plain=''
        for j in y:
            plain+=chr(j^i)
        if(score(plain)>max):
            max=score(plain)
            plaintext=plain
            key=chr(i)
            ciphertext=y
        
print("Key:",key,"\nPlaintext:",plaintext,"\nCiphertext:",ciphertext)

