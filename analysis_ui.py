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
		# Display results
		print("LETTER\tFREQUENCY")
		for k in frequencies:
			print(str(k) + "     \t" + str(frequencies[k]))
				
	def n_gram_analysis():
		text = util.raw_input("Enter Text To Analyse:")
		n = util.get_int_choice("Enter length of strings to find frequencies for: ")
		continuous = util.get_bool_choice("Continuous analysis?\n(i.e. for n = 2 'abcd' returns 'ab','bc','cd' instead of 'ab', 'cd')\n")
		frequencies = util.ngram(text, n, continuous) 
		# Display results
		print("STRING\tFREQUENCY")
		for k in frequencies:
			print(str(k) + (5-n)*" " + "\t" + str(frequencies[k]))

	## UI ##
	choices = {"Single Letter Analysis":single_letter_analysis
			  ,"N-Gram Analysis":n_gram_analysis}
	util.display_menu("Frequency Analysis", choices)


def GENERAL():
	choices = {"Factor Analysis":factor_analysis}
	util.display_menu("Other Tools", choices)

def factor_analysis():
	text = util.raw_input("Enter text to analyse:")
	ignore_spaces = util.get_bool_choice("Ignore spaces?")
	ignore_punct = util.get_bool_choice("Ignore punctuation?")
	length = util.get_length(text, ignore_spaces, ignore_punct)
	print("Text Length: " + str(length))
	print(print("Factors: " + str(util.get_factors(length))))
	
### MENU ###
def main():
	choices = {"Frequency Analysis":FREQ_ANALYSIS
			  ,"Other Tools":GENERAL}
	util.display_menu("Menu", choices)

if __name__ == "__main__":
	main()