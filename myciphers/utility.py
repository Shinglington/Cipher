import sys

### USER INPUTS ###
def raw_input(prompt):
	lines = []
	print(prompt)
	lines = sys.stdin.readlines()
	return ' '.join(lines).replace("\n","")

def get_int_choice(prompt, choices = []):
	success = False
	user_input = None
	while not success:
		print(prompt)
		user_input = input().replace(" ","")
		try:
			user_input = int(user_input)
			if (user_input in choices) or len(choices) == 0:
				success = True
			else:
				print("Please choose one of the listed options")
		except:
			print("Please enter an integer")
	return user_input

def get_string_choice(prompt, length = 0):
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

def display_menu(title, choices): # Choices is a dictionary with keys as names and values as functions
	exit = False
	while not exit:
		print("\n\n\n")
		print(title)
		for i in range(1, len(choices) + 1):
			print("{index} - {choice}".format(index = i, choice = list(choices.keys())[i-1]))
		print("{index} - Exit".format(index = len(choices) + 1))

		user_choice = get_int_choice("", range(1, len(choices) + 2))
		if user_choice - 1 < len(choices):
			choices[list(choices.keys())[user_choice-1]]()
		elif user_choice == len(choices) + 1:
			exit = True
		else:
			print("Something went wrong")
			break



def ngram(text, n=1, continuous = True, display = False, ignore_case = True, ignore_spaces = True):
    frequencies = {}
    increment = 1
    if not continuous:
        increment = n
    if ignore_case:
    	text = text.upper()
    if ignore_spaces:
        text = text.replace(" ","")

		
    for i in range(0, len(text), increment):
        substring = text[i:i+n]
        if substring in frequencies:
            frequencies.update({substring:frequencies[substring]+1})
        else:
            frequencies.update({substring:1})

    return sort_result(frequencies, display)


def sort_result(freq_dict, display=False):
    sorted_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1]))
    if display:
        for k,v in sorted_dict:
            print(k + " : " + v)
    return sorted_dict










