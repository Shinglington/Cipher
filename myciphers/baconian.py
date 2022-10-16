from myciphers.cipher import Cipher
import myciphers.config as config
class Baconian(Cipher):
	def __init__(self, alphabet = config.alphabet_upper):
		Cipher.__init__(self, alphabet)

	def encrypt(self, text):
		text = self.prep_text(text, 
							  keep_spaces = False, 
							  keep_punct = False, 
							  keep_num = False)
		ciphertext = ""
		for char in text:
			binary = bin(self.alphabet.index(char.upper()))
			ciphertext += str(binary).replace("0b", "").zfill(5)
			ciphertext += " "
		return ciphertext

	def decrypt(self, text):
		text = self.prep_text(text, keep_spaces = False
							 , keep_punct = False
							 , keep_num = True)
		text = text.upper().replace("A","0").replace("B","1")
		plaintext = ""
		for i in range(0, len(text), 5):
			binary = text[i:i+5]
			plaintext += self.alphabet[int("0b" + binary, base = 0)]
		return plaintext