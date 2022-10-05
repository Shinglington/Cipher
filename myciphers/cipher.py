
class Cipher():
    def __init__(self, key, keep_case = False):
        self.key = key
        self.keep_case = keep_case

    def encrypt(self, text):
        return text
    
    def decrypt(self, text):
        return text
    
    def prep_text(self, text, filter = ""):
        output = ""
        if not self.keep_case:
            text = text.upper()
        for c in text:
            if c not in filter:
                output += c
        return output

class SubCipher(Cipher):
    def __init__(self, key, alphabet, keep_case = False):
        Cipher.__init__(self, key, keep_case)
        self.alphabet = alphabet

    def encrypt(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
        return text
    
    def decrypt(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
        return text
    
    def prep_text(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
        filter = ""
        if not keep_spaces:
            filter += ' '
        if not keep_punct:
            filter += "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        if not keep_num:
            filter += "0123456789"
        return Cipher.prep_text(self, text, filter)

class TransCipher(Cipher):
    def __init__(self, key, keep_case = False):
        Cipher.__init__(self, key, keep_case)

    def encrypt(self, text, keep_spaces = False, keep_punct = False):
        return self.prep_text(self, text, keep_spaces, keep_punct)
    
    def decrypt(self, text, keep_spaces = False, keep_punct = False):
        return self.prep_text(self, text, keep_spaces, keep_punct)
    
    def prep_text(self, text, keep_spaces = False, keep_punct = False):
        filter = ""
        if not keep_spaces:
            filter += ' '
        if not keep_punct:
            filter += "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        return Cipher.prep_text(self, text, filter)