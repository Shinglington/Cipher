from myciphers.cipher import SubCipher

class Caesar(SubCipher):
    def __init__(self, key = 13, alphabet = SubCipher.uppercase, keep_case = False):
        SubCipher.__init__(self, key % len(alphabet), alphabet, keep_case)
    
    def encrypt(self, text, keep_spaces = True, keep_punct = True, keep_num = True):
        text = self.prep_text(text, keep_spaces, keep_punct, keep_num)
        ciphertext = ""
        for c in text:
            new_char = c.upper()
            if new_char in self.alphabet:
                new_char = self.alphabet[(self.alphabet.index(new_char) + self.key) % len(self.alphabet)]
            if c.islower() and self.keep_case:
                new_char = new_char.lower()
            ciphertext += new_char
        return ciphertext

    def decrypt(self, text, keep_spaces = True, keep_punct = True, keep_num = True):
        text = self.prep_text(text, keep_spaces, keep_punct, keep_num)
        plaintext = ""
        for c in text:
            new_char = c.upper()
            if new_char in self.alphabet:
                new_char = self.alphabet[(self.alphabet.index(new_char) + (len(self.alphabet) - self.key)) % len(self.alphabet)]
            if c.islower() and self.keep_case:
                new_char = new_char.lower()
            plaintext += new_char
        return plaintext

