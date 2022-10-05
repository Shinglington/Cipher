from myciphers.cipher import TransCipher

class ColTrans(TransCipher):
    def __init__(self, key = "ABCDEF"):
        TransCipher.__init__(self, key.upper())

    def get_order(self):
        unsorted_letters = [(self.key[i], i) for i in range(len(self.key))]
        sorted_letters = [(letter, index) for letter, index in sorted(unsorted_letters)]
        return [pair[1] for pair in sorted_letters]

    def cols_from_plaintext(self, text, pad_text = True):
        columns = []
        keylen = len(self.key)
        if pad_text:
          while len(text) % keylen != 0:
              text += "X"
        for col_num in range(keylen):
            columns.append("")
        for i in range(len(text)):
            columns[i%keylen] = columns[i%keylen] + text[i]
        return columns

    def cols_from_ciphertext(self, text):
        columns = []
        keylen = len(self.key)
        for col_num in range(keylen):
            columns.append("")
        for i in range(len(text)):
            columns[i%int(len(text) / keylen)] += text[i]
        return columns

    def ciphertext_from_col(self, columns, order):
        string = ""
        for i in range(len(order)):
          string += columns[order[i]]
        return string

    def plaintext_from_col(self, columns, order):
        string = ""
        for i in range(len(columns)):
            for j in range(len(order)):
                if len(columns[i]) > order.index(j):
                    string += columns[i][order.index(j)]
        return string
          
            
    def encrypt(self, text, keep_spaces = False, keep_punct = False):
        text = self.prep_text(text, keep_spaces, keep_punct)
        columns = self.cols_from_plaintext(text)
        return self.ciphertext_from_col(columns, self.get_order())


    def decrypt(self, text, keep_spaces = False, keep_punct = False):
        text = self.prep_text(text, keep_spaces, keep_punct)
        columns = self.cols_from_ciphertext(text)
        print(columns)
        return self.plaintext_from_col(columns, self.get_order())