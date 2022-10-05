from cipher import SubCipher

class Vigenere(SubCipher):
    def __init__(self, key = "ABCDEF", alphabet = "abcdefghijklmnopqrstuvwxyz")