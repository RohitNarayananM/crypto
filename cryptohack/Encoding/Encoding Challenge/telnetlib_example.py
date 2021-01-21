import telnetlib
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import binascii

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

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
        decoded = encoded.decode("utf-8")
        
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