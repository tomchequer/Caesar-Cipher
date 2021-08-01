#This should be a programm that will be able to encrypt
#and decrypt data stored in Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caeser(text_par, shift_par, positions_par):
    end_text = ''
    for i in text:
        position = alphabet.index(i)
        if positions_par == 'encode':
            new_position = position + shift_par
        elif positions_par == 'decode':
            new_position = position - shift_par
        new_letter = alphabet[new_position]
        end_text += new_letter
    print(f"The {positions_par}d message is: '{end_text}'")

caeser(text, shift, direction)


