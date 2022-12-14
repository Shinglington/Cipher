import myciphers as ciph
from console_io import raw_input, get_int_choice, get_bool_choice, get_string_choice, display_menu
import myciphers.utility as util
import myciphers.config as config

def DEFAULT_TESTS():
	text = raw_input("Enter Text To Analyse:")
	ignore_spaces = get_bool_choice("Ignore spaces?")
	ignore_punct= get_bool_choice("Ignore punctuation?")
	ignore_case = get_bool_choice("Ignore case?")
	## IOC, length, factors
	length = util.get_length(text, ignore_spaces, ignore_punct)
	print("Text Length: " + str(length))
	print(print("Factors: " + str(util.get_factors(length))))
	print("IOC : {0}".format(util.calc_ioc(text)))
	
	## n-gram analysis
	for n in range(1, 4):
		freqs = util.ngram(text, n, True, 
							ignore_case, 
							ignore_spaces, 
							ignore_punct)
		util.display_freqs(freqs)

def FREQ_ANALYSIS():
	### FREQUENCY ANALYSIS CHOICE ###
	def single_letter_analysis():
		text = raw_input("Enter Text To Analyse:")
		ignore_spaces = get_bool_choice("Ignore spaces?")
		ignore_punct= get_bool_choice("Ignore punctuation?")
		ignore_case = get_bool_choice("Ignore case?")
		frequencies = util.ngram(text, 1, True, 
								 ignore_case, 
								 ignore_spaces, 
								 ignore_punct)
		## Get number of different characters found
		print("\n\n{0} total different characters found".format(len(list(frequencies.keys()))))
		alphabetic_count = 0
		for l in list(frequencies.keys()):
			if l in config.alphabet_upper or l in config.alphabet_lower:
				alphabetic_count+=1

		print("{0} different alphabetic characters found".format(alphabetic_count))
		util.display_freqs(frequencies)

	def n_gram_analysis():
		text = raw_input("Enter Text To Analyse:")
		n = get_int_choice("Enter length of strings to find frequencies for: ")
		continuous = get_bool_choice("Continuous analysis?"
									 +"\n(treat 'abcd' as 'ab', 'bc', 'cd' instead of 'ab', 'cd')\n")
		ignore_spaces = get_bool_choice("Ignore spaces?")
		ignore_punct= get_bool_choice("Ignore punctuation?")
		ignore_case = get_bool_choice("Ignore case?")
		frequencies = util.ngram(text, n, 
								 continuous, 
								 ignore_case, 
								 ignore_spaces, 
								 ignore_punct)
		util.display_freqs(frequencies)

	## UI ##
	choices = {"Single Letter Analysis":single_letter_analysis
			  ,"N-Gram Analysis":n_gram_analysis}
	display_menu("Frequency Analysis", choices)


def GENERAL():
	## GENERAL TOOLS ##
	choices = {"Factor Analysis":factor_analysis
			  ,"Expected Ngram Frequencies":get_expected_ngrams
			  ,"Calculate n-gram Fitness":calculate_fitness
			  ,"Calculate Index of Coincidence":calculate_ioc
			  ,"Calculate Chi Squared Score":calculate_chi_squared}
	display_menu("Other Tools", choices)

def factor_analysis():
	text = raw_input("Enter text to analyse:")
	ignore_spaces = get_bool_choice("Ignore spaces?")
	ignore_punct = get_bool_choice("Ignore punctuation?")
	length = util.get_length(text, ignore_spaces, ignore_punct)
	print("Text Length: " + str(length))
	print(print("Factors: " + str(util.get_factors(length))))

def get_expected_ngrams():
	n = get_int_choice("Enter n (1 to 4)", [1,2,3,4])
	util.display_result(util.get_expected_ngrams(n))


def calculate_fitness():
	text = raw_input("Enter text to analyse:")
	text = text.replace(ciph.Cipher.punctuation, "")
	text = text.replace(" ","")
	text = text.upper()
	n = get_int_choice("Enter n-gram length to analyse (1 to 4)", [1,2,3,4])
	score = util.expected_ngrams.calc_fitness(text, n)
	print("{0}-gram score is: {1}".format(n, score))

def calculate_ioc():
	text = raw_input("Enter text to analyse:")
	ioc = util.calc_ioc(text)
	print("IOC : {0}".format(ioc))

def calculate_chi_squared():
	text = raw_input("Enter text to analyse:")
	chi_squared = util.calc_chi_squared(text)
	print("Chi Squared Score: {0}".format(chi_squared))
	
	
### MENU ###
def main():
	choices = {"Default Analysis Test":DEFAULT_TESTS
			  ,"Frequency Analysis":FREQ_ANALYSIS
			  ,"Other Tools":GENERAL}
	display_menu("Menu", choices)

if __name__ == "__main__":
	main()