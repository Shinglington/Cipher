from myciphers.cipher import Cipher
import myciphers.config as config
import myciphers.utility as util

class FourSquare(Cipher):
	def __init__(self, alphabet1, alphabet2):
		Cipher.__init__(self, alphabet1, keep_case = False)
		self.grid1 = FourSquare.create_grid(alphabet1)
		self.grid2 = FourSquare.create_grid(alphabet2)

	def create_grid(alphabet):
		side_length = int(len(alphabet)**0.5)
		grid = []
		for i in range(side_length):
			row = ""
			for j in range(side_length):
				row += alphabet[i*side_length + j]
			grid.append(row)
		return grid

	def get_coords(letter, grid):
		xCoord = -1
		yCoord = -1
		for y in range(len(grid)):
			for x in range(len(grid)):
				if letter == grid[y][x]:
					xCoord = x
					yCoord = y
		return (xCoord, yCoord)

	
	def encrypt_pair(self, pair):
		coords1 = FourSquare.get_coords(pair[0], self.grid1)
		coords2 = FourSquare.get_coords(pair[1], self.grid2)
		
		

	def decrypt_pair(self pair):


	def encrypt(self, text):
		text = self.prep_text(text)
		ciphertext = ""
		for i in range(0, len(text), 2):
			pair = text[i]
			if i+1 >= len(text):
				pair += "X"
			else:
				pair += text[i+1]

			ciphertext += self.encrypt_pair(pair)

		return ciphertext
			
		

	def decrypt(self, text):
		text = self.prep_text(text)
		if len(text) % 2 != 0:
			print("Can't decrypt text which is odd length")
			return 
		plaintext = ""
		for i in range(0, len(text), 2):
			pair = text[i:i+2]
			plaintext += self.encrypt_pair(pair)
		return plaintext

		