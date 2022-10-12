from myciphers.cipher import Cipher
import myciphers.config as config

class ColTrans(Cipher):
    def __init__(self, key = "ABCDEF"):
        Cipher.__init__(self, key.upper())

    def get_order(self, keyword):
        unsorted_letters = [(keyword[i], i) for i in range(len(keyword))]
        sorted_letters = [(letter, index) for letter, index in sorted(unsorted_letters)]
        return [pair[1] for pair in sorted_letters]


    def display_cols(self, columns):
        print("\nCOLUMN DISPLAY")
        for row in range(len(columns[0])):
            current_row = ""
            for col in range(len(columns)):
                current_row += columns[col][row]
            print(current_row)
        print()
        
    def cols_from_plaintext(self, text, pad_text = True):
        columns = []
        keylen = len(self.key)
        if pad_text:
          while len(text) % keylen != 0:
              text += config.padding
        for col_num in range(keylen):
            columns.append("")
        for i in range(len(text)):
            columns[i%keylen] = columns[i%keylen] + text[i]
        # optional display of columns
        if config.detailed:
            self.display_cols(columns)
        return columns

    def cols_from_ciphertext(self, text):
        columns = []
        keylen = len(self.key)
        col_len = int(len(text) / keylen)
        for col_num in range(keylen):
            col = ""
            for i in range(col_len):
                col += text[col_num * col_len + i]
            columns.append(col)
        # optional display of columns
        if config.detailed:
            self.display_cols(columns)
        return columns

    def ciphertext_from_col(self, columns, order):
        string = ""
        for i in range(len(order)):
          string += columns[order[i]]
        return string

    def plaintext_from_col(self, columns, order):
        string = ""
        for i in range(len(columns[0])):
            for j in range(len(order)):
                if len(columns[order.index(j)]) > i:
                    string += columns[order.index(j)][i]
        return string
          
            
    def encrypt(self, text):
        text = self.prep_text(text)
        columns = self.cols_from_plaintext(text)
        return self.ciphertext_from_col(columns, self.get_order(self.key))


    def decrypt(self, text):
		## If ciphertext contains numbers and punctuation, likely need them to get columns correct
        text = self.prep_text(text, keep_num = True, keep_punct = True)
        columns = self.cols_from_ciphertext(text)
        return self.plaintext_from_col(columns, self.get_order(self.key))