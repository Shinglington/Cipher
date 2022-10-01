from cipher import Cipher

class Caesar(Cipher):
    def __init__(self, key = 13, alphabet = "abcdefghijklmnopqrstuvwxyz", keep_punct = False):
        self.alphabet = alphabet
        self.key = key % len(alphabet)
    
    def encrypt(self, text):
        if not keep_punct:
            
        ciphertext = ""
        for c in text:
            new_char = c.lower()
            if (new_char) in self.alphabet:
                new_char = self.alphabet[(self.alphabet.index(new_char) + self.key) % len(self.key)]
                if c.isupper():
                    new_char = new_char.upper()
            ciphertext = ciphertext + new_char
        return ciphertext

    def decrypt(text):
            plaintext = encrypt(ciphertext, -shift, alphabet)


        return 
