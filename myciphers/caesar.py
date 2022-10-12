from myciphers.cipher import Cipher
import myciphers.config as config
class Caesar(Cipher):
	def __init__(self, key = 13, alphabet = config.alphabet_upper):
		self.alphabet = alphabet
		Cipher.__init__(self, key % len(self.alphabet))

	def encrypt(self, text):
		text = self.prep_text(text)
		ciphertext = ""
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				new_char = self.alphabet[(self.alphabet.index(new_char) + self.key) % len(self.alphabet)]
			if c.islower() and self.keep_case:    
				new_char = new_char.lower()
			ciphertext += new_char
		return ciphertext

	def decrypt(self, text):
		text = self.prep_text(text)
		plaintext = ""
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				new_char = self.alphabet[(self.alphabet.index(new_char) + (len(self.alphabet) - self.key)) % len(self.alphabet)]
			if c.islower() and self.keep_case:
				new_char = new_char.lower()
			plaintext += new_char
		return plaintext