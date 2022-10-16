from myciphers.cipher import Cipher
import myciphers.config as config
from myciphers.simplesub import SimpleSub

class KeywordSub(Cipher):
	def __init__(self, keyword = "KEY", 
				 alphabet = config.alphabet_upper,
				 detailed = config.detailed):
		Cipher.__init__(self, alphabet)
		self.keyword = keyword.upper()
		self.cipher_alphabet = KeywordSub.generate_cipher_alphabet(self.keyword, alphabet)
		if self.detailed:
			print("Cipher alphabet : {0}".format(self.cipher_alphabet))
		
	def generate_cipher_alphabet(keyword, alphabet):
		cipher_alphabet = ""
		## Add keyword to start of cipher alphabet
		for letter in keyword:
			if letter not in cipher_alphabet:
				cipher_alphabet += letter

		## Add rest of letters of alphabet
		for letter in alphabet:
			if letter not in cipher_alphabet:
				cipher_alphabet += letter
		return cipher_alphabet

	def encrypt(self, text):
		return SimpleSub(self.cipher_alphabet).encrypt(text)
		
	def decrypt(self, text):
		return SimpleSub(self.cipher_alphabet).decrypt(text)

	def dictionary_attack(text):
		return text
		
		
		
			
		
	