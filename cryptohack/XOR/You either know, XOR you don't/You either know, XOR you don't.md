## You either know, XOR you don't

I've encrypted the flag with my secret key, you'll never be able to guess it.

Remember the flag format and how it might help you in this challenge!

```
0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
```



### Solving

The question says to remember the flag format. We know that the flag starts with "crypto{".

Xoring it with the first part of the ciphertext gives us the first part of key

We know that the key ends with "}". So xoring it with the last character of the ciphertext will give us the last part of key

So we can find the key using:

 

```python
hexstr = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
ciphertext = bytearray.fromhex(hexstr)
partflag= b"crypto{"
key =''
flag=''
for i in range(0,7):
    key += chr(ciphertext[i]^partflag[i])
key += chr(ciphertext[-1]^ord("}"))
print(key)
```

It will give the key as:

**myXORkey**

Now we can repeat the key to make the same length as of the ciphertext and xor it again to get the flag:

```python
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
```

It will give the flag as:

**crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}**