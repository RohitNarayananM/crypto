## XOR Properties

In the last challenge, you saw how XOR worked at the level of bits. In this one, we're going to cover the properties of the XOR operation and then use them to undo a chain of operations that have encrypted a flag. Gaining an intuition for how this works will help greatly when you come to attacking real cryptosystems later, especially in the block ciphers category.

There are four main properties we should consider when we solve challenges using the XOR operator

```
Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0
```

Let's break this down. Commutative means that the order of the XOR operations is not important. Associative means that a chain of operations can be carried out without order (we do not need to worry about brackets). The identity is 0, so XOR with 0 "does nothing", and lastly something XOR'd with itself returns zero.

Let's try this out in action! Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag.

```
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
```

 Before you XOR these objects, be sure to decode from hex to bytes. If you have `pwntools` installed, you have a xor function for byte strings: `from pwn import xor`

### Solving

Here we first have to decode the given strings from hex to bytes. We can do that with binascii.unhexlify(string)

Then we can get the the key by xoring 1st and 3rd string which is

```
KEY1 ^ KEY2 ^ KEY3
```

Now that we have the key and ciphertext we can get the plain text by xoring these two

```python
from pwn import xor
import binascii

key1 =  binascii.unhexlify("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key23 = binascii.unhexlify("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
ciphertext = binascii.unhexlify("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
key = xor(key1,key23)
plaintext = xor(key,ciphertext)
print(plaintext.decode("ASCII"))
```

It will give us the flag:

### Flag

**crypto{x0r_i5_ass0c1at1v3}**