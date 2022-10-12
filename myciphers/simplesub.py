from myciphers.cipher import Cipher
import myciphers.config as config

class SimpleSub(Cipher):
	def __init__(self, key = config.alphabet_upper, alphabet = config.alphabet_upper):
		Cipher.__init__(self, key, alphabet)

	def encrypt(self, text):
		text = self.prep_text(text)
		ciphertext = ""
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				new_char = self.key[self.alphabet.index(new_char)]
			if c.islower() and self.keep_case:
				new_char = new_char.lower()
			ciphertext += new_char
		return ciphertext
		
	def decrypt(self, text, keep_spaces=True, keep_punct=True, keep_num=True):
		## if ciphertext has punctuation, spaces and numbers, no harm in keepng them for plaintext 
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
		
	## Decryption with partial decryption dictionary
	def partial_decrypt(self, text, decrypt_dict):
		text = text.lower()
		for c, p in decrypt_dict.items():
			if p != None:
				text = text.replace(c.lower(), p.upper())
		return text
			
		
		
