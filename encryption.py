#This should be a programm that will be able to encrypt
#and decrypt data stored in Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print('Welcome to my Caesar Cipher cryptographer')
print('''                       _                              _           
                      | |                            | |          
  ___ _ __ _   _ _ __ | |_ ___   __ _ _ __ __ _ _ __ | |__  _   _ 
 / __| '__| | | | '_ \| __/ _ \ / _` | '__/ _` | '_ \| '_ \| | | |
| (__| |  | |_| | |_) | || (_) | (_| | | | (_| | |_) | | | | |_| |
 \___|_|   \__, | .__/ \__\___/ \__, |_|  \__,_| .__/|_| |_|\__, |
            __/ | |              __/ |         | |           __/ |
           |___/|_|             |___/          |_|          |___/ 
           ''')

keepgoing = True
while keepgoing == True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caeser(text_par, shift_par, positions_par):
        end_text = ''
        if shift_par > (26 * 2):
            shift_par = shift_par % 26
        for i in text:
            if i in alphabet:    
                position = alphabet.index(i)
                if positions_par == 'encode':
                    new_position = position + shift_par
                elif positions_par == 'decode':
                    new_position = position - shift_par
                new_letter = alphabet[new_position]
                end_text += new_letter
            else:
                end_text += i
        print(f"The {positions_par}d message is: '{end_text}'")

    caeser(text, shift, direction)

    stop = input('Do you wanna go again? (type yes or no)\n')
    if stop == 'no':
        keepgoing = False
        print('Good Bye!')
        