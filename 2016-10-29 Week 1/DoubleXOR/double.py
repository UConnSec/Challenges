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
