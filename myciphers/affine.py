from myciphers.cipher import Cipher
import myciphers.config as config

class Affine(Cipher):
	def __init__(self, a, b, alphabet = config.alphabet_upper): 
		## key in form [a, b]
		self.alphabet = alphabet
		self.a = a
		self.b = b

	def check_valid_key(self):
		valid = False
		return valid

	def calc_inverse_key(self):
		inverse = -1
		for i in range(1, 26, 2):
			if (self.a*i) % 26 == 1:
				inverse = i
		return inverse
		
	
	def encrypt(self, text):
		text = self.prep_text(text)
		ciphertext = ""
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				# new index = (a * current index + b) % 26
				new_index = (self.a * self.alphabet.index(new_char) + self.b) % 26
				new_char = self.alphabet[new_index]
			if c.islower() and self.keep_case:
				new_char = new_char.lower()
			ciphertext += new_char
		return ciphertext

	def decrypt(self, text, keep_spaces = True, keep_punct = True, keep_num = True):
		## No harm in keeping extra letters since they don't affect decryption
		text = self.prep_text(text, keep_spaces, keep_punct, keep_num)
		plaintext = ""
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				# cipher index = (a * plain index + b) % 26
				# plain index =  c * (cipherindex - b) % 26
				# c is modular multiplicative inverse of a
				new_index = (self.calc_inverse_key() * (self.alphabet.index(new_char) - self.b) % 26)
				new_char = self.alphabet[new_index]
			if c.islower() and self.keep_case:
				new_char = new_char.lower()
			plaintext += new_char
		return plaintext
		
		
    

