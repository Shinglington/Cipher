from myciphers.cipher import Cipher
import myciphers.config as config

class Playfair(Cipher):
	def __init__(self, alphabet):
		Cipher.__init__(self, alphabet, keep_case = False)
		self.rows = 5
		self.cols = 5
		self.grid = self.get_grid()
		assert len(self.alphabet) == self.rows * self.cols

	def generate_grid_alphabet(keyword, alphabet = config.alphabet_upper.replace("J","")):
		## STATIC METHOD TO GET ALPHABET FROM KEYWORD
		## alphabet uses 25 letters, so replace J
		grid_alphabet = ""
		## Add keyword letters first
		for letter in keyword.upper().replace("J","I"):
			if letter not in grid_alphabet:
				grid_alphabet += letter
		## Add remaining alphabet letters
		for letter in alphabet:
			if letter not in grid_alphabet:
				grid_alphabet += letter
		return grid_alphabet

	def get_grid(self):
		if config.detailed:
			print("\n\n### PLAYFAIR GRID ###")
		grid = []
		## for each row
		for i in range(0, self.rows):
			grid.append(self.alphabet[i*self.rows:self.cols*(i+1)])
			if config.detailed:
				print(grid[i])
		return grid

	def get_coordinates(self, letter):
		## coordinates in row num, col num
		row = -1
		for i in range(len(self.grid)):
			if letter in self.grid[i]:
				row = i
				break
		col = -1
		for i in range(len(self.grid[row])):
			if letter == self.grid[row][i]:
				col = i
				break

		return (row, col)
		
	
	def encrypt_pair(self, pair):
		a = pair[0]
		b = pair[1]
		## coordinates in form row, column
		coord_a = self.get_coordinates(a)
		coord_b = self.get_coordinates(b)
		
		new_a = ""
		new_b = ""
		## if row same
		if coord_a[0] == coord_b[0]:
			new_a = self.grid[coord_a[0]][(coord_a[1] + 1)%self.cols]
			new_b = self.grid[coord_b[0]][(coord_b[1] + 1)%self.cols]

		## if column same
		elif coord_a[1] == coord_b[1]:
			new_a = self.grid[(coord_a[0] + 1)%self.rows][coord_b[1]]
			new_b = self.grid[(coord_b[0] + 1)%self.rows][coord_b[1]]
		## otherwise different row and different column
		else:
			## swap column numbers
			new_a = self.grid[coord_a[0]][coord_b[1]]
			new_b = self.grid[coord_b[0]][coord_a[1]]

		return new_a + new_b
			
			
	def decrypt_pair(self, pair):
		a = pair[0]
		b = pair[1]
		## coordinates in form row, column
		coord_a = self.get_coordinates(a)
		coord_b = self.get_coordinates(b)
		
		new_a = ""
		new_b = ""
		## if row same
		if coord_a[0] == coord_b[0]:
			new_a = self.grid[coord_a[0]][(coord_a[1] - 1)%5]
			new_b = self.grid[coord_b[0]][(coord_b[1] - 1)%5]

		## if column same
		elif coord_a[1] == coord_b[1]:
			new_a = self.grid[(coord_a[0] - 1)%5][coord_a[1]]
			new_b = self.grid[(coord_b[0] - 1)%5][coord_b[1]]
		## otherwise different row and different column
		else:
			new_a = self.grid[coord_a[0]][coord_b[1]]
			new_b = self.grid[coord_b[0]][coord_a[1]]
		return new_a + new_b
	
	def encrypt(self, text):
		text = self.prep_text(text, 
							  keep_spaces = False, 
							  keep_punct = False, 
							  keep_num = False)
		text = text.replace("J", "I") ## replace j with i
		## check for double letters
		for i in range(0, len(text), 2):
			if text[i] == text[i+1]:
				text[i+1] = "X"
		## if odd, add x
		if len(text) % 2 != 0:
			text += "X"

		## ENCRYPT ##
		ciphertext = ""
		## loop pairs
		for i in range(0, len(text), 2):
			ciphertext += self.encrypt_pair(text[i:i+2])

		return ciphertext


	def decrypt(self, text):
		text = self.prep_text(text, keep_spaces = False)
		## if odd, add x
		if len(text) % 2 != 0:
			text += "X"
		## Decrypt ##
		plaintext = ""
		## loop pairs
		for i in range(0, len(text), 2):
			if text[i] == text[i+1]:
				assert "Can't decrypt double letters"
			plaintext += self.decrypt_pair(text[i:i+2])
		return plaintext
		

	

	
		
	
	