from myciphers.vigenere import Vigenere
import myciphers.config as config

class Beaufort(Vigenere):
	def __init__(self, key, 
				 alphabet = config.alphabet_upper, 
				 detailed = config.detailed):
		Vigenere.__init__(self, key, alphabet, detailed)

	def get_cipherchar(self, plainchar, keychar):
		# go to row of plaintext letter, then go to corresponding column which gives the keychar
		# corresponding column gives ciphertext char
		return Vigenere.get_plainchar(self, keychar, plainchar)

	def get_plainchar(self, cipherchar, keychar):
		return Vigenere.get_plainchar(self, keychar, cipherchar)

	def get_keychar(self, plainchar, cipherchar):
		return Vigenere.get_cipherchar(self, plainchar, cipherchar)
	

	