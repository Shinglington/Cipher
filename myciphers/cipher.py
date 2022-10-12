import myciphers.config as config
class Cipher():	
	def __init__(self, key):
		self.key = key
      
	def encrypt(self, text):
		return text
    	
	def decrypt(self, text):
		return text
		
	def prep_text(self, text, filter = "", keep_spaces = config.keep_spaces, keep_punct = config.keep_punct, keep_num = config.numbers, keep_case = config.keep_case):
		if not keep_spaces:
			filter += ' '
		if not keep_punct:
			filter += config.punctuation
		if not keep_num:
			filter += config.numbers
		if not keep_case:
			text = text.upper()
		output = ""
		for c in text:
			if c not in filter:
				output += c
		return output
