import myciphers



def freq_analysis():
	







def menu():
	exit = False
	while not exit:
		choice = None
		while choice == None:
			print("Menu:")
			print("1 - Frequency Analysis"
				 + "9 - Exit")
			input = input()
			try:
				choice = int(input)
				if choice == 1:
					freq_analysis()
				elif choice == 9:
					choice == None
				else:
					choice == 0
			except:
				print("Please enter an integer")
		
	


def main():
	menu()

		
		
		



main()