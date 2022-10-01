
class Cipher():
    def __init__(self, key, alphabet, ignore_case = True):
        self.key = key
        self.alphabet = alphabet
        self.ignore_case = ignore_case

    def encrypt(self, text):
        return text
    
    def decrypt(self, text):
        return text
    
    def prep_text(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
        output = ""
        filter = ""
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
