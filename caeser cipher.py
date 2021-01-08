def encrypt_caesar(plaintext):
    ciphertext=""
    for i in range(len(plaintext)):
        char_value=ord(plaintext[i])
        if char_value>=65 and char_value<=90:               
            if char_value>=88:
                ciphertext+=chr(char_value-23)
            else:
                ciphertext+=chr(char_value+3)
        elif plaintext[i]==" ":
            ciphertext+=plaintext[i]
        else:
            ciphertext+=plaintext[i]
    return ciphertext

def decrypt_caesar(ciphertext):
    plaintext1=""
    for j in range(len(ciphertext)):
        cipher_value=ord(ciphertext[j])
        if cipher_value>=65 and cipher_value<=90:
            if cipher_value<=67:
                plaintext1+=chr(cipher_value+23)
            else:
                plaintext1+=chr(cipher_value-3)
        elif ciphertext[j]==" ":
            plaintext1+=ciphertext[j]
        else:
            plaintext1+=ciphertext[j]
    return plaintext1

encryption=input("Enter string for encryption and decryption :").upper()
decryption = encrypt_caesar(encryption)
print(f"Encrypted form: {decryption}")
print(f"Decrypted form :{decrypt_caesar(decryption)}")