import myciphers as ciph
import myciphers.utility as util
import myciphers.config as config
 
def MONO_SUB(): 
	### MONOALPHABETIC SUBSTITUTION ###
	choices = {"Caesar":caesar,
			   "Affine Cipher":affine,
			   "Simple Substitution":simple_substitution,
			   "Keyword Substitution":keyword_substitution
}
	util.display_menu("Monoalphabetic Substitution Ciphers", choices)
def caesar():
	def encrypt():
		text = util.raw_input("Enter Plaintext: ")
		shift = util.get_int_choice("Enter Shift: ", range(0,26))
		print(ciph.Caesar(shift).encrypt(text))
			
	def decrypt():
		def known_key():
			text = util.raw_input("Enter Ciphertext:")
			shift = util.get_int_choice("Enter Shift:", range(0,26))
			print(ciph.Caesar(shift).decrypt(text))
		def brute_force():
			text = util.raw_input("Enter Ciphertext:")
			decryptions = ciph.Caesar.brute_force_decrypt(text)
			util.display_decryptions(decryptions)
			
		choices = {"Known Key":known_key
				  ,"Brute Force":brute_force}
		util.display_menu("Decryption", choices)

	## UI ##
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	util.display_menu("Caesar Cipher", choices)


def affine():
	def encrypt():
		print("")
		text = util.raw_input("Enter Plaintext: ")
		a = util.get_int_choice("Enter a:", range(0,26))
		b = util.get_int_choice("Enter b:", range(0,26))
		print(ciph.Affine(a, b).encrypt(text))
			
	def decrypt():
		def known_key():
			text = util.raw_input("Enter Ciphertext:")
			a = util.get_int_choice("Enter a:", range(0,26))
			b = util.get_int_choice("Enter b:", range(0,26))
			if ciph.Affine.calc_inverse_key(a) != -1:
				print(ciph.Affine(a, b).decrypt(text))
			else:
				print("Invalid 'a' value, no inverse exists")
					
		def brute_force():
			text = util.raw_input("Enter Ciphertext:")
			decryptions = ciph.Affine.brute_force_decrypt(text)
			util.display_decryptions(decryptions)
			
		choices = {"Known Key":known_key
				  ,"Brute Force":brute_force}
		util.display_menu("Decryption", choices)

	## UI ##
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	util.display_menu("Affine Cipher", choices)
	
def simple_substitution():
	
	def encrypt():
		text = util.raw_input("Enter Plaintext: ")
		key = util.get_string_choice("Enter Corresponding Cipher Alphabet\n" + config.alphabet_upper + "\n            \/", 26)
		print(ciph.SimpleSub(key).encrypt(text))

	def decrypt():
		def normal_decrypt():
			text = util.raw_input("Enter Ciphertext: ")
			key = util.get_string_choice("Enter Cipher Alphabet used\n" + ciph.Cipher.uppercase + "\n            /\\", 26)
			print(ciph.SimpleSub(key).decrypt(text))

		def partial_decrypt():
			done = False
			text = util.raw_input("Enter Ciphertext: ").lower()
			partial_alphabet = {} ## Stores partial cipher -> plain alphabet
			## Initialise dictionary
			for letter in config.alphabet_upper:
				partial_alphabet.update({letter:None})
			## Loop trial and error decryption
			while not done:
				## Display current partial_alphabet
				print("CIPHERTEXT\tPLAINTEXT")
				for c, p in partial_alphabet.items():
					if p == None:
						p = ""
					print("{0}         -> {1}".format(c, p))
				## Get any new cipher -> plain letters
				print("Enter * to exit after next display")
				ciph_letter = util.get_string_choice("Enter Cipher Letter", 1).upper()
				plain_letter = util.get_string_choice("Enter Plaintext Letter (Enter a space to set to None)", 1).upper()
				if ciph_letter == "*" or plain_letter == "*":
					done = True
							
				if ciph_letter in partial_alphabet.keys():
					if plain_letter == " ":
						partial_alphabet.update({ciph_letter:None})
					else:
						if plain_letter not in partial_alphabet.values():
							partial_alphabet.update({ciph_letter:plain_letter})
						else:
							print("Plaintext letter is already assigned")
							input()
				## Display new decryption
				print(ciph.SimpleSub().partial_decrypt(text, partial_alphabet))
				print()

				
		choices = {"Known Cipher Alphabet":normal_decrypt
				  ,"Trial And Error":partial_decrypt}
		util.display_menu("", choices)

	## UI ##
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	util.display_menu("Simple Substitution Cipher", choices)


	


