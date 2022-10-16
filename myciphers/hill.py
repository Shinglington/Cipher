from myciphers.cipher import Cipher
import myciphers.config as config

class Hill(Cipher):
	def __init__(self, matrix_string = "ABCD", size = 2, alphabet = config.alphabet_upper):
		Cipher.__init__(self, alphabet)
		assert len(matrix_string) == size ** 2
		self.size = size
		self.matrix = self.make_matrix(matrix_string.upper())
		if self.detailed:
			print("\nENCRYPTION MATRIX")
			self.show_matrix()
		self.inverse = Hill.get_inverse(self.matrix)
		assert self.inverse != None
		
	def make_matrix(self, matrix_string):
		print(self.size)
		matrix = []
		print(matrix)
		for i in range(self.size):
			row = []
			for j in range(self.size):
				index = self.alphabet.index(matrix_string[i*self.size+j])
				row.append(index)
			matrix.append(row)
		return matrix
		
	def show_matrix(self):
		print(self.matrix)
		for row in self.matrix:
			print(" ".join("{0:2}".format(str(x)) for x in row))


	def encrypt(self, text):
		text = self.prep_text(text, 
							  keep_spaces = False, 
							  keep_punct = False, 
							  keep_num = False)
		## Make sure text is multiple of size
		while len(text) % self.size != 0:
			text += "X"
		
		ciphertext = ""
		return ciphertext
		
	def decrypt(self, text):
		text = self.prep_text(text, 
							  keep_spaces = False)
		assert len(text) % self.size == 0
		plaintext = ""
		return plaintext

	def get_inverse(matrix):
		if len(matrix) == 2:
			## matrix in form [[a, b], [c, d]]
			a = matrix[0][0]
			b = matrix[0][1]
			c = matrix[1][0]
			d = matrix[1][1]

	def get_determinant(matrix):
		if len(matrix) == 2:
			## matrix in form [[a, b], [c, d]]
			a = matrix[0][0]
			b = matrix[0][1]
			c = matrix[1][0]
			d = matrix[1][1]
			return (a*d) - (b*c)
		else:
			determinant = 0
			for i in range(len(matrix)):
				minor = []
				for row in range(1, len(matrix) + 1):
					minor_row = []
					for col in range(len(matrix)):
						if col != i:
							minor_row.append(matrix[row][col])
					minor.append(minor_row)
				determinant += ((-1)**i) * Hill.get_determinant(minor)
			return determinant
			
			
		
		