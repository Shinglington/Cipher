from myciphers.cipher import SubCipher

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