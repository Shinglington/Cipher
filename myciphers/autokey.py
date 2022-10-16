from myciphers.cipher import Cipher
from myciphers.vigenere import Vigenere
import myciphers.config as config

class Autokey(Cipher):
	def __init__(self, key, 
				 alphabet = config.alphabet_upper, 
				 detailed = config.detailed):
		Cipher.__init__(self, alphabet, detailed = detailed)
		self.key = key.upper()

	def encrypt(self, text):
		text = self.prep_text(text, 
							  keep_spaces = False,
							  keep_punct = False,
							  keep_num = False)
		ciphertext = ""
		for i in range(len(text)):
			if i < len(self.key):
				ciphertext += Vigenere(self.key[i], 
									   self.alphabet, 
									   detailed = False).encrypt(text[i])
			else:
				ciphertext += Vigenere(text[i - len(self.key)],
									   self.alphabet,
									   detailed = False).encrypt(text[i])
		return ciphertext


	def decrypt(self, text):
		text = self.prep_text(text, 
							  keep_spaces = False)
		plaintext = ""
		for i in range(len(text)):
			if i < len(self.key):
				plaintext += Vigenere(self.key[i], 
									   self.alphabet, 
									   detailed = False).decrypt(text[i])
			else:
				plaintext += Vigenere(plaintext[i - len(self.key)],
									   self.alphabet,
									   detailed = False).decrypt(text[i])
		return plaintext

					 