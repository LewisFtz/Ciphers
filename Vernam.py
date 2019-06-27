
def Vernam2(Text,Key):
    EncryptedText = []
    for i in range(len(Text)):
        numberCode = ord(Text[i])
        numberKey = ord(Key[i])
        cipher = numberCode^numberKey
        #cipher = (chr(cipher))
        
        EncryptedText.append(cipher)
    return EncryptedText

def Vernam(Text,Key):
    """ Returns the Vernam Cypher for given string and key """
    EncryptedText = "" # the Cypher text
    p = 0 # pointer for the key
    for c in Text:
        EncryptedText += chr(ord(c) ^ ord(Key[p]))
        p += 1
        if p==len(Key):
            p = 0
    return EncryptedText
