# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 20:33:51 2021

@author: ASUS
"""
import base64
import binascii
x="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
y=binascii.unhexlify(x)
print(base64.b64encode(y))