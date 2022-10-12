import myciphers.config as config
import myciphers.utility as util
class Cipher():	
	def __init__(self, key, 
				 detailed = config.detailed, 
				 teaching = config.teaching,
				 keep_spaces = config.keep_spaces, 
				 keep_punct = config.keep_punct, 
				 keep_num = config.numbers, 
				 keep_case = config.keep_case):
		self.key = key
		self.detailed = detailed
		self.teaching = teaching
		self.keep_spaces = keep_spaces
		self.keep_punct = keep_punct
		self.keep_num = keep_num
		self.keep_case = keep_case
					 
	def encrypt(self, text):
		return text
    	
	def decrypt(self, text):
		return text
		
	def prep_text(self, text, filter = ""):
		## \/ DETAILED REPORT \/ ##
		if self.detailed:
			print("\n\n### PREP TEXT FUNCTION ###")
		## /\ DETAILED REPORT /\ ##
		if not self.keep_spaces:
			filter += ' '
		if not self.keep_punct:
			filter += config.punctuation
		if not self.keep_num:
			filter += config.numbers
		if not self.keep_case:
			## \/ DETAILED REPORT \/ ##
			if self.detailed:
				print("Converted text to uppercase")
			## /\ DETAILED REPORT /\ ##
			text = text.upper()
		output = ""
		
		removed_characters = {}
		for c in text:
			if c not in filter:
				output += c
			else:
				if c in removed_characters:
					removed_characters.update({c:removed_characters[c]+1})
				else:
					removed_characters.update({c:1})
		## \/ DETAILED REPORT \/ ##
		if self.detailed and len(removed_characters) > 0:
			print("REMOVED CHARACTERS:")
			for k in util.sort_dict(removed_characters):
				print("{0} : {1}".format(k, removed_characters[k]))
		## /\ DETAILED REPORT /\ ##
		return output
