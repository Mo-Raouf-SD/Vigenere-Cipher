print("Important notes:")
print("1- Your plain text can be in either uppercase or lowercase letters, or even a mix of the two.")
print("2- The ciphertext will always be in uppercase letters.")
print("3- The key can be longer than the plain text.")

def query():
    question = input("Do you want to cipher another text?(y/n)")
    if question == 'y' or question == 'Y':
        ciphering()
    if question == 'n' or question == 'N':
        exit()
    else:
        query()

def exit():
    print("")
    print("Submitted by: Mohammed Abdulraouf AlHassan")
    print("Index: 164093")

def ciphering():
    print("")
    plain = input("Enter the Plain Text:")
    plainText = plain.upper()
    k = input("Enter the Key:")
    key = k.upper()
    plainlist = list(plainText)
    keylist = list(key)
    textLen = len(plainlist)
    keyLen = len(keylist)

    def genNewKey():
        if textLen > keyLen :
            tempKey = []
            i=0
            for x in range (0, textLen) :
                if i == keyLen:
                    i=0
                tempKey.append(keylist[i])
                i += 1
        else:
            diff = keyLen - textLen
            tempKey = keylist
            tempKey.pop(diff)
        return tempKey

    newKey = genNewKey()

    def cipher(plainText, newKey):
        cipherT = []
        for x in range(0, textLen):
            value = (ord(plainText[x]) + ord(newKey[x])) % 26
            value = value + ord('A')
            cipherT.append(chr(value))
        return cipherT

    cipherTe = cipher(plainText, newKey)
    cipherText = ""
    for x in cipherTe :
        cipherText += x
    print("Ciphertext:" + cipherText)
    print("")


ciphering()
query()
press = input("Press Enter to Exit")




