# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 20:15:49 2021

@author: ASUS
"""
import binascii 

hexstr="63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(binascii.unhexlify(hexstr))