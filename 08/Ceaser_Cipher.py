alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_positions = position + shift_amount
        new_letter = alphabet[new_positions]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_positions = position - shift_amount + 26
        new_letter = alphabet[new_positions]
        cipher_text += new_letter
    print(f"The decoded text is {cipher_text}")

def demands():
    
    return text, shift

direction = "encode"
while direction in ("encode", "decode"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, anything else to quit:\n")  
    if direction in ("encode", "decode"):
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    


