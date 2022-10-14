import sys

### USER INPUTS ###
def raw_input(prompt):
	lines = []
	print(prompt)
	lines = sys.stdin.readlines()
	return ' '.join(lines).replace("\n", "")


def get_int_choice(prompt, choices=[]):
	success = False
	user_input = None
	while not success:
		print(prompt)
		user_input = input().replace(" ", "")
		try:
			user_input = int(user_input)
			if (user_input in choices) or len(choices) == 0:
				success = True
			else:
				print("Please choose one of the listed options")
		except:
			print("Please enter an integer")
	return user_input


def get_string_choice(prompt, length=0):
	success = False
	user_input = None
	while not success:
		print(prompt)
		user_input = input()
		if length != 0 and len(user_input) != length:
			print("Expected string length of " + str(length))
		else:
			success = True
	return user_input


def get_bool_choice(prompt):
	success = False
	user_input = None
	while not success:
		print(prompt + " (y/n)")
		user_input = input().strip(" ").upper()
		if user_input != "Y" and user_input != "N":
			print("Please enter y/n ")
		else:
			success = True

	if user_input == "Y":
		return True
	elif user_input == "N":
		return False
	else:
		print("Something went wrong")



def display_menu(
 title, choices
):  # Choices is a dictionary with keys as names and values as functions
	exit = False
	while not exit:
		print("\n\n\n")
		print(title)
		for i in range(1, len(choices) + 1):
			print("{index} - {choice}".format(index=i,
			                                  choice=list(choices.keys())[i - 1]))
		print("{index} - Exit".format(index=len(choices) + 1))

		user_choice = get_int_choice("", range(1, len(choices) + 2))
		if user_choice - 1 < len(choices):
			choices[list(choices.keys())[user_choice - 1]]()
		elif user_choice == len(choices) + 1:
			exit = True
		else:
			print("Something went wrong")
			break
