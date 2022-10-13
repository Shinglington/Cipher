import myciphers.config as config
import myciphers.utility as util
class Cipher():	
	def __init__(self, 
				 alphabet = config.alphabet_upper, 
				 keep_case = config.keep_case):
		self.alphabet = alphabet
		self.keep_case = keep_case
					 
	def encrypt(self, text):
		return text
    	
	def decrypt(self, text):
		return text
		
	def prep_text(self, text, 				
				  keep_spaces = config.keep_spaces,
				  keep_punct = config.keep_punct,
				  keep_num = config.keep_num):
		filter = ""
		filtered_text = ""
		if not self.keep_case:
			text = text.upper()
		if not keep_spaces:
			filter += ' '
		if not keep_punct:
			filter += config.punctuation
		if not keep_num:
			filter += config.numbers
		# keep characters in alphabet
		for c in self.alphabet:
			filter.replace(c,"")
		# filter text
		removed_characters = {}
		for c in text:
			if c not in filter:
				filtered_text += c
			else:
				if c in removed_characters:
					removed_characters.update({c:removed_characters[c]+1})
				else:
					removed_characters.update({c:1})
		## \/ DETAILED REPORT \/ ##
		if config.detailed and len(removed_characters) > 0:
			print("REMOVED CHARACTERS:")
			for k in util.sort_dict(removed_characters):
				print("{0} : {1}".format(k, removed_characters[k]))
		## /\ DETAILED REPORT /\ ##
		return filtered_text
