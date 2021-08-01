#This should be a programm that will be able to encrypt
#and decrypt data stored in Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(text_par, shift_par):
    ciphertext = ''
    for i in text:
        position = alphabet.index(i)
        new_position = position + shift_par
        new_letter = alphabet[new_position]
        ciphertext += new_letter
    print(f"The encoded message is: '{ciphertext}'")

def decrypt (text_par, shift_par):
    decryptedtext = ''
    for i in text:
        position = alphabet.index(i)
        oldposition = position - shift_par
        old_letter = alphabet[oldposition]
        decryptedtext += old_letter
    print(f'The decrypted message is "{decryptedtext}"".')

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
    