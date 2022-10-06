from cipher import SubCipher

class Vigenere(SubCipher):
    def __init__(self, key = "ABCDEF", alphabet = SubCipher.uppercase, keep_case = False):
        SubCipher.__init__(self, key, alphabet, keep_case)