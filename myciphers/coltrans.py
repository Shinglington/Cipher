from myciphers.cipher import TransCipher

class ColTrans(TransCipher):
    def __init__(self, key = "ABCDEF"):
        TransCipher.__init__(self, key.upper())

    def get_encrypt_order(self):
        unsorted_letters = [(self.key[i], i) for i in range(len(self.key))]
        sorted_letters = [(letter, index) for letter, index in sorted(unsorted_letters)]
        return [pair[1] for pair in sorted_letters]

    def get_decrypt_order(self):
        return
    
    def make_columns(self, text):
        columns = []
        keylen = len(self.key)
        while len(text) % keylen != 0:
            text += "X"
        for col_num in range(keylen):
            columns.append("")
        for i in range(len(text)):
            columns[i%keylen] = columns[i%keylen] + text[i]
        return columns

    def get_string_from_cols(self, columns, order):
      string = ""
      for i in range(len(order)):
        string += columns[order[i]]
      return string
            
    def encrypt(self, text, keep_spaces = False, keep_punct = False):
        text = self.prep_text(text, keep_spaces, keep_punct)
        columns = self.make_columns(text)
        return self.get_string_from_cols(columns, self.get_encrypt_order())
      