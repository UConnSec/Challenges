# Double XOR

We were flying in a spaceship and out of nowhere we get hit with some ciphertext. It didn't cause any damage, but we are left wondering: what hit us?

The pet space monkey thinks it is 8-bit binary encoded ASCII with the same XOR key applied to both. He says the key should be 656 characters long and then returns to her crib.

Hint: There are two possible keys.

Cipher text 1:
```
01101101001001111000011110111111000000100110101011010010001100001000001010100010111010100010001011110010010010101011110101000101111101100010010010000101001001000100000100011001011100111110000100000110110001001111101001110000100010000100000010011000101001000110111110101100011110011100100111000011110100111000000111100101000100111001001001110100011111111010110100010110000000011110010000000101110001010100000001110010110000000000010111100110000001010011111000110011100111000111000110100101000000110001111011010101101000111100011001110101000111110101101110101101010001011110010101011101110100010110001111011010000011011101100111110111101000111001011010100101
```
Cipher text 2:
```
01111011001101101001000110111111000001100110110111001000011111111000010111110001101000110011000011110010010100011011101001010001111100010111110111010111001101010100100100011001011110011110011100010000100101101011010100110110101101010101000111001010111101110110010110100110011010011000101011001110110000011101001010110110000110001001110001110100011011001110001000010010000100001110111000011011100010010101001000111010110010000001111110110010000001010111000000100010110101000111000010101010000110110101011111010111101000011000011101110011000110010101101110110000010001011110111101010010100111110011011111001101010001011101101011110111101111001101110110101011
```

```python
import random


def xorstr(str1, str2):
    result = []

    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            result.append(1)
        else:
            result.append(0)

    return "".join([str(c) for c in result])


plaintext1 = 'Education is what remains after one has forgotten what one has learned in school. '
plaintext2 = 'Success is a lousy teacher. It seduces smart people into thinking they can\'t lose.'

p1bin = [format(ord(c), '08b') for c in plaintext1]
p1bin = "".join([str(c) for c in p1bin])

p2bin = [format(ord(c), '08b') for c in plaintext2]
p2bin = "".join([str(c) for c in p2bin])

key = [random.randrange(2) for _ in range(len(p1bin))]
key = "".join([str(c) for c in key])

print("Here's your key, keep it safe!: " + key)

ciphertext1 = xorstr(p1bin, key)
ciphertext2 = xorstr(p2bin, key)

print("Cipher text 1: " + ciphertext1)
print("Cipher text 2: " + ciphertext2)
```