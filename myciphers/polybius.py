from myciphers.cipher import Cipher


class PolybiusSquare(Cipher):
	def __init__(self, square = "ABCDEFGHIKLMNOPQRSTUVWXYZ", size = 5, chars = None):
		Cipher.__init__(self, square.upper())
		self.size = size
		self.chars = chars or "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:size]
		assert len(self.alphabet) == size ** 2
		assert len(self.chars) == size


	def encrypt_char(self, char):
		row = int(self.alphabet.index(char) / self.size)
		col = (self.alphabet.index(char) % self.size)
		return self.chars[row] + self.chars[col]

	def decrypt_pair(self, pair):
		row = self.chars.index(pair[0])
		col = self.chars.index(pair[1])
		return self.alphabet[row*self.size + col]
	
	def encrypt(self, text):
		text = self.prep_text(text
							 ,keep_spaces = False
							 ,keep_punct = False
							 ,keep_num = False)
		text = text.replace("J","I")
		ciphertext = ""
		for i in range(len(text),):
			ciphertext += self.encrypt_char(text[i])
		return ciphertext
		
	def decrypt(self, text):
		text = self.prep_text(text ,keep_spaces = False)
		plaintext = ""
		for i in range(0, len(text), 2):
			pair = text[i:i+2]
			plaintext += self.decrypt_pair(pair)
		return plaintext
		