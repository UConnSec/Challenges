## Double XOR Solution

Since the same XOR key was used twice, the following proof shows that we can
guess potential plaintext outputs.

Given:
```
C1 = P1 ⊕ K  
C2 = P2 ⊕ K
```

Rearranging the equation gives us a potential key K? when guessing P1?:
```
K = C1 ⊕ P1
K? = C1 ⊕ P1?
```

Plugging this guess K into the decipher for P2:
```
P2 = C2 ⊕ C1 ⊕ P1?
```

And vice versa:
```
P1 = C2 ⊕ C1 ⊕ P2?
```

Here's your key, keep it safe!:
```
00101000010000111111001011011100011000110001111010111011010111111110110010000010100000110101000111010010001111011101010100100100100000100000010011110111010000010010110001111000000110101000111101110101111001001001101100010110111111000010010111101010100001000000000011000010000111001110100110101011101100101111001011000101011101011111110100000110000110001100001001100010011101011000000101101011111001010011011100011010101000010111000111000110011010100101000001010110101111000001100111000100011100000011111010111001110001101010011100000111011100010011111011001001011001011000110000110011111100010001000010111001011001011011011010011000110011111011100010000101
```