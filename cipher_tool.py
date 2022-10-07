import myciphers as ciph
import myciphers.utility as util

### MONOALPHABETIC SUBSTITUTION ###
def mono_sub():
	choices = {"Caesar":caesar}
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
			text = util.raw_input("Enter Plaintext Text: ")
			shift = util.get_int_choice("Enter Shift: ", range(0,26))
			print(ciph.Caesar(shift).encrypt(text))
		elif choice == 2:
			text = util.raw_input("Enter Cipher Text: ")
			shift = util.get_int_choice("Enter Shift: ", range(0,26))
			print(ciph.Caesar(shift).decrypt(text))
	
			
### POLYALPHABETIC SUBSTITUTION ###
def poly_sub():
	pass


### TRANSPOSITION ###
def transposition():
	pass

### MENU ###
def main():
	choices = {"Monoalphabetic Substitution":mono_sub
			  ,"Polyalphabetic Substitution":poly_sub
			  ,"Transposition":transposition}
	util.display_menu("Menu", choices)

if __name__ == "__main__":
	main()