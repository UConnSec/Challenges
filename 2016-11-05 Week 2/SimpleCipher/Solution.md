# Solution

```
cloumxsqzsgwbmxpcimszgmtxcpqzcbmgtqpkqxxczwbmxqzcbmgrcmpzclszgubqqrmrdcpxcszgxcsz
```

The first task here is to determine what kind of cipher we were given.

The Incidence of Coincidence is quite high for this cipher. Around `0.07191` on
the [PracticalCryptography.com](http://practicalcryptography.com/cryptanalysis/text-characterisation/index-coincidence/) tool.

This suggests that the cipher is monoalphabetic and possibly just a simple substitution cipher.

Let's try cracking the ciphertext above as an Affine Cipher. (Supposedly after trying to crack it as other simple monoalphabetic ciphers.)

http://www.dcode.fr/affine-cipher

```
educationiswhatremainsafteronehasforgottenwhatonehaslearnedinschoolalberteinstein
```

a = 17, b = 12
