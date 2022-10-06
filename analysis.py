import myciphers
uppercase = myciphers.Cipher.uppercase

def freq_analysis():
	exit = False
	while not exit:
		print("\n\n\n")
		choice = get_int_choice("Frequency Analysis:\n"
  								+ "1 - Single Letter Frequencies\n"
								+ "9 - Back\n"
							   	, [1, 9])
		if choice == 1:
			text = myciphers.utility.raw_input("Enter Text To Analyse:")
			# Single letter frequency analysis
			frequencies = myciphers.utility.ngram(text, 1)
			for l in uppercase:
				if l not in frequencies.keys():
					frequencies.update({l:0})
			# Display results
			print("LETTER\tFREQUENCY")
			for k in frequencies:
				print(str(k) + "     \t" + str(frequencies[k]))
				

		elif choice == 9:
			exit = True





def get_int_choice(prompt, choices):
	success = False
	user_input = None
	while not success:
		print(prompt)
		user_input = input()
		try:
			user_input = int(user_input)
			if user_input in choices:
				success = True
			else:
				print("Please choose one of the listed options")
		except:
			print("Please enter an integer")

	return user_input
	


def menu():
	exit = False
	while not exit:
		choice = get_int_choice("Menu:\n" 
							+ "1 - Frequency Analysis\n"
				 			+ "9 - Exit\n"
							   , [1,9])
		if choice == 1:
			freq_analysis()
		elif choice == 9:
			choice == None

		
	


def main():
	menu()

		
		
		



main()