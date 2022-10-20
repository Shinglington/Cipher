from myciphers.cipher import Cipher
import myciphers.config as config
import myciphers.utility as util

class SimpleSub(Cipher):
	def __init__(self, key = config.alphabet_upper, 
				 alphabet = config.alphabet_upper,
				 detailed = config.detailed):
		Cipher.__init__(self, alphabet)
		self.key = key

	def encrypt(self, text):
		## \/ TEACHING SECTION \/ ##
		if self.detailed:
			print("\nUsing Simple Substitution Cipher to decrypt text" + "\nCipher Alphabet is {0}".format(self.key))
		## /\ TEACHING SECTION /\ ##
		text = self.prep_text(text, 
							  keep_punct = False)
		ciphertext = ""
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				new_char = self.key[self.alphabet.index(new_char)]
			if c.islower() and self.keep_case:
				new_char = new_char.lower()
			ciphertext += new_char
		return ciphertext
		
	def decrypt(self, text):
		## if ciphertext has punctuation, spaces and numbers, no harm in keeping them for plaintext 
		text = self.prep_text(text, 
							  keep_spaces = True,
							  keep_punct = True)
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

	def brute_force(text, max_iterations = 1000, alphabet = config.alphabet_upper):
		## Hill climbing
		import random
		max_key = alphabet
		max_score = -99e9
		## Generate random starting key
		key_streak = 0
		for i in range(max_iterations):
			current_key = ""
			remaining_alphabet = alphabet
			for j in range(0,26):
				key_char = remaining_alphabet[random.randint(0, len(alphabet) - j - 1)]
				current_key += key_char
				remaining_alphabet = remaining_alphabet.replace(key_char, "")
			
			current_score = util.expected_ngrams.calc_fitness(SimpleSub(current_key).decrypt(text))
			iterations = 0
			while (iterations < 1000):
				a = random.randint(0, 25)
				b = random.randint(0, 25)
				new_key = ""
				for j in range(len(current_key)):
					if j == a:
						new_key += current_key[b]
					elif j == b:
						new_key += current_key[a]
					else:
						new_key += current_key[j]
				score = util.expected_ngrams.calc_fitness(SimpleSub(new_key).decrypt(text))
				# check if new score better
				if score > current_score:
					current_key = new_key
					current_score = score
					iterations = 0
				iterations += 1

			if current_score > max_score:
				max_score = current_score
				max_key = current_key
				print("\nAfter iteration {0}, score is currently {1}".format(i, max_score))
				print(SimpleSub(max_key).decrypt(text))
				print("Key = {0}".format(max_key))
			else:
				key_streak += 1

			## if key streak over 10, break
			if key_streak > 10:
				break

		return SimpleSub(max_key).decrypt(text)

		
		
			
		
		
