from myciphers.cipher import SubCipher

class SimpleSub(SubCipher):
	def __init__(self, key = SubCipher.uppercase, alphabet = SubCipher.uppercase, keep_case = False):
		SubCipher.__init__(self, key, alphabet, keep_case)

	def encrypt(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
		text = self.prep_text(text, keep_spaces, keep_punct, keep_num)
		ciphertext = ""
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				new_char = self.key[self.alphabet.index(new_char)]
			if c.islower() and self.keep_case:
				new_char = new_char.lower()
			ciphertext += new_char
		return ciphertext
		
	def decrypt(self, text, keep_spaces=False, keep_punct=False, keep_num=False):
		text = self.prep_text(text, keep_spaces, keep_punct, keep_num)
		plaintext = ""
		for c in text:
			new_char = c.upper()
			if new_char in self.key:
				new_char = self.alphabet[self.key.index(new_char)]
			if c.islower() and self.keep_case:
				new_char = new_char.lower()
			plaintext += new_char
		return plaintext
	## Decryption with partial decrpytion dictionary
	def partial_decrypt(self, text, decrypt_dict):
		text = text.lower()
		for c, p in decrypt_dict.items():
			if p != None:
				text = text.replace(c.lower(), p.upper())
		return text
			
		
		
