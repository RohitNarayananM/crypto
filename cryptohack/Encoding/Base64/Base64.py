# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 20:16:54 2021

@author: ASUS
"""
import base64

hexstr="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
flag=bytearray.fromhex(hexstr)
print(base64.b64encode(flag))