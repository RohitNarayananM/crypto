## XOR Starter

For longer binary numbers we XOR bit by bit: `0110 ^ 1010 = 1100`. We can XOR integers by first converting the integer from decimal to binary. We can XOR strings by first converting each character to the integer representing the Unicode character.

Given the string `"label"`, XOR each character with the integer `13`. Convert these integers back to a string and submit the flag as `crypto{new_string}`.

### Solving

Here we have to xor the string "label" with the integer 13. We can do that using:

```python
for i in "label":
    print(chr(ord(i)^13),end='')
```

It will give the flag



### Flag

**crypto{aloha}**