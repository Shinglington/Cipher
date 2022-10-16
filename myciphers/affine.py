from myciphers.cipher import Cipher
import myciphers.config as config
import myciphers.utility as util

class Affine(Cipher):
	def __init__(self, a, b, 
				 alphabet = config.alphabet_upper,
				 detailed = config.detailed): 
		## key in form [a, b]
		Cipher.__init__(self, alphabet)
		self.modulo = len(self.alphabet)
		self.a = a
		self.b = b
		self.c = util.modular_inverse(a, self.modulo)
		assert self.c != -1
		
	def encrypt(self, text):
		## \/ DETAILED SECTION \/ ##
		if config.detailed:
			print("\n\n ## Affine Cipher Encryption"
				 + "\na = {0}, b = {1}".format(self.a, self.b))
		## /\ DETAILED SECTION /\ ##
		text = self.prep_text(text, keep_punct = False)
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

	def decrypt(self, text):
		## \/ DETAILED SECTION \/ ##
		if config.detailed:
			print("\n\n ## Affine Cipher Decryption"
				 + "\na = {0}, b = {1}, c = {2}"
				  .format(self.a, self.b, self.c)
				 + "\nWhere c is the modular multiplicative inverse of a")
		## /\ DETAILED SECTION /\ ##

		## No harm in keeping extra letters since they don't affect decryption
		text = self.prep_text(text, 
							  keep_punct = True, 
							  keep_spaces = True, 
							  keep_num = True)
		plaintext = ""
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				# cipher index = (a * plain index + b) % 26
				# plain index =  c * (cipherindex - b) % 26
				# c is modular multiplicative inverse of a
				new_index = (self.c * (self.alphabet.index(new_char) - self.b) % 26)
				new_char = self.alphabet[new_index]
			if c.islower() and self.keep_case:
				new_char = new_char.lower()
			plaintext += new_char
		return plaintext

	def brute_force(text, alphabet = config.alphabet_upper):
		## RETURNS DICTIONARY OF DECRYPTIONS ##
		decryptions = {} # dictionary where key is (a, b)
		for a in range(1, 26):
			for b in range(0, 26):
				# Check if inverse exists
				if util.modular_inverse(a) != -1:
					decrypt = Affine(a, b).decrypt(text)
					if config.detailed:
						print("\na = {0}, b = {1}".format(a, b))
						print(decrypt[0:min(len(decrypt), 20)] + "...")
					decryptions.update({(a,b):decrypt})
		return decryptions
		
		
    

