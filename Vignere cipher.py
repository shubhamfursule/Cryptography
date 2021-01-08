def encrypt_vigenere(plaintext,keyword):
    Chipertext=''
    if len(keyword)!= len(plaintext):
        for j in range(len(plaintext)-len(keyword)):
            keyword+=keyword[j]
    print(keyword)
    upper_char1=[chr(i) for i in range(65,91)]
    for i in range(len(plaintext)):
        ascii_value=upper_char1.index(plaintext[i])+upper_char1.index(keyword[i])
        if ascii_value>25:
            Chipertext+=upper_char1[ascii_value-26]
        else:
            Chipertext+= upper_char1[ascii_value]
    return Chipertext

def decrypt_vigenere(ciphertext,keyword):
    Plaintext=""
    if len(keyword)!= len(ciphertext):
        for k in range(len(ciphertext)-len(keyword)):
            keyword+=keyword[k]
    upper_chard=[chr(i) for i in range(65,91)]
    for i in range(len(ciphertext)):
        ascii_value1=(upper_chard.index(ciphertext[i])+26)-upper_chard.index(keyword[i])
        if ascii_value1<25:
            Plaintext+= upper_chard[ascii_value1]
            
        else:
            Plaintext+= upper_chard[ascii_value1-26]
    return Plaintext


while True:
    try:
        plaintext_vig=input("Enter the String for decryption :").upper()
        keyword_vig=input("Enter the Secret keyword: ").upper()
        plaintext_nospace=""
        for word in plaintext_vig.split(" "):
            plaintext_nospace+=word
        if len(keyword_vig)<=len(plaintext_nospace):
            if plaintext_nospace.isalpha() and keyword_vig.isalpha() :
                encrypted=encrypt_vigenere(plaintext_nospace,keyword_vig)  
                print(f"encrypted form of given: {encrypted}\n")
                Chipertext_vig=input("Enter the string for 'Encryption' :").upper()
                keyword_vig1=input("Enter  secret keyword for 'encrypt' : ").upper()
                if Chipertext_vig.isalpha() and keyword_vig1.isalpha():
                    decrypted=decrypt_vigenere(Chipertext_vig,keyword_vig1)
                    print(f"decrypted form is : {decrypted}")
                    break
                else:
                    raise "Error"
            else: 
                raise "ValueError"
        else:
             raise "keyError"                              
    except:
        if "ValueError":
            print("!!Enter only aphabets and no space between string !!")
        else:
            print("!!Keyword should be smaller than plaintext!!")