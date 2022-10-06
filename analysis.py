import myciphers as ciph
import ciph.utility as util
uppercase = ciph.Cipher.uppercase

### FREQUENCY ANALYSIS CHOICE ###
def freq_analysis():
	exit = False
	while not exit:
		print("\n\n\n")
		choice = util.get_int_choice("Frequency Analysis:\n"
  								+ "1 - Single Letter Frequencies\n"
								+ "9 - Back\n"
							   	, [1, 9])
		if choice == 1:
			text = util.raw_input("Enter Text To Analyse:")
			# Single letter frequency analysis
			frequencies = util.ngram(text, 1) 
			for l in uppercase:
				if l not in frequencies.keys():
					frequencies.update({l:0})
			# Display results
			print("LETTER\tFREQUENCY")
			for k in frequencies:
				print(str(k) + "     \t" + str(frequencies[k]))
				

		elif choice == 9:
			exit = True



### MENU ###
def menu():
	choices = {"Frequency Analysis":freq_analysis}
	util.display_menu("Menu", choices)

def main():
	menu()

main()