from curses.ascii import isupper
from cipher import Cipher

class Caesar(Cipher):
    def __init__(self, key = 13, alphabet = "abcdefghijklmnopqrstuvwxyz", keep_case = False):
        Cipher.__init__(self, key % len(alphabet), alphabet, keep_case)
    
    def encrypt(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
        text = self.prep_text(text, keep_spaces, keep_punct, keep_num)
        ciphertext = ""
        for c in text:
            new_char = c.lower()
            if new_char in self.alphabet:
                new_char = self.alphabet[(self.alphabet.index(new_char) + self.key) % len(self.alphabet)]
            if c.isupper() and self.keep_case:
                new_char = new_char.upper()
            ciphertext += new_char
        return ciphertext

    def decrypt(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
        text = self.prep_text(text, keep_spaces, keep_punct, keep_num)
        plaintext = ""
        for c in text:
            new_char = c.lower()
            if new_char in self.alphabet:
                new_char = self.alphabet[(self.alphabet.index(new_char) + (len(self.alphabet) - self.key)) % len(self.alphabet)]
            if c.isupper() and self.keep_case:
                new_char = new_char.upper()
            plaintext += new_char
        return plaintext

