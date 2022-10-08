import sys
## Initialise default English frequencies
class ngram_score():
	TEXTFILE_NAMES = ["monograms.txt","bigrams.txt","trigrams.txt","quadgrams.txt"]
	def __init__(self, default = True):
		
		folder = "myciphers/ngram_freqs/"
		if default:
			folder += "default/"
		else:
			folder += "custom/"
		## setup list to store dictionaries of ngram counts
		## ngrams[i] returns n = i+1 ngrams
		self.ngrams = [{}, {}, {}, {}]
		self.totals = [0, 0, 0, 0]
		for i in range(len(self.ngrams)):
			self.ngrams[i] = self.load_ngram_file(folder+self.TEXTFILE_NAMES[i])
			self.totals[i] = sum([int(x) for x in self.ngrams[i].values()])
			
	def load_ngram_file(self, filename, sep = ' '):
		ngram_dict = {}
		for line in open(filename):
			key, count = line.split(sep)
			ngram_dict.update({key:count.strip("\n")})
		return ngram_dict

	def get_ngram_dict(self, n):
		if n > 0 and n < 5:
			return self.ngrams[n-1]
		else:
			return {}

	def get_ngram_totals(self, n):
		if n > 0 and n < 5:
			return self.totals[n-1]
		else:
			return 0

## GLOBAL NGRAM COUNTER
expected_ngrams = ngram_score()

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



## SIMPLE TEXT FUNCTIONS ##
def get_length(text, ignore_spaces = True, ignore_punctuation = True):
	if ignore_spaces:
		text = text.replace(" ","")
	if ignore_punctuation:
		for c in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
			text = text.replace(c, "")
	return len(text)

def get_factors(num):
	factors = []
	for i in range(1, int(num**0.5)+1):
		if num % i == 0:
			if i not in factors:
				factors.append(i)
			if num / i not in factors:
				factors.append(int(num/i))
	return sorted(factors)



## FREQUENCY ANALYSIS ##
def ngram(text, n=1, continuous = True, ignore_case = True, ignore_spaces = True):
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
    return sort_result(frequencies)

def sort_result(freq_dict):
    sorted_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1]))
    return sorted_dict

def display_result(sorted_freqs, count = 26, comparison = True, percentages = True):
	# If empty, return nothing
	if len(sorted_freqs) < 1:
		return
		

	# Input text variables
	keys = list(sorted_freqs.keys())
	n = len(keys[0])
	total_count = sum(list(sorted_freqs.values()))

	# Comparison variables
	comparisons = get_expected_ngrams(n, count)
	compkeys = list(comparisons.keys())

	
	# SETUP HEADER
	subtitle = "INPUT FREQS"
	header = "LETTER(S)"
	if n > len(header):
		header += " "*(n-len(header))
		subtitle += " "*(n-len(header))
	gap = " "*(len(header)-n)
	header += "\tFREQUENCY"
	if comparison:
		subtitle += "\t" + " "*(len("FREQUENCY")) + "\t\t" + "NORMAL FREQS"
		header += "\t\t" + header
	## HEADERS
	print()
	print(subtitle)
	print(header)
	## PRINT LINES
	for i in range(count):
		line = ""
		k = keys[i]
		freq = str(sorted_freqs[k])
		# Convert freq to percentages
		if percentages:
			freq = int(freq) / total_count
			freq = "{0:.3%}".format(freq)
		line += k + gap + "\t" + freq + " "*(len("FREQUENCY") - len(str(freq)))
		# Add Comparison section
		if comparison:
			if len(compkeys) > i:
				line += "\t\t"
				k = compkeys[i]
				freq = comparisons[k]
				if percentages:
					freq = int(freq) / expected_ngrams.get_ngram_totals(n)
					freq = "{0:.3%}".format(freq)
				line += k + gap + "\t" + freq
		print(line)
	
def get_expected_ngrams(n, count = 26):
	shortened_dict = {}
	ngram_dict = expected_ngrams.get_ngram_dict(n)
	keys = list(ngram_dict.keys())
	for i in range(min(len(ngram_dict), count)):
		key = keys[i]
		shortened_dict.update({key:ngram_dict[key]})
	return shortened_dict
	


		





