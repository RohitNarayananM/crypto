## Introduction

### Finding Flags

Each challenge is designed to help introduce you to a new piece of cryptography. Solving a challenge will require you to find a "flag".These flags will usually be in the format `crypto{y0ur_f1rst_fl4g}`. The flag format helps you verify that you found the correct solution.

Try submitting this into the form below to solve your first challenge.

##### Flag

**crypto{y0ur_f1rst_fl4g}**



### Great snakes

Modern cryptography involves code, and code involves coding. CryptoHack provides a good opportunity to sharpen your skills. Of all modern programming languages, Python 3 stands out as ideal for quickly writing cryptographic scripts and attacks. For more information about why we think Python is so great for this, please see the [FAQ](https://cryptohack.org/faq#python3).

Run the attached Python script and it will output your flag.

#### Solving

Here we are given a python file and when we run the script we will get the flag.

```python
import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))
```

##### Flag

**crypto{z3n_0f_pyth0n}**



### Network attacks

Several of the challenges are dynamic and require you to talk to our challenge servers over the network. This allows you to perform man-in-the-middle attacks on people trying to communicate, or directly attack a vulnerable service. To keep things consistent, our interactive servers always send and receive JSON objects.

Python makes such network communication easy with the `telnetlib` module. Conveniently, it's part of Python's standard library, so let's use it for now.

For this challenge, connect to `socket.cryptohack.org` on port `11112`. Send a JSON object with the key `buy` and value `flag`.

The example script below contains the beginnings of a solution for you to modify, and you can reuse it for later challenges.

Connect at `nc socket.cryptohack.org 11112`

#### Solving

Here we are given a python script. 

```python
#!/usr/bin/env python3

import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 11112

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


print(readline())
print(readline())
print(readline())
print(readline())


request = {
    "buy": "clothes"
}
json_send(request)

response = json_recv()

print(response)
```

We have to connect to `socket.cryptohack.org` on port `11112`. Send a JSON object with the key `buy` and value `flag`. The value is given as clothes in the code.

 We can change **"clothes"** to **"flag"** and get the flag

##### Flag

**crypto{sh0pp1ng_f0r_fl4g5}**