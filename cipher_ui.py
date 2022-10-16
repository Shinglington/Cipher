from console_io import raw_input, get_int_choice, get_bool_choice, get_string_choice, display_menu
import myciphers as ciph
import myciphers.utility as util
import myciphers.config as config
 
def MONO_SUB(): 
	### MONOALPHABETIC SUBSTITUTION ###
	choices = {"Caesar":caesar,
			   "Affine Cipher":affine,
			   "Simple Substitution":simple_substitution,
			   "Keyword Substitution":keyword_substitution,
			   "Polybius Square":polybius_square,
			   "Baconian Cipher":baconian
}
	display_menu("Monoalphabetic Substitution Ciphers", choices)
def caesar():
	def encrypt():
		text = raw_input("Enter Plaintext: ")
		shift = get_int_choice("Enter Shift: ", range(0,26))
		print(ciph.Caesar(shift).encrypt(text))
			
	def decrypt():
		def known_key():
			text = raw_input("Enter Ciphertext:")
			shift = get_int_choice("Enter Shift:", range(0,26))
			print(ciph.Caesar(shift).decrypt(text))
		def brute_force():
			text = raw_input("Enter Ciphertext:")
			decryptions = ciph.Caesar.brute_force(text)
			util.display_decryptions(decryptions)
			
		choices = {"Known Key":known_key
				  ,"Brute Force":brute_force}
		display_menu("Decryption", choices)

	## UI ##
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	display_menu("Caesar Cipher", choices)


def affine():
	def encrypt():
		print("")
		text = raw_input("Enter Plaintext: ")
		a = get_int_choice("Enter a:", range(0,26))
		b = get_int_choice("Enter b:", range(0,26))
		print(ciph.Affine(a, b).encrypt(text))
			
	def decrypt():
		def known_key():
			text = raw_input("Enter Ciphertext:")
			a = get_int_choice("Enter a:", range(0,26))
			b = get_int_choice("Enter b:", range(0,26))
			if util.modular_inverse(a) != -1:
				print(ciph.Affine(a, b).decrypt(text))
			else:
				print("Invalid 'a' value, no inverse exists")
					
		def brute_force():
			text = raw_input("Enter Ciphertext:")
			decryptions = ciph.Affine.brute_force(text)
			util.display_decryptions(decryptions)
			
		choices = {"Known Key":known_key
				  ,"Brute Force":brute_force}
		display_menu("Decryption", choices)

	## UI ##
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	display_menu("Affine Cipher", choices)
	
def simple_substitution():
	
	def encrypt():
		text = raw_input("Enter Plaintext: ")
		key = get_string_choice("Enter Corresponding Cipher Alphabet\n" + config.alphabet_upper + "\n            \/", 26)
		print(ciph.SimpleSub(key).encrypt(text))

	def decrypt():
		def normal_decrypt():
			text = raw_input("Enter Ciphertext: ")
			key = get_string_choice("Enter Cipher Alphabet used\n" + ciph.Cipher.uppercase + "\n            /\\", 26)
			print(ciph.SimpleSub(key).decrypt(text))

		def partial_decrypt():
			done = False
			text = raw_input("Enter Ciphertext: ").lower()
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
				ciph_letter = get_string_choice("Enter Cipher Letter", 1).upper()
				plain_letter = get_string_choice("Enter Plaintext Letter (Enter a space to set to None)", 1).upper()
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
		display_menu("", choices)

	## UI ##
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	display_menu("Simple Substitution Cipher", choices)


def keyword_substitution():
	def encrypt():
		text = raw_input("Enter Plaintext: ")
		keyword = get_string_choice("Enter keyword: ")
		print(ciph.KeywordSub(keyword).encrypt(text))

	def decrypt():
		def normal_decrypt():
			text = raw_input("Enter Ciphertext: ")
			keyword = get_string_choice("Enter keyword: ")
			print(ciph.KeywordSub(keyword).decrypt(text))
		def dictionary_attack():
			text = raw_input("Enter Ciphertext: ")
			decryptions = ciph.KeywordSub.dictionary_attack(text)
			util.display_decryptions(decryptions)
		
		choices = {"Known Keyword":normal_decrypt
				  ,"Dictionary Attack":dictionary_attack}
		display_menu("", choices)

	## UI ##
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	display_menu("Simple Substitution Cipher", choices)

def polybius_square():
	def encrypt():
		text = raw_input("Enter Plaintext: ")
		alphabet = None
		if get_bool_choice("Use custom square alphabet?"):
			alphabet = get_string_choice("Enter custom alphabet", length = 25)
		print(ciph.PolybiusSquare(alphabet).encrypt(text))
		
	def decrypt():
		text = raw_input("Enter Ciphertext: ")
		alphabet = None
		if get_bool_choice("Use custom square alphabet?"):
			alphabet = get_string_choice("Enter custom alphabet", length = 25)
		print(ciph.PolybiusSquare(alphabet).decrypt(text))

	## UI ##
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	display_menu("Polybius Square", choices)


def baconian():
	def encrypt():
		text = raw_input("Enter Plaintext: ")
		print(ciph.Baconian().encrypt(text))
		
	def decrypt():
		text = raw_input("Enter Ciphertext: ")
		print(ciph.Baconian().decrypt(text))
		
	## UI ##
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	display_menu("Baconian Cipher", choices)
	
