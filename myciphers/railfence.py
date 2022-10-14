from myciphers.cipher import Cipher
import myciphers.config as config

class RailFence(Cipher):
	def __init__(self, key):
		Cipher.__init__(self)
		self.key = key

	
	def make_fence(self, text):
		fence =[[""] * len(text) for row in range(self.key)]
		rail = 0
		descending = True
		for i in range(len(text)):
			fence[rail][i] = text[i]
			## check if descending state needs changing
			if rail + 1 >= self.key and descending:
				descending = False
			elif rail - 1 < 0 and not descending:
				descending = True
			## increment or decrement rail
			if descending:
				rail += 1	
			else:
				rail -= 1
				
		return fence

	def display_fence(self, fence):
		for row in fence:
			line = ""
			for char in row:
				if char == "":
					line += " "
				else:
					line += str(char)
			print(line)
		

	def encrypt(self, text):
		text = self.prep_text(text,
							  keep_spaces = False,
							  keep_num = True,
							  keep_punct = False)
		fence = self.make_fence(text)
		## reading fence
		if config.detailed:
			print("\nRAILFENCE")
			self.display_fence(fence)
			print()
		return "".join("".join(row) for row in fence)

	def decrypt(self, text):
		text = self.prep_text(text,
							  keep_spaces = False,
							  keep_num = True)
		indices = self.make_fence(range(len(text)))
		ciphertext = [""] * len(text)
		text_pos = 0
		for row in indices:
			for i in row:
				if i != "":
					if text_pos < len(text):
						ciphertext[i] = text[text_pos]
						text_pos += 1

		return "".join(ciphertext)


	def brute_force_decrypt(text, max_rails = 10):
		decryptions = {}
		for rail_count in range(2, max_rails):
			decryptions.update({rail_count:RailFence(rail_count).decrypt(text)})
		return decryptions