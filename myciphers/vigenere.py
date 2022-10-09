from myciphers.cipher import SubCipher
import myciphers.utility as util
class Vigenere(SubCipher):
	def __init__(self, key = "ABCDEF", alphabet = SubCipher.uppercase, keep_case = False):
		SubCipher.__init__(self, key.upper(), alphabet, keep_case)
		self.grid = self.tabula_recta()

	def tabula_recta(self):
		grid = []
		for i in range(len(self.alphabet)):
			grid.append(self.alphabet[i: len(self.alphabet)] + self.alphabet[0:i])
		return grid
	
	def get_cipherchar(self, plainchar, keychar):
        # Go to row corresponding to plainchar
        # Go to column corresponding to keychar
        # Return cipherchar
		return self.grid[self.alphabet.index(plainchar)][self.alphabet.index(keychar)]

	def get_plainchar(self, cipherchar, keychar):
        # Go to row corresponding to keychar
        # Find position of cipherchar in row
        # Use position to get corresponding plainchar
		return self.alphabet[self.grid[self.alphabet.index(keychar)].index(cipherchar)]
		
	def encrypt(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
		text = self.prep_text(text, keep_spaces, keep_punct, keep_num)
		ciphertext = ""
		keyindex = 0
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				print(new_char)
				new_char = self.get_cipherchar(new_char, self.key[keyindex])
				keyindex = (keyindex + 1) % len(self.key)
			if self.keep_case and c.islower:
				new_char = new_char.lower()
			ciphertext += new_char
		return ciphertext
                

	def decrypt(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
		text = self.prep_text(text, keep_spaces, keep_punct, keep_num)
		plaintext = ""
		keyindex = 0
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				new_char = self.get_plainchar(new_char, self.key[keyindex])
				keyindex = (keyindex + 1) % len(self.key)
			if self.keep_case and c.islower:
				new_char = new_char.lower()
			plaintext += new_char
		return plaintext

def guess_key_length(text, max_length = 15):
	text = text.replace(" ","").upper().replace(SubCipher.punctuation,"")
	ioc_list = []
	for i in range(1, max_length):
		columns = []
		for col_count in range(i):
			this_column = ""
			for j in range(i, len(text), col_count):
				this_column += text[j]
			columns.append(this_column)

		column_iocs = []
		for c in columns:
			ioc = 0
			if len(c) > 1:
				ioc = util.calc_ioc(c)
			column_iocs.append(ioc)
		average_ioc = sum(column_iocs) / len(column_iocs)
		ioc_list.append(average_ioc)

	key_length = 0
	for i in range(len(ioc_list)):
		if key_length = 0:
			key_length = i+1
		elif ioc_list[i] > ioc_list[key_length - 1]:
			key_length = i+1
	
	return key_length



def guess_key(text):
	length =
	text = text.replace(" ","").upper().replace(SubCipher.punctuation,"")
	