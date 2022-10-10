import sys
import math


## Initialise default English frequencies
class ngram_score():
	TEXTFILE_NAMES = [
	 "monograms.txt", "bigrams.txt", "trigrams.txt", "quadgrams.txt"
	]

	def __init__(self, default=True):

		folder = "myciphers/ngram_freqs/"
		if default:
			folder += "default/"
		else:
			folder += "custom/"
		## setup list to store dictionaries of ngram counts
		## ngrams[i] returns n = i+1 ngrams
		self.ngrams = [{}, {}, {}, {}]
		self.totals = [0, 0, 0, 0]
		self.log_probs = [{}, {}, {}, {}]
		for i in range(len(self.ngrams)):
			self.ngrams[i] = self.load_ngram_file(folder + self.TEXTFILE_NAMES[i])
			self.totals[i] = sum([int(x) for x in self.ngrams[i].values()])
			self.log_probs[i] = self.load_log_probs(self.ngrams[i], self.totals[i])

	def load_ngram_file(self, filename, sep=' '):
		ngram_dict = {}
		for line in open(filename):
			key, count = line.split(sep)
			ngram_dict.update({key: count.strip("\n")})
		return ngram_dict

	def load_log_probs(self, ngram_dict, total):
		log_probs = {}
		for key in ngram_dict.keys():
			log_probs[key] = math.log10(float(ngram_dict[key]) / total)
		return log_probs

	def get_ngram_dict(self, n):
		if n > 0 and n < 5:
			return self.ngrams[n - 1]
		else:
			return {}

	def get_ngram_totals(self, n):
		if n > 0 and n < 5:
			return self.totals[n - 1]
		else:
			return 0

	def calc_fitness(self, text, n=4):
		score = 0
		for i in range(len(text) - n):
			string = text[i:i + n]
			if string in self.log_probs[n - 1].keys():
				score += self.log_probs[n - 1][string]
			else:
				score += math.log10(0.01 / self.totals[n - 1])
		return score


## GLOBAL NGRAM COUNTER
expected_ngrams = ngram_score()


## ngram score related funtions
def get_expected_ngrams(n, count=26):
	shortened_dict = {}
	ngram_dict = expected_ngrams.get_ngram_dict(n)
	keys = list(ngram_dict.keys())
	for i in range(min(len(ngram_dict), count)):
		key = keys[i]
		shortened_dict.update({key: ngram_dict[key]})
	return shortened_dict


def order_by_english_likelihood(decryptions, n=4):
	decrypt_scores = {}
	for d in decryptions:
		decrypt_scores.update({d: expected_ngrams.calc_fitness(d, n)})
	decrypt_scores = sort_result(decrypt_scores)
	return decrypt_scores


### FITNESS CALCULATORS
### IOC Calculator
def calc_ioc(text):
	text = text.upper().replace(" ",
	                            "").replace("!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~",
	                                        "")
	freqs = ngram(text, 1)
	ioc = 0
	for c in freqs:
		c_count = freqs[c]
		charIOC = (c_count * (c_count - 1)) / (len(text) * (len(text) - 1))
		ioc += charIOC
	return ioc


### CHI SQUARED STATISTIC
def calc_chi_squared(text):
	text = text.upper().replace(" ",
	                            "").replace("!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~",
	                                        "")
	text_length = len(text)
	freqs = ngram(text, 1)
	expected_freqs = expected_ngrams.get_ngram_dict(1)
	chi_squared = 0
	for char in expected_freqs:
		expected_prob = int(
		 expected_freqs[char]) / expected_ngrams.get_ngram_totals(1)
		expected_count = text_length * expected_prob
		actual_count = 0
		if char in freqs:
			actual_count = freqs[char]
		result = ((actual_count - expected_count)**2) / expected_count
		chi_squared += result
	return chi_squared


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


## FREQUENCY ANALYSIS ##
def ngram(text, n=1, continuous=True, ignore_case=True, ignore_spaces=True):
	frequencies = {}
	increment = 1
	if not continuous:
		increment = n
	if ignore_case:
		text = text.upper()
	if ignore_spaces:
		text = text.replace(" ", "")

	for i in range(0, len(text), increment):
		substring = text[i:i + n]
		if substring in frequencies:
			frequencies.update({substring: frequencies[substring] + 1})
		else:
			frequencies.update({substring: 1})
	return sort_result(frequencies)


def sort_result(freq_dict):
	sorted_dict = dict(
	 sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))
	return sorted_dict


def display_result(sorted_freqs, count=26, comparison=True, percentages=True):
	# If empty, return nothing
	if len(sorted_freqs) < 1:
		return

	# Variables
	keys = list(sorted_freqs.keys())
	n = len(keys[0])
	total_count = sum(list(sorted_freqs.values()))
	comparisons = get_expected_ngrams(n, count)
	compkeys = list(comparisons.keys())

	## PRINT LINES
	print()
	line_template = "{0:8}\t{1:8}\t\t{2:8}\t{3:8}"

	if comparison:
		print(line_template.format("INPUT FREQS", "", "NORMAL FREQS", ""))
		print(
		 line_template.format("LETTER(S)", "FREQUENCY", "LETTER(S)", "FREQUENCY"))
	else:
		print(line_template.format("INPUT FREQS", "", "", ""))
		print(line_template.format("LETTER(S)", "FREQUENCY", "", ""))

	for i in range(count):
		letter1 = keys[i]
		freq1 = sorted_freqs[letter1]
		letter2 = ""
		freq2 = ""
		if percentages:
			freq1 = "{0:.3%}".format(freq1 / total_count)
		## Add comparisons
		if comparison:
			if len(compkeys) > i:
				letter2 = compkeys[i]
				freq2 = int(comparisons[letter2])
				if percentages:
					freq2 = "{0:.3%}".format(freq2 / expected_ngrams.get_ngram_totals(n))
		print(line_template.format(letter1, freq1, letter2, freq2))


## SIMPLE TEXT FUNCTIONS ##
def get_length(text, ignore_spaces=True, ignore_punctuation=True):
	if ignore_spaces:
		text = text.replace(" ", "")
	if ignore_punctuation:
		for c in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
			text = text.replace(c, "")
	return len(text)


def get_factors(num):
	factors = []
	for i in range(1, int(num**0.5) + 1):
		if num % i == 0:
			if i not in factors:
				factors.append(i)
			if num / i not in factors:
				factors.append(int(num / i))
	return sorted(factors)
