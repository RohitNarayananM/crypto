# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:09:53 2021

@author: ASUS
"""
import binascii

x=b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
y=binascii.unhexlify(x)

frequency ={"a":8.34,"b":1.54,"c":2.73,"d":4.14,"e":12.60,"f":2.03 ,"g":1.92 ,"h":6.11 ,"i":6.71 ,"j":0.23 ,"k":0.87 ,"l":4.24,"m":2.53,"n":6.80,"o":7.70,"p":1.66,"q":0.09,"r":5.68,"s":6.11,"t":9.37,"u":2.85,"v":1.06,"w":2.34,"x":0.20,"y":2.04,"z":0.06}
def score(what):
    score=0
    for i in what:
        if (ord(i) in range(97,123) ):
            score+=frequency[i]
        elif(i.isupper()):
            score+=(frequency[i.lower()]*0.75)
        elif(i!=' '):
            score*=0.95
    return score
max=0
for i in range(0,128):
    plain=''
    for j in y:
        plain+=chr(j^i)
    if(score(plain)>max):
        max=score(plain)
        plaintext=plain
        key=chr(i)
        
print(key,plaintext)
