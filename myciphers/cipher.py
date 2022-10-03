
class Cipher():
    def __init__(self, key, alphabet, keep_case = False):
        self.key = key
        self.alphabet = alphabet
        self.keep_case = keep_case

    def encrypt(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
        return text
    
    def decrypt(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
        return text
    
    def prep_text(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
        output = ""
        filter = ""
        if not self.keep_case:
            text = text.lower()
        if not keep_spaces:
            filter += ' '
        if not keep_punct:
            filter += "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        if not keep_num:
            filter += "0123456789"

        for c in text:
            if c not in filter:
                output += c
        return output
