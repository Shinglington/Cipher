import config
class Cipher():	
	def __init__(self, key):
		self.key = key
      
	def encrypt(self, text):
		return text
    	
	def decrypt(self, text):
		return text
		
	def prep_text(self, text, filter = ""):
		if not config.keep_spaces:
			filter += ' '
		if not config.keep_punct:
			filter += config.punctuation
		if not config.keep_num:
			filter += config.numbers
		if not config.keep_case:
			text = text.upper()
		output = ""
		for c in text:
			if c not in filter:
				output += c
		return output

class SubCipher(Cipher):
    def __init__(self, key):
        Cipher.__init__(self, key)

    def encrypt(self, text):
        return self.prep_text(text)
    
    def decrypt(self, text):
        return self.prep_text(text)
    
    def prep_text(self, text):
        return Cipher.prep_text(self, text, filter)

class TransCipher(Cipher):
    def __init__(self, key):
        Cipher.__init__(self, key)

    def encrypt(self, text):
        return self.prep_text(self, text)
    
    def decrypt(self, text):
        return self.prep_text(self, text)
    
    def prep_text(self, text):
        return Cipher.prep_text(self, text, filter)