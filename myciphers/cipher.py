import myciphers.config as config

class Cipher():	
	def __init__(self, key, detailed = config.detailed, teaching = config.teaching):
		self.key = key
		self.detailed = config.detailed
		self.teaching = config.teaching
      
	def encrypt(self, text):
		return text
    	
	def decrypt(self, text):
		return text
		
	def prep_text(self, text, filter = "", keep_spaces = config.keep_spaces, keep_punct = config.keep_punct, keep_num = config.numbers, keep_case = config.keep_case):
		## \/ DETAILED REPORT \/ ##
		if self.detailed:
			print("\n\n### PREP TEXT FUNCTION ###")
		## /\ DETAILED REPORT /\ ##
		if not keep_spaces:
			filter += ' '
		if not keep_punct:
			filter += config.punctuation
		if not keep_num:
			filter += config.numbers
		if not keep_case:
			## \/ DETAILED REPORT \/ ##
			if self.detailed:
				print("\nConverted text to uppercase")
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
			print("\nREMOVED CHARACTERS:")
			for k, v in sorted(removed_characters, key = lambda item : item[1], reverse = True):
				print("{0} : {1}".format(k, v))
		## /\ DETAILED REPORT /\ ##
		return output
