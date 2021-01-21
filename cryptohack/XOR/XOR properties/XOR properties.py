from pwn import xor
import binascii

key1 =  binascii.unhexlify("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key23 = binascii.unhexlify("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
ciphertext = binascii.unhexlify("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
key = xor(key1,key23)
plaintext = xor(key,ciphertext)
print(plaintext.decode("ASCII"))
