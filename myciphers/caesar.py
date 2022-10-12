from myciphers.cipher import Cipher
import myciphers.config as config

class Caesar(Cipher):
	def __init__(self, key = 13, alphabet = config.alphabet_upper, detailed = config.detailed):
		self.alphabet = alphabet
		Cipher.__init__(self, key % len(self.alphabet), detailed)

	
	def encrypt(self, text):
		## \/ TEACHING SECTION \/ ##
		if self.detailed:
			print("\nUsing Caesar Cipher shift {0} to encrypt text".format(self.key))
		## /\ TEACHING SECTION /\ ##
			
		text = self.prep_text(text)
		ciphertext = ""
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				new_index = (self.alphabet.index(new_char) + self.key) % len(self.alphabet)
				new_char = self.alphabet[new_index]

			if c.islower() and self.keep_case:    
				new_char = new_char.lower()
			ciphertext += new_char
			
			## \/ TEACHING SECTION \/ ##
			if self.detailed:
				print("\nThe Plaintext Character is '{0}',we shift right by '{1}', and get '{2}'".format(c.upper(), self.key, new_char))
				print(self.alphabet.lower().replace(c.lower(), c.upper()).replace(new_char.lower(), new_char.upper()))
				print("\nWe now have {0}".format(ciphertext))
				input()
			## /\ TEACHING SECTION /\ ##
		return ciphertext

	
	def decrypt(self, text):
		## \/ TEACHING SECTION \/ ##
		if self.detailed:
			print("\nUsing Caesar Cipher shift {0} to decrypt text".format(self.key))
		## /\ TEACHING SECTION /\ ##
			
		text = self.prep_text(text)
		plaintext = ""
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				new_index = (self.alphabet.index(new_char) + (len(self.alphabet) - self.key)) % len(self.alphabet)
				new_char = self.alphabet[new_index]

			if c.islower() and self.keep_case:
				new_char = new_char.lower()
			plaintext += new_char
			
			## \/ TEACHING SECTION \/ ##
			if self.detailed:
				print("\nThe Cipher Character is '{0}', we shift left by '{1}', and get '{2}'".format(c.upper(), self.key, new_char.upper()))
				print(self.alphabet.lower().replace(c.lower(), c.upper()).replace(new_char.lower(), new_char.upper()))
				print("\nWe now have {0}".format(plaintext))
				input()
			## /\ TEACHING SECTION /\ ##
		return plaintext