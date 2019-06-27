
def Encrypt(PlainText,Key):
    PlainText = str(PlainText.lower())
    Key = int(Key)
    EncryptedText = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz" 
    for i in PlainText:
        if i in alphabet:
            EncryptedText += alphabet[(alphabet.index(i)+Key)%(26)]
    return EncryptedText


def Decrypt(EncryptedText,Key):
    EncryptedText = str(EncryptedText.lower())
    Key = int(Key)
    DecryptedText = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"        
    for a in EncryptedText:
        if a in alphabet:
            DecryptedText += alphabet[(alphabet.index(a)-Key)%(26)]
    return DecryptedText
        












            

##            
##
##
##
##
##
##        
##        while True:
##            try:
##                Key = int(Key)
##            except ValueError:
##                
##                continue
##            else:            
##                if Key >= 1 and Key <=25:
##                    KeyV = 1      
##                    return Key, KeyV
##                else:
##                    )
##                    continue
##