def POLY_SUB(): 
	### POLYALPHABETIC SUBSTITUTION ###
	choices = {"Vigenere":vigenere}
	display_menu("Monoalphabetic Substitution Ciphers", choices)

def vigenere():
	def encrypt():
		text =raw_input("Enter Plaintext: ")
		key = get_string_choice("Enter Key")
		print(ciph.Vigenere(key).encrypt(text))
	def decrypt():
		def known_key():
			text = raw_input("Enter Ciphertext: ")
			key = get_string_choice("Enter Key")
			print(ciph.Vigenere(key).decrypt(text))
		def guess_key():
			text = raw_input("Enter Ciphertext: ")
			key_length = 0
			if get_bool_choice("Do you know the key length?"):
				key_length = get_int_choice("Enter key length:")
			decryptions = ciph.Vigenere.brute_force(text, key_length)
			util.display_decryptions(decryptions)

		choices = {"Known Key":known_key
				  ,"Attempt to Guess Key":guess_key}
		display_menu("Decryption", choices)
		
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	display_menu("Vigenere Cipher", choices)



def TRANSPOSITION():
	### TRANSPOSITION ###
	choices = {"Column Transposition":col_trans
			  ,"Railfence Cipher":rail_fence}
	display_menu("Transposition Ciphers", choices)

def col_trans():
	def encrypt():
		text = raw_input("Enter Plaintext")
		key = get_string_choice("Enter Key")
		print(ciph.ColTrans(key).encrypt(text))
	def decrypt():
		text = raw_input("Enter Cipher Text")
		key = get_string_choice("Enter Key")
		print(ciph.ColTrans(key).decrypt(text))

		
	## UI ##
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	display_menu("COLUMN TRANSPOSITION CIPHER", choices)

def rail_fence():
	def encrypt():
		text = raw_input("Enter Plaintext")
		key = get_int_choice("Enter Key")
		print(ciph.RailFence(key).encrypt(text))

	def decrypt():
		def known_key():
			text = raw_input("Enter Ciphertext")
			key = get_int_choice("Enter Key")
			print(ciph.RailFence(key).decrypt(text))

	
		def bruteforce():
			text = raw_input("Enter Ciphertext")
			decryptions = ciph.RailFence.brute_force_decrypt(text)
			util.display_decryptions(decryptions)

		choices = {"Known number of rails":known_key
				 ,"Unknown number of rails (bruteforce)":bruteforce}
		display_menu("Decryption", choices)
	## UI ##
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	display_menu("RAILFENCE CIPHER", choices)

def POLY_TRANS():
	### POLYGRAPHIC TRANSPOSITION CIPHERS
	choices = {"Playfair":playfair
			  ,"Hill":hill}
	display_menu("Polygraphic Transposition Ciphers", choices)

	
def playfair():
	def encrypt():
		text = raw_input("Enter Plaintext")
		keyword = get_string_choice("Enter Keyword")
		
		if not get_bool_choice("Use standard alphabet?"):
			alphabet = get_string_choice("Enter Custom Alphabet", 25)
			print(ciph.Playfair(ciph.Playfair.generate_grid_alphabet(keyword, alphabet)).encrypt(text))
		else:			
			print(ciph.Playfair(ciph.Playfair.generate_grid_alphabet(keyword)).encrypt(text))
			
		
	def decrypt():
		text = raw_input("Enter Ciphertext")
		keyword = get_string_choice("Enter Keyword")
		if not get_bool_choice("Use standard alphabet?"):
			alphabet = get_string_choice("Enter Custom Alphabet", 25)
			print(ciph.Playfair(ciph.Playfair.generate_grid_alphabet(keyword, alphabet)).decrypt(text))
		else:			
			print(ciph.Playfair(ciph.Playfair.generate_grid_alphabet(keyword)).decrypt(text))
			
	## UI ##
	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	display_menu("PLAYFAIR CIPHER", choices)
		

	
### MENU ###
def hill():
	def encrypt():
		text = raw_input("Enter Plaintext")
		matrix_string = get_string_choice("Enter Matrix String", alphabet_only = True)
		if len(matrix_string) ** 0.5 % 1 != 0:
			print("Matrix must be square")
		elif ciph.Hill.get_inverse(ciph.Hill.make_matrix(matrix_string.upper())) == None:
			print("Matrix must have inverse")
		else:
			print(ciph.Hill(matrix_string).encrypt(text))
		
	def decrypt():
		text = raw_input("Enter Ciphertext")
		matrix_string = get_string_choice("Enter Matrix String", alphabet_only = True)
		if len(matrix_string) ** 0.5 % 1 != 0:
			print("Matrix must be square")
		elif ciph.Hill.get_inverse(ciph.Hill.make_matrix(matrix_string.upper())) == None:
			print("Matrix must have inverse")
		else:
			print(ciph.Hill(matrix_string).decrypt(text))
			

	choices = {"Encrypt":encrypt
			  ,"Decrypt":decrypt}
	display_menu("HILL CIPHER", choices)
def main():
	choices = {"Monoalphabetic Substitution":MONO_SUB
			  ,"Polyalphabetic Substitution":POLY_SUB
			  ,"Transposition":TRANSPOSITION
			  ,"Polygraphic Transposition":POLY_TRANS}
	display_menu("Menu", choices)

if __name__ == "__main__":
	main()