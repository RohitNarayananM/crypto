hexstr = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
ciphertext = bytearray.fromhex(hexstr)
partflag= b"crypto{"
key =''
flag=''
for i in range(0,7):
    key += chr(ciphertext[i]^partflag[i])
key += chr(ciphertext[-1]^ord("}"))
print(key)
for i in range(0,len(ciphertext)):
    flag += chr(ciphertext[i]^ord(key[i%8]))
print(flag)
