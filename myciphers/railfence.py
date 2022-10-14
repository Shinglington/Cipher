from myciphers.cipher import Cipher
import myciphers.config as config

class RailFence(Cipher):
	def __init__(self, key):
		Cipher.__init__(self)
		self.key = key

	
	def make_fence(self, text):
		fence =[[None] * len(text) for row in range(self.key)]

		rail = 0
		for i in range(len(text)):
			fence[rail][i]
		



		if config.detailed:
			self.display_fence(fence)
		return fence

	def display_fence(self, fence):
		for row in fence:
			row = ""
			for char in row:
				if char == None:
					row += " "
				else:
					row += char
			print(row)
		

	def encrypt(self, text):
		text = self.prep_text(text,
							  keep_spaces = False,
							  keep_num = True,
							  keep_punct = False)
		fence = self.make_fence(text)
		return text

	def decrypt(self, text):
		text = self.prep_text(text,
							  keep_spaces = False,
							  keep_num = True)
		fence = self.make_fence(text)
		return text