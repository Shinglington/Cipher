import myciphers as ciph
import myciphers.utility as util
uppercase = ciph.Cipher.uppercase


def FREQ_ANALYSIS():
	### FREQUENCY ANALYSIS CHOICE ###
	def single_letter_analysis():
		text = util.raw_input("Enter Text To Analyse:")
		frequencies = util.ngram(text, 1) 
		for l in uppercase:
			if l not in frequencies.keys():
				frequencies.update({l:0})
		util.display_result(frequencies)
				
	def n_gram_analysis():
		text = util.raw_input("Enter Text To Analyse:")
		n = util.get_int_choice("Enter length of strings to find frequencies for: ")
		continuous = util.get_bool_choice("Continuous analysis?\n(i.e. for n = 2 'abcd' returns 'ab','bc','cd' instead of 'ab', 'cd')\n")
		frequencies = util.ngram(text, n, continuous)
		util.display_result(frequencies)

	## UI ##
	choices = {"Single Letter Analysis":single_letter_analysis
			  ,"N-Gram Analysis":n_gram_analysis}
	util.display_menu("Frequency Analysis", choices)


def GENERAL():
	## GENERAL TOOLS ##
	choices = {"Factor Analysis":factor_analysis
			  ,"Expected Ngram Frequencies":get_expected_ngrams
			  ,"Calculate n-gram Fitness":calculate_fitness}
	util.display_menu("Other Tools", choices)

def factor_analysis():
	text = util.raw_input("Enter text to analyse:")
	ignore_spaces = util.get_bool_choice("Ignore spaces?")
	ignore_punct = util.get_bool_choice("Ignore punctuation?")
	length = util.get_length(text, ignore_spaces, ignore_punct)
	print("Text Length: " + str(length))
	print(print("Factors: " + str(util.get_factors(length))))

def get_expected_ngrams():
	n = util.get_int_choice("Enter n (1 to 4)", [1,2,3,4])
	util.display_result(util.get_expected_ngrams(n))


def calculate_fitness():
	text = util.raw_input("Enter text to analyse:")
	text = text.replace(ciph.Cipher.punctuation, "")
	text = text.replace(" ","")
	text = text.upper()
	n = util.get_int_choice("Enter n-gram length to analyse (1 to 4)", [1,2,3,4])
	score = util.expected_ngrams.calc_fitness(text, n)
	print("{0}-gram score is: {1}".format(n, score))
	
	
### MENU ###
def main():
	choices = {"Frequency Analysis":FREQ_ANALYSIS
			  ,"Other Tools":GENERAL}
	util.display_menu("Menu", choices)

if __name__ == "__main__":
	main()