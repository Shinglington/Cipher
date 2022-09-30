import string

def encrypt(plaintext, shift, alphabet = string.ascii_lowercase):
    ciphertext = ""
    for c in plaintext:
        new_char = c.lower()
        if (new_char) in alphabet:
            new_char = alphabet[(alphabet.index(new_char) + shift) % len(alphabet)]
            if c.isUpper():
                new_char = new_char.upper()
        ciphertext = ciphertext + new_char
    return ciphertext
    
def decrypt(plaintext, shift = None, alphabet = string.ascii_lowercase):