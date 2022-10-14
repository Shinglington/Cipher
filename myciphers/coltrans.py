from myciphers.cipher import Cipher
import myciphers.config as config

class ColTrans(Cipher):
	def __init__(self, key = "ABCDEF"):
		Cipher.__init__(self)
		self.key = key.upper()

	def get_order(self, keyword):
		## \/ DETAILED DISPLAY \/ ##
		if config.detailed:
			print("\n\n## FINDING ORDER OF COLUMNS ##")
			print("Keyword is {0} -> convert keyword to index numbers".format(self.key))
		## /\ DETAILED DISPLAY /\ ##
			
		unsorted_letters = [(keyword[i], i) for i in range(len(keyword))]
		sorted_letters = [(letter, index) for letter, index in sorted(unsorted_letters)]
		col_order = [pair[1] for pair in sorted_letters]
		
		## \/ DETAILED DISPLAY \/ ##
		if config.detailed:
			print("Found order to be " 
				  + "".join(str(x) for x in col_order))
		## /\ DETAILED DISPLAY /\ ##
		return col_order


	def display_cols(self, columns):
		for row in range(len(columns[0])):
			current_row = ""
			# loop through each column
			for col in range(len(columns)):
				if len(columns[col]) > row:
					current_row += columns[col][row]
			print(current_row)
        
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
			
        ## \/ DETAILED DISPLAY \/ ##
			if config.detailed:
				print("\n\n## COLUMNS FROM PLAINTEXT ##")
				self.display_cols(columns)
		## /\ DETAILED DISPLAY /\ ##
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
			
		## \/ DETAILED DISPLAY \/ ##
		if config.detailed:
			print("\n\n## COLUMNS FROM CIPHERTEXT ##")
			self.display_cols(columns)
		## /\ DETAILED DISPLAY /\ ##
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
          
            
	def encrypt(self, text, 
				keep_spaces = False, 
				keep_punct = False):
		# Remove spaces and extra punctuation
		text = self.prep_text(text, keep_spaces = keep_spaces, keep_punct = keep_punct)
		columns = self.cols_from_plaintext(text)
		col_order = self.get_order(self.key)
		return self.ciphertext_from_col(columns, col_order)


	def decrypt(self, text):
		## If ciphertext contains numbers and punctuation, likely need them to get columns correct
		text = self.prep_text(text, 
							  keep_num = True, 
							  keep_punct = True)
		columns = self.cols_from_ciphertext(text)
		col_order = self.get_order(self.key)
		return self.plaintext_from_col(columns, col_order)
