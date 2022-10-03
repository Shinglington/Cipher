from cipher import Cipher

class Substition(Cipher):
    def __init__(self, key = "abcdefghijklmnopqrstuvwxyz", alphabet = "abcdefghijklmnopqrstuvwxyz", keep_case = False):
        Cipher.__init__(self, key, alphabet, keep_case)

    def encrypt(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
        text = self.prep_text(text, keep_spaces, keep_punct, keep_num)
        ciphertext = ""
        for c in text:
            new_char = c.lower()
            if new_char in self.alphabet:
                new_char = self.key[self.alphabet.index(new_char)]
            if c.isupper() and self.keep_case:
                new_char = new_char.upper()
            ciphertext += new_char
        return ciphertext

    def decrypt(self, text, keep_spaces=False, keep_punct=False, keep_num=False):
        text = self.prep_text(text, keep_spaces, keep_punct, keep_num)
        plaintext = ""
        for c in text:
            new_char = c.lower()
            if new_char in self.key:
                new_char = self.alphabet[self.key.index(new_char)]
            if c.isupper() and self.keep_case:
                new_char = new_char.upper()
            plaintext += new_char
        return plaintext