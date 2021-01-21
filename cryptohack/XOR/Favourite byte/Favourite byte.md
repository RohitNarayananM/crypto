## Favourite byte

I've hidden my data using XOR with a single byte. Don't forget to decode from hex first.

```
73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
```



### Solving

It is a single byte xor. So we can just xor each character in the string with the first 128 characters. But it will give 128 strings. As we know the format of the flag, we can check each with first 7 characters of flag and print the flag

```python
hexstr = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
ciphertext = bytearray.fromhex(hexstr)
print(ciphertext)
for i in range(0,128):
    can=''
    for j in ciphertext:
        can+=chr(j^i)
    if (can[0:7]=="crypto{"):
        print(i,can)
```

It will give the flag

### Flag

**crypto{0x10_15_my_f4v0ur173_by7e}**