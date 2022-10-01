from curses import keyname
from cipher import Cipher

class substition(Cipher):
    def __init__(self, key = "abcdefghijklmnopqrstuvwxyz", alphabet = "abcdefghijklmnopqrstuvwxyz", keep_case = False):
        Cipher.__init__(self, key, alphabet, keep_case)

    def encrypt(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
        return text

    def decrypt(self, text, keep_spaces=False, keep_punct=False, keep_num=False):
        return text