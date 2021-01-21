# Encoding

## Encoding Challenge

Now you've got the hang of the various encodings you'll be encountering, let's have a look at automating it.

Can you pass all 100 levels to get the flag?

The *13377.py* file attached below is the source code for what's running on the server. The *pwntools_example.py* file provides the start of a solution using the incredibly convenient pwntools library. which you can use if you like. pwntools however is incompatible with Windows, so *telnetlib_example.py* is also provided.

For more information about connecting to interactive challenges, see the [FAQ](https://cryptohack.org/faq#netcat). Feel free to skip ahead to the cryptography if you aren't in the mood for a coding challenge!

Connect at `nc socket.cryptohack.org 13377`

### Solving

Here we are given 13777.py file which is the source code for what is running the in the server. We can take a look at the file to understand what is happening there.

```python
from Crypto.Util.number import bytes_to_long, long_to_bytes
from utils import listener # this is cryptohack's server-side module and not part of python
import base64
import codecs
import random

FLAG = "crypto{????????????????????}"
ENCODINGS = [
    "base64",
    "hex",
    "rot13",
    "bigint",
    "utf-8",
]
with open('/usr/share/dict/words') as f:
    WORDS = [line.strip().replace("'", "") for line in f.readlines()]


class Challenge():
    def __init__(self):
        self.challenge_words = ""
        self.stage = 0

    def create_level(self):
        self.stage += 1
        self.challenge_words = "_".join(random.choices(WORDS, k=3))
        encoding = random.choice(ENCODINGS)

        if encoding == "base64":
            encoded = base64.b64encode(self.challenge_words.encode()).decode() # wow so encode
        elif encoding == "hex":
            encoded = self.challenge_words.encode().hex()
        elif encoding == "rot13":
            encoded = codecs.encode(self.challenge_words, 'rot_13')
        elif encoding == "bigint":
            encoded = hex(bytes_to_long(self.challenge_words.encode()))
        elif encoding == "utf-8":
            encoded = [ord(b) for b in self.challenge_words]

        return {"type": encoding, "encoded": encoded}

    #
    # This challenge function is called on your input, which must be JSON
    # encoded
    #
    def challenge(self, your_input):
        if self.stage == 0:
            return self.create_level()
        elif self.stage == 100:
            self.exit = True
            return {"flag": FLAG}

        if self.challenge_words == your_input["decoded"]:
            return self.create_level()

        return {"error": "Decoding fail"}


listener.start_server(port=13377)
```



So when we connect to the server the server  will give us to values. An encoded ciphertext and the type of encoding. So we have to decode it  and send it back. We will have to repeat the process 100 times to get the flag.

The type of encoding will be randomly selected each time. So first we have to find a way to decode all these types of encoding.

There are 6 types of encryption:



for base64 we can use:

```python
decoded = base64.b64decode(encoded).decode("utf-8")
```

for hex:

```python
decoded = binascii.unhexlify(encoded).decode("utf-8")
```

for rot13 : 

```python
decoded = codecs.decode(encoded,'rot_13')
```

for bigint:

```python
decoded = long_to_bytes(int(encoded,0)).decode("utf-8")
```

for utf-8 :

```python
decoded = ''
for i in encoded:
    decoded+= chr(i)
```

We can now make this as a function and use a loop to do it 100 times. WE can use this code inside the pwntools example or telnetlib example to get the flag:

pwntools

```python
from pwn import * # pip install pwntools
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import binascii

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def challenge(type,encoded):

    if type == "base64":
        decoded = base64.b64decode(encoded).decode("utf-8") # wow so encode
    elif type == "hex":
        decoded = binascii.unhexlify(encoded).decode("utf-8")
    elif type == "rot13":
        decoded = codecs.decode(encoded,'rot_13')
    elif type == "bigint":
        decoded = long_to_bytes(int(encoded,0)).decode("utf-8")
    elif type == "utf-8":
        decoded = ''
        for i in encoded:
            decoded+= chr(i)
    print(decoded)
    return decoded

for i in range (100):
    received = json_recv()
    
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    
    to_send = {"decoded": challenge(received["type"],received["encoded"])}
    json_send(to_send)
    

received = json_recv()
print(received["flag"])
```

This will give us the flag

## Flag

**crypto{3nc0d3_d3c0d3_3nc0d3}**

