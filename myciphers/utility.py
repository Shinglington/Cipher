import math
import myciphers.config as config

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

### FITNESS CALCULATORS ##
	
### IOC Calculator
def calc_ioc(text):
	text = filter_text(text, keep_spaces = False, keep_punct = False, keep_num = False)
	freqs = ngram(text, 1)
	ioc = 0
	for c in freqs:
		c_count = freqs[c]
		charIOC = (c_count * (c_count - 1)) / (len(text) * (len(text) - 1))
		ioc += charIOC
	return ioc


### CHI SQUARED STATISTIC
def calc_chi_squared(text):
	text = filter_text(text, keep_spaces = False, keep_punct = False, keep_num = False)
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

### ORDER BY FITNESS SCORE
def order_by_likelihood(decryption_dict):
	key_fitness = {}
	for key in decryption_dict:
		text = decryption_dict[key]
		key_fitness[key] = expected_ngrams.calc_fitness(text)
	
	## sort by fitness
	decryption_dict = dict(sorted(decryption_dict.items(), key = lambda items : key_fitness[items[0]], reverse = True))

	return decryption_dict

def display_decryptions(decryption_dict, count = 3):
	print("\n\n\n###DECRYPTIONS ORDERED BY LIKELIHOOD###")
	decryptions = order_by_likelihood(decryption_dict)
	print("Most likely decryptions:")
	for i in range(count):
		key = list(decryptions.keys())[i]
		print("{0}. Key = {1}".format(i+1, key))
		print(decryptions[key])
		print("\n\n")

## FREQUENCY ANALYSIS ##
def ngram(text, 
		  n=1,
		  continuous=True, 
		  ignore_case=True, 
		  ignore_spaces=True,
		  ignore_punct=False):
	## GET NGRAMS AND FREQUENCIES
	frequencies = {}
	increment = 1
	if not continuous:
		increment = n
	text = filter_text(text, 
					   keep_case = not ignore_case, 
					   keep_spaces = not ignore_spaces,
					   keep_punct = not ignore_punct)
			  
	for i in range(0, len(text), increment):
		substring = text[i:i + n]
		if substring in frequencies:
			frequencies.update({substring: frequencies[substring] + 1})
		else:
			frequencies.update({substring: 1})
	return sort_dict(frequencies)


def display_freqs(sorted_freqs, count=26, comparison=True, percentages=True):
	# If empty, return nothing
	if len(sorted_freqs) < 1:
		return

	# Variables
	keys = list(sorted_freqs.keys())
	n = len(keys[0])
	total_count = sum(list(sorted_freqs.values()))
	comparisons = get_expected_ngrams(n, count)
	compkeys = list(comparisons.keys())

	## PRINT FREQUENCIES AND COMPARISONS ##
	print()
	line_template = "{0:8}\t{1:8}\t\t{2:8}\t{3:8}"
	if comparison:
		print(line_template.format("INPUT FREQS", "", "NORMAL FREQS", ""))
		print(
		 line_template.format("LETTER(S)", "FREQUENCY", "LETTER(S)", "FREQUENCY"))
	else:
		print(line_template.format("INPUT FREQS", "", "", ""))
		print(line_template.format("LETTER(S)", "FREQUENCY", "", ""))

	for i in range(min(count, len(keys))):
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
def get_length(text, 
			   ignore_spaces=True, 
			   ignore_punctuation=True):
	return len(filter_text(text, 
						   keep_spaces = not ignore_spaces, 
						   keep_punct = not ignore_punctuation))

def get_factors(num):
	factors = []
	for i in range(1, int(num**0.5) + 1):
		if num % i == 0:
			if i not in factors:
				factors.append(i)
			if num / i not in factors:
				factors.append(int(num / i))
	return sorted(factors)

def filter_text(text, filter = "", 
				keep_spaces = True, 
				keep_punct = True, 
				keep_num = True, 
				keep_case = True):
		output = ""
		if not keep_spaces:
			filter += ' '
		if not keep_punct:
			filter += config.punctuation
		if not keep_num:
			filter += config.numbers
		if not keep_case:
			text = text.upper()
		for c in text:
			if c not in filter:
				output += c
		return output


## GENERAL ##
def sort_dict(unsorted_dict, 
			  reverse = True):
	sorted_dict = dict(sorted(unsorted_dict.items(), key = lambda item : item[1], reverse=reverse))
	return sorted_dict


## MATHEMATICAL FUNCTIONS
def modular_inverse(x, modulo = 26):
	inverse = -1
	for i in range(1, modulo):
		if (x*i) % modulo == 1:
			inverse = i
			break
	return inverse

	
	
	
# Matrices
def matrix_multiply(a, b):
	assert len(a[0]) == len(b)
	product = []
	for row in range(len(a)):
		new_row = []
		for col in range(len(b[row])):
			new_item = 0
			for i in range(len(a[row])):
				new_item += a[row][i] * b[i][col]
			new_row.append(new_item)
		product.append(new_row)
	return product
			
	

def matrix_determinant(matrix):
	if len(matrix) == 2:
		## matrix in form [[a, b], [c, d]]
		a = matrix[0][0]
		b = matrix[0][1]
		c = matrix[1][0]
		d = matrix[1][1]
		return (a*d) - (b*c)
	else:
		determinant = 0
		cofactors = matrix_cofactors(matrix)
		for j in range(len(matrix)):
			determinant += matrix[0][j] * cofactors[0][j]
		return determinant
	
def matrix_cofactors(matrix):
	cofactor_matrix = []
	## find cofactor of each element in matrix
	for row in range(len(matrix)):
		cofactor_row = []
		for col in range(len(matrix)):
			minor = matrix_determinant(matrix_minor(matrix, row, col))
			cofactor = minor * ((-1)**(row+col))
			cofactor_row.append(cofactor)
		cofactor_matrix.append(cofactor_row)
	return cofactor_matrix

def matrix_minor(matrix, row, col):
	minor = []
	for i in range(len(matrix)):
		if i != row:
			minor_row = []
			for j in range(len(matrix)):
				if j != col:
					minor_row.append(matrix[i][j])
			minor.append(minor_row)
	return minor

def transpose_matrix(matrix):
	transposed = []
	for j in range(len(matrix)):
		new_row = []
		for i in range(len(matrix)):
			new_row.append(matrix[i][j])
		transposed.append(new_row)
	return transposed 