def keyword_substitution():
	def encrypt():
		text = util.raw_input("Enter Plaintext: ")
		keyword = util.get_string_choice("Enter keyword: ")
		print(ciph.KeywordSub(keyword).encrypt(text))

	def decrypt():
		def normal_decrypt():
			text = util.raw_input("Enter Ciphertext: ")
			keyword = util.get_string_choice("Enter keyword: ")
			print(ciph.KeywordSub(keyword).decrypt(text))
		def dictionary_attack():
			text = util.raw_input("Enter Ciphertext: ")
			decryptions = ciph.KeywordSub.dictionary_attack(text)
			util.display_decryptions(decryptions)
		
		choices = {"Known Keyword":normal_decrypt
				  ,"Dictionary Attack":dictionary_attack}
		util.display_menu("", choices)

	## UI ##
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	util.display_menu("Simple Substitution Cipher", choices)

def POLY_SUB(): 
	### POLYALPHABETIC SUBSTITUTION ###
	choices = {"Vigenere":vigenere}
	util.display_menu("Monoalphabetic Substitution Ciphers", choices)

def vigenere():
	import myciphers.vigenere as vig
	def encrypt():
		text = util.raw_input("Enter Plaintext: ")
		key = util.get_string_choice("Enter Key")
		print(ciph.Vigenere(key).encrypt(text))
	def decrypt():
		def known_key():
			text = util.raw_input("Enter Ciphertext: ")
			key = util.get_string_choice("Enter Key")
			print(ciph.Vigenere(key).decrypt(text))
		def guess_key():
			text = util.raw_input("Enter Ciphertext: ")
			known_length = util.get_bool_choice("Do you know the key length?")
			key_length = 0
			if known_length:
				key_length = util.get_int_choice("Enter key length:")
			guessed_keys = vig.guess_key(text, key_length)
			# Add all key and decryption combinations to a dictionary
			possible_decryptions = {}
			for k in guessed_keys:
				# replace unknowns with "A"
				k = k.replace("?", "A")
				possible_decryptions.update({k:ciph.Vigenere(k).decrypt(text)})
			# sort dictionary by decryption ioc
			possible_decryptions = dict(sorted(possible_decryptions.items(), key = lambda item : util.expected_ngrams.calc_fitness(item[1]), reverse = True))
			
			# show top 5 results
			print("Most likely results")
			print("\n\n")
			for i in range(min(5, len(possible_decryptions))):
				key = list(possible_decryptions.keys())[i]
				print("{0} : key = {1}".format(i+1, key))
				print(possible_decryptions[key])
				print("\n\n")
				

		choices = {"Known Key":known_key
				  ,"Attempt to Guess Key":guess_key}
		util.display_menu("Decryption", choices)
		
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	util.display_menu("Vigenere Cipher", choices)



def TRANSPOSITION():
	### TRANSPOSITION ###
	choices = {"Column Transposition":col_trans}
	util.display_menu("Transposition Ciphers", choices)

def col_trans():
	def encrypt():
		text = util.raw_input("Enter Plaintext")
		key = util.get_string_choice("Enter Key")
		print(ciph.ColTrans(key).encrypt(text))
	def decrypt():
		text = util.raw_input("Enter Cipher Text")
		key = util.get_string_choice("Enter Key")
		print(ciph.ColTrans(key).decrypt(text))

		
	## UI ##
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	util.display_menu("COLUMN TRANSPOSITION CIPHER", choices)

### MENU ###
def main():
	choices = {"Monoalphabetic Substitution":MONO_SUB
			  ,"Polyalphabetic Substitution":POLY_SUB
			  ,"Transposition":TRANSPOSITION}
	util.display_menu("Menu", choices)

if __name__ == "__main__":
	main()