import myciphers as ciph
import myciphers.utility as util

### MONOALPHABETIC SUBSTITUTION ###
def mono_sub():
	choices = {"Caesar":caesar
			  ,"Simple Substitution":simple_substitution}
	util.display_menu("Menu", choices)

def caesar():
	choice = 0
	while (choice != 3):
		print("\n\n\n")
		print("Caesar Cipher")
		choice = util.get_int_choice("1 - Encrypt\n" 
							+"2 - Decrypt\n"
							+"3 - Back\n", [1,2,3])
		if choice == 1:
			text = util.raw_input("Enter Plaintext: ")
			shift = util.get_int_choice("Enter Shift: ", range(0,26))
			print(ciph.Caesar(shift).encrypt(text))
		elif choice == 2:
			text = util.raw_input("Enter Ciphertext: ")
			shift = util.get_int_choice("Enter Shift (0 for bruteforce): ", range(0,26))
			if shift != 0:
				print(ciph.Caesar(shift).decrypt(text))
			else:
				for i in range(0, 26):
					print(ciph.Caesar(i).decrypt(text))
					print()
					print()

def simple_substitution():
	choice = 0
	while (choice != 3):
		print("\n\n\n")
		print("Simple Substitution Cipher")
		choice = util.get_int_choice("1 - Encrypt\n" 
							+"2 - Decrypt\n"
							+"3 - Back\n", [1,2,3])
		if choice == 1:
			text = util.raw_input("Enter Plaintext: ")
			key = util.get_string_choice("Enter Corresponding Cipher Alphabet\n" + ciph.Cipher.uppercase + "\n            \/", 26)
			print(ciph.SimpleSub(key).encrypt(text))
		elif choice == 2:
			subchoice = 0
			while (subchoice != 3):
				subchoice = util.get_int_choice("1 - Full Cipher Alphabet Known\n"
												+"2 - Trial and Error Decryption\n"
												+"3 - Back\n", [1,2,3])
				## Decryption with full alphabet known
				if choice == 1:
					text = util.raw_input("Enter Ciphertext: ")
					key = util.get_string_choice("Enter Cipher Alphabet used\n" + ciph.Cipher.uppercase + "\n            /\\", 26)
					print(ciph.SimpleSub(key).decrypt(text))
				## Partial decryption
				elif choice == 2:
					done = False
					text = util.raw_input("Enter Ciphertext: ").lower()
					partial_alphabet = {} ## Stores partial cipher -> plain alphabet
					## Initialise dictionary
					for letter in ciph.Cipher.uppercase:
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
						
### POLYALPHABETIC SUBSTITUTION ###



def poly_sub():
	pass


### TRANSPOSITION ###
def transposition():
	pass

def reverse_text():
	text = util.get_raw_input("Enter text to reverse")
	

### MENU ###
def main():
	choices = {"Monoalphabetic Substitution":mono_sub
			  ,"Polyalphabetic Substitution":poly_sub
			  ,"Transposition":transposition}
	util.display_menu("Menu", choices)

if __name__ == "__main__":
	main()