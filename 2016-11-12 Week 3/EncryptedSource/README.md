# XOR Encrypted C Code for 200

The challenge is to decrypt a piece of XOR encrypted c code. The XOR encrypt
code is in the python script, it will be useful for solving the problem. The key
length is 26 bytes and it uses English

Hint: Most code contains regularities and patterns

[encrypted_source_sourcecode.dat](https://github.com/UConnSec/Challenges/blob/master/2016-11-12 Week 3/EncryptedSource/encrypted_source_sourcecode.dat)

The company releasing the encrypted source code is so confident that no one can
break it, they also release their encryptor code.

```python
#!/bin/python
import sys

#cyphertext: data in the encrypted file
#key: key to be xored through the cyphertext
def crypt(cyphertext,key):    

    #prepare some variables,
    #keyindex indicates current read spot of key
    #plaintextList is the precursor to the return value
    keyIndex = 0
    plaintextList = []
    #iterate through the cyphertext xoring characters
    for cypherChar in cyphertext:
        # ^ is xor
        plaintextList.append(cypherChar ^ key[keyIndex])
        #if index extends past key then it should reset to first char in key
        keyIndex = (keyIndex + 1) % len(key)

    #convert list object to bytes object
    return(bytes(plaintextList))

if __name__ == "__main__":
    #takes 2 arguments: KEY_FILE,FILE
    if (len(sys.argv) != 4):
        sys.exit('Usage: %s <KEY_FILE> <ENC_FILE> <RESULT_FILE_NAME>' % sys.argv[0])

    #open the files to be read as raw data instead of characters with 'rb'
    keyFile = open(sys.argv[1],'rb')
    cyphertextFile = open(sys.argv[2],'rb')

    #copy the file's contents into strings
    #remove newline from end of key
    key = keyFile.readline()
    if key[-1] == ord('\n'):
        key = key[:-1]
    print(len(key))
    #for the sake of this program plaintext/cyphertext file is named cyphertext
    #YOU COULD PASS A PLAINTEXTFILE AS CYPHERTEXTFILE AND THE OUTPUT WILL BE CYPHERTEXT
    cyphertext = cyphertextFile.read()

    #convert the list to a string and write to result file
    result = open(sys.argv[3],'wb')
    result.write(crypt(cyphertext,key))

    #cleanup
    cyphertextFile.close()
    result.close()
    keyFile.close()
    cyphertextFile.close()
```
