hexstr = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
ciphertext = bytearray.fromhex(hexstr)
print(ciphertext)
for i in range(0,128):
    can=''
    for j in ciphertext:
        can+=chr(j^i)
    if (can[0:7]=="crypto{"):
        print(i,can)