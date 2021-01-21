# Encoding

## Base64

Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using 64 characters. One character of a Base64 string encodes 6 bits, and so 4 characters of Base64 encodes three 8-bit bytes.

Base64 is most commonly used online, where binary data such as images can be easy included into html or css files.

Take the below hex string, decode it into bytes and then encode it into Base64.

```
72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf
```

### Solving

We have to first decode the given string to bytes and then encode it with base64. Which we can do with

```python
import base64

hexstr="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
flag=bytearray.fromhex(hexstr)
print(base64.b64encode(flag))
```

Which will give the flag 

#### Flag

**crypto/Base+64+Encoding+is+Web+Safe/**


