# Encoding

## Hex

When we encrypt something the resulting ciphertext commonly has bytes which are not printable ASCII characters. If we want to share our encrypted data, it's common to encode it into something more user-friendly and portable across different systems.

Included below is a the flag encoded as a hex string. Decode this back into bytes to get the flag.

```
63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d
```

### Solving

Here we are given a hex encoded string and we have to convert it back to bytes. We can use

unhexlify of binascii todo this

```python
import binascii 

hexstr="63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(binascii.unhexlify(hexstr))
```

Which will give the flag

#### Flag

**crypto{You_will_be_working_with_hex_strings_a_lot}**

**4ll_7h3_w4y_d0wn}**