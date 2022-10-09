from myciphers.cipher import SubCipher
class Affine(SubCipher):
	def __init__(self, key = [5, 8], alphabet = SubCipher.uppercase, keep_case  = False): 
		## key in form [a, b]
		SubCipher.__init__(key, alphabet, keep_case)

	def check_valid_key(self):
		valid = False
		return valid

	def calc_inverse_key():
		a = key[0]
		b = key[1]
		
	
	def encrypt(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
		text = self.prep_text(text, keep_spaces, keep_punct, keep_num)
		ciphertext = ""
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				# new index = (a * current index + b) % 26
				new_index = (self.key[0] * self.alphabet.index(new_char) + self.key[1]) % 26
				new_char = self.alphabet[new_index]
			if c.islower() and self.keep_case:
				new_char = new_char.lower()
			ciphertext += new_char
		return ciphertext

	def decrypt(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
		text = self.prep_text(text, keep_spaces, keep_punct, keep_num)
		plaintext = ""
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				# cipher index = (a * plain index + b) % 26
				# plain index =  c * (cipherindex - b) % 26
				# c is modular multiplicative inverse of a
				new_index = (self.key[0] * self.alphabet.index(new_char) + self.key[1]) % 26
				new_char = self.alphabet[new_index]
			if c.islower() and self.keep_case:
				new_char = new_char.lower()
			ciphertext += new_char
		return plaintext
		
		
    

