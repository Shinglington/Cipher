import myciphers as ciph
import myciphers.utility as util

def mono_sub():
	exit = False
	while not exit:
		print("\n\n\n")
		choice = util.get_int_choice("Monoalphabetic Substitution:\n"
  								+ "1 - Caesar\n"
								+ "9 - Back\n"
							   	, [1, 9])
		if choice == 1:
			text = util.raw_input("Enter Cipher Text: ")
			shift = util.get_int_choice("Enter Shift: ", range(0,26))
			print(ciph.Caesar(shift).decrypt(text))
		elif choice == 9:
			exit = True

def poly_sub():
	pass

def transposition():
	pass

### MENU ###
def menu():
	choices = {"Monoalphabetic Substitution":mono_sub
			  ,"Polyalphabetic Substitution":poly_sub
			  ,"Transposition":transposition}
	util.display_menu("Menu", choices)

def main():
	menu()

main()