# Cryptopals - set1

This is the **qualifying set**. We picked the exercises in it to ramp developers up gradually into coding cryptography, but also to verify that we were working with people who were ready to write code.

This set is **relatively easy**. With one exception, most of these exercises should take only a couple minutes. But don't beat yourself up if it takes longer than that. It took Alex two weeks to get through the set!

If you've written any crypto code in the past, you're going to feel like skipping a lot of this. **Don't skip them**. At least two of them (we won't say which) are important stepping stones to later attacks.

1. [Convert hex to base64](https://cryptopals.com/sets/1/challenges/1)
2. [Fixed XOR](https://cryptopals.com/sets/1/challenges/2)
3. [Single-byte XOR cipher](https://cryptopals.com/sets/1/challenges/3)
4. [Detect single-character XOR](https://cryptopals.com/sets/1/challenges/4)
5. [Implement repeating-key XOR](https://cryptopals.com/sets/1/challenges/5)
6. [Break repeating-key XOR](https://cryptopals.com/sets/1/challenges/6)
7. [AES in ECB mode](https://cryptopals.com/sets/1/challenges/7)
8. [Detect AES in ECB mode](https://cryptopals.com/sets/1/challenges/8)

###  1. Convert hex to base64

The string:

```
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
```

Should produce:

```
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
```

So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

#### Solving

Here we are given a hex encoded string ad we have to convert it to base64 encoding

First we have to decode it form hex using binascii library and then encode it using base64. For that we have the base64 library in python:

```python
import base64
import binascii
x="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
y=binascii.unhexlify(x)
print(base64.b64encode(y))
```

### 2. Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

```
1c0111001f010100061a024b53535009181c
```

... after hex decoding, and when XOR'd against:

```
686974207468652062756c6c277320657965
```

... should produce:

```
746865206b696420646f6e277420706c6179
```

#### Solving

Here we have to first decode the given hex strings and then xor them. We can use `binascii` to decode hex and then xor each character of the first string with the second string. Python has a built in operator for bitwise xor `^` but it operates on integers

So we have to convert characters to their corresponding unicode numbers and then xor them and then convert them back to characters.

```python
import base64
import binascii

plain=''
result='746865206b696420646f6e277420706c6179'
x='1c0111001f010100061a024b53535009181c'
y=binascii.unhexlify(x)
a= '686974207468652062756c6c277320657965'
b=binascii.unhexlify(a)
for i in range (len(y)):
    plain+=(chr(y[i]^b[i]))
print(plain)
print(plain.encode("utf-8").hex())
print(result==(plain.encode("utf-8").hex()))
```

### 3. Single-byte XOR cipher

The hex encoded string:

```
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
```

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

```
Achievement Unlocked

You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.
```

#### Solving

This is a single byte xor. Every character of the cipher text is xored with the same byte. So we can just xor the cipher text with all 256 possible bytes and one of them will give us the key.

But it is hard to find key from 256 outputs so we have to score each xored text and only print the string with highest score.

There is a certain frequency of letters in english language. It represents the average number of a letter in an english sentence. We can use this to score the ciphertext.

```python
import binascii

x=b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
y=binascii.unhexlify(x)

frequency ={"a":8.34,"b":1.54,"c":2.73,"d":4.14,"e":12.60,"f":2.03 ,"g":1.92 ,"h":6.11 ,"i":6.71 ,"j":0.23 ,"k":0.87 ,"l":4.24,"m":2.53,"n":6.80,"o":7.70,"p":1.66,"q":0.09,"r":5.68,"s":6.11,"t":9.37,"u":2.85,"v":1.06,"w":2.34,"x":0.20,"y":2.04,"z":0.06}
def score(what):
    score=0
    for i in what:
        if (ord(i) in range(97,123) ):
            score+=frequency[i]
        elif(i.isupper()):
            score+=(frequency[i.lower()]*0.75)
        elif(i!=' '):
            score*=0.95
    return score
max=0
for i in range(0,128):
    plain=''
    for j in y:
        plain+=chr(j^i)
    if(score(plain)>max):
        max=score(plain)
        plaintext=plain
        key=chr(i)
        
print(key,plaintext)
```

**We get the key as "X" and ciphertext : "Cooking MC's like a pound of bacon"**

### 4. Detect single-character XOR

One of the 60-character strings in [this file](https://cryptopals.com/static/challenge-data/4.txt) has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)

#### Solving

Now we have to detect single byte xor. we are given a file with many strings. We can xor all the strings in the file with all possible bytes and then score the output using our code from the previous challenge. Then we can print the one with highest score 

```python
import binascii

frequency ={"a":8.34,"b":1.54,"c":2.73,"d":4.14,"e":12.60,"f":2.03 ,"g":1.92 ,"h":6.11 ,"i":6.71 ,"j":0.23 ,"k":0.87 ,"l":4.24,"m":2.53,"n":6.80,"o":7.70,"p":1.66,"q":0.09,"r":5.68,"s":6.11,"t":9.37,"u":2.85,"v":1.06,"w":2.34,"x":0.20,"y":2.04,"z":0.06}
text = open("4.txt",'r')

def score(what):
    score=0
    for i in what:
        if (ord(i) in range(97,123) ):
            score+=frequency[i]
        elif(ord(i) in range(65,91) ):
            score+=(frequency[i.lower()]*0.75)
        elif(i!=' '):
            score*=0.95
    return score
max=0
for i in text:
    y=binascii.unhexlify(i.strip())
    for i in range(0,128):
        plain=''
        for j in y:
            plain+=chr(j^i)
        if(score(plain)>max):
            max=score(plain)
            plaintext=plain
            key=chr(i)
            ciphertext=y
        
print("Key:",key,"\nPlaintext:",plaintext,"\nCiphertext:",ciphertext)
```

It will give us

**Key: 5** 
**Plaintext: Now that the party is jumping**

**Ciphertext: b'{ZB\x15A]TA\x15A]P\x15ETGAL\x15\\F\x15_@XE\\[R?'**

### 5. Implement repeating-key XOR

Here is the opening stanza of an important work of the English language:

```
Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal
```

Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.

It should come out to:

```
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
```

Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this.

#### Solving

Here we are implementing repeating key XOR. We have to use the key 'ICE' repeatedly to XOR the plaintext 

WE can do it with the follwing code :

```python
import binascii

plain = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
cipher=b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
key=b'ICE'
check=''
for i in range(len(plain)):
    check+=chr(plain[i]^key[i%3])

check=binascii.hexlify(check.encode())
print(plain)
print(check)
print(cipher==check)
```

### 6. Break repeating-key XOR

It is officially on, now.

This challenge isn't conceptually hard, but it involves actual error-prone coding. The other challenges in this set are there to bring you up to speed. This one is there to **qualify** you. If you can do this one, you're probably just fine up to Set 6.

[There's a file here.](https://cryptopals.com/static/challenge-data/6.txt) It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

1. Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

2. Write a function to compute the edit distance/Hamming distance between two strings.

    

   The Hamming distance is just the number of differing bits.

    

   The distance between:

   ```
   this is a test
   ```

   and

   ```
   wokka wokka!!!
   ```

   is 37. Make sure your code agrees before you proceed.

3. For each KEYSIZE, take the *first* KEYSIZE worth of bytes, and the *second* KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.

4. The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.

5. Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.

6. Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.

7. Solve each block as if it was single-character XOR. You already have code to do this.

8. For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.

This code is going to turn out to be surprisingly useful later on. Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing. But more people "know how" to break it than can *actually break it*, and a similar technique breaks something much more important.

```
No, that's not a mistake.

We get more tech support questions for this challenge than any of the other ones. We promise, there aren't any blatant errors in this text. In particular: the "wokka wokka!!!" edit distance really is 37.
```

#### Solving

Here we have to break repeating key XOR. 

First we have to find hamming distance which can be calculated using :

```python
def hamming(a,b):
    count=0
    for i in xor(a,b):
        for j in bin(i):
            if (j=='1'):
                count+=1
    return count
```

Now we can find the key length with lowest hamming length using :

```python
print(hamming("this is a test","wokka wokka!!!"))
mini=9999999
text = open("6.txt","r")
cipher=base64.b64decode(text.read())
for i in range(2,40):
    dist=0
    for j in range(1,int(len(cipher)/i+1)):
        dist+=hamming(cipher[0:i*j],cipher[i:i*j])
        dist/=len(cipher)
    if(dist<=mini):
        mini=dist
        leng=i
print(mini,leng)
```

It will give the key length as **29**

Now we can divide the plaintext into 29 parts and solve each as a single byte xor and th whole program is:

```python
from pwn import xor
import base64

frequency ={"a":8.34,"b":1.54,"c":2.73,"d":4.14,"e":12.60,"f":2.03 ,"g":1.92 ,"h":6.11 ,"i":6.71 ,"j":0.23 ,"k":0.87 ,"l":4.24,"m":2.53,"n":6.80,"o":7.70,"p":1.66,"q":0.09,"r":5.68,"s":6.11,"t":9.37,"u":2.85,"v":1.06,"w":2.34,"x":0.20,"y":2.04,"z":0.06}

def hamming(a,b):
    count=0
    for i in xor(a,b):
        for j in bin(i):
            if (j=='1'):
                count+=1
    return count

def score(what):
    score=0
    for i in what:
        if (ord(i) in range(97,123) ):
            score+=frequency[i]
        elif(ord(i) in range(65,91) ):
            score+=(frequency[i.lower()]*0.75)
        elif(i!=' '):
            score*=0.95
    return score

print(hamming("this is a test","wokka wokka!!!"))
mini=9999999
text = open("6.txt","r")
cipher=base64.b64decode(text.read())
for i in range(2,40):
    dist=0
    for j in range(1,int(len(cipher)/i+1)):
        dist+=hamming(cipher[0:i*j],cipher[i:i*j])
        dist/=len(cipher)
    if(dist<=mini):
        mini=dist
        leng=i
key=''
print(mini,leng)
for i in range(0,leng):
    maxi=0
    y=cipher[i::leng]
    for j in range(0,128):
        plain=''
        for k in y:
            plain+=chr(k^j)
        if(score(plain)>maxi):
            maxi=score(plain)
            plaintext=j
    key+=chr(plaintext)
for i in range(0,len(cipher)):
    print(chr(cipher[i]^ord(key[i%29])),end='')
```

It will give us 

the key : **Terminator X: Bring the noise**

and the ciphertext : 

```
I'm back and I'm ringin' the bell 
A rockin' on the mike while the fly girls yell 
In ecstasy in the back of me 
Well that's my DJ Deshay cuttin' all them Z's 
Hittin' hard and the girlies goin' crazy 
Vanilla's on the mike, man I'm not lazy. 

I'm lettin' my drug kick in 
It controls my mouth and I begin 
To just let it flow, let my concepts go 
My posse's to the side yellin', Go Vanilla Go! 

Smooth 'cause that's the way I will be 
And if you don't give a damn, then 
Why you starin' at me 
So get off 'cause I control the stage 
There's no dissin' allowed 
I'm in my own phase 
The girlies sa y they love me and that is ok 
And I can dance better than any kid n' play 

Stage 2 -- Yea the one ya' wanna listen to 
It's off my head so let the beat play through 
So I can funk it up and make it sound good 
1-2-3 Yo -- Knock on some wood 
For good luck, I like my rhymes atrocious 
Supercalafragilisticexpialidocious 
I'm an effect and that you can bet 
I can take a fly girl and make her wet. 

I'm like Samson -- Samson to Delilah 
There's no denyin', You can try to hang 
But you'll keep tryin' to get my style 
Over and over, practice makes perfect 
But not if you're a loafer. 

You'll get nowhere, no place, no time, no girls 
Soon -- Oh my God, homebody, you probably eat 
Spaghetti with a spoon! Come on and say it! 

VIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino 
Intoxicating so you stagger like a wino 
So punks stop trying and girl stop cryin' 
Vanilla Ice is sellin' and you people are buyin' 
'Cause why the freaks are jockin' like Crazy Glue 
Movin' and groovin' trying to sing along 
All through the ghetto groovin' this here song 
Now you're amazed by the VIP posse. 

Steppin' so hard like a German Nazi 
Startled by the bases hittin' ground 
There's no trippin' on mine, I'm just gettin' down 
Sparkamatic, I'm hangin' tight like a fanatic 
You trapped me once and I thought that 
You might have it 
So step down and lend me your ear 
'89 in my time! You, '90 is my year. 

You're weakenin' fast, YO! and I can tell it 
Your body's gettin' hot, so, so I can smell it 
So don't be mad and don't be sad 
'Cause the lyrics belong to ICE, You can call me Dad 
You're pitchin' a fit, so step back and endure 
Let the witch doctor, Ice, do the dance to cure 
So come up close and don't be square 
You wanna battle me -- Anytime, anywhere 

You thought that I was weak, Boy, you're dead wrong 
So come on, everybody and sing this song 

Say -- Play that funky music Say, go white boy, go white boy go 
play that funky music Go white boy, go white boy, go 
Lay down and boogie and play that funky music till you die. 

Play that funky music Come on, Come on, let me hear 
Play that funky music white boy you say it, say it 
Play that funky music A little louder now 
Play that funky music, white boy Come on, Come on, Come on 
Play that funky music 
```

### 7. AES in ECB mode

The Base64-encoded content [in this file](https://cryptopals.com/static/challenge-data/7.txt) has been encrypted via AES-128 in ECB mode under the key

```
"YELLOW SUBMARINE".
```

(case-sensitive, without the quotes; exactly 16 characters; I like "YELLOW SUBMARINE" because it's exactly 16 bytes long, and now you do too).

Decrypt it. You know the key, after all.

Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher.

```
Do this with code.

You can obviously decrypt this using the OpenSSL command-line tool, but we're having you get ECB working in code for a reason. You'll need it *a lot* later on, and not just for attacking ECB.
```

#### Solving

Now we have to decrypt AES encryption in ECB mode. We have the Crypto library in python for this. Using it we can encrypt the cipher in the file

```python
import base64
from Crypto.Cipher import AES

text=open("7.txt","r").read()
text=base64.b64decode(text)

key=b"YELLOW SUBMARINE"
cipher=AES.new(key,AES.MODE_ECB)
print(cipher.decrypt(text).decode())
```

It will give us the same song from previous challenge

### 8. Detect AES in ECB mode

[In this file](https://cryptopals.com/static/challenge-data/8.txt) are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.

#### Solving

Now we have to detect AES in ECB mode

The problem with AES is that the same plaintext block will produce same ciphertext. So we can check if there are any duplicated blocks in the ciphertext to check whether it is an AES encrypted one

```python
import binascii

text=open("8.txt","r")
cipher=[]
for line in text:
    cipher+=[binascii.unhexlify(line.strip())]
for i in cipher:
    for j in range(0,int(len(i)/16)):
        for k in range(j,int(len(i)/16)):
            if(i[j*16:(j+1)*16]==i[(k+1)*16:(k+2)*16]):
                encrypted=i
print(encrypted)
```

It will give us :

```
b'\xd8\x80a\x97@\xa8\xa1\x9bx@\xa8\xa3\x1c\x81\n=\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\xe2\xdd\x05/kd\x1d\xbf\x9d\x11\xb04\x85B\xbbW\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\x94u\xc9\xdf\xdb\xc1\xd4e\x97\x94\x9d\x9c~\x82\xbfZ\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\x97\xa9>\xab\x8dj\xec\xd5fH\x91Tx\x9ak\x03\x08d\x9a\xf7\r\xc0oO\xd5\xd2\xd6\x9ctL\xd2\x83\xd4\x03\x18\x0c\x98\xc8\xf6\xdb\x1f*?\x9c@@\xde\xb0\xabQ\xb2\x993\xf2\xc1#\xc5\x83\x86\xb0o\xba\x18j'
```

