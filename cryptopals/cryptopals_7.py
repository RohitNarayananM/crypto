# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:34:45 2021

@author: ASUS
"""

import base64
from Crypto.Cipher import AES

text=open("7.txt","r").read()
text=base64.b64decode(text)

key=b"YELLOW SUBMARINE"
cipher=AES.new(key,AES.MODE_ECB)
print(cipher.decrypt(text).decode())