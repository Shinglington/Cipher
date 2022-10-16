from myciphers.cipher import Cipher
import myciphers.config as config
import myciphers.utility as util

class Hill(Cipher):
	def __init__(self, matrix_string = "ABCD", alphabet = config.alphabet_upper):
		Cipher.__init__(self, alphabet)
		self.size = int(len(matrix_string) ** 0.5)
		assert len(matrix_string) == self.size ** 2
		self.matrix = Hill.make_matrix(matrix_string.upper(), self.alphabet)
		if self.detailed:
			print("\nENCRYPTION MATRIX")
			self.show_matrix(self.matrix)
		self.inverse = Hill.get_inverse(self.matrix)
		assert self.inverse != None
		if self.detailed:
			print("\nDECRYPTION MATRIX")
			self.show_matrix(self.inverse)


	

	def make_matrix(matrix_string, alphabet = config.alphabet_upper):
		matrix = []
		size = int(len(matrix_string) ** 0.5)
		for i in range(size):
			row = []
			for j in range(size):
				index = alphabet.index(matrix_string[i*size+j])
				row.append(index)
			matrix.append(row)
		return matrix
		
	def show_matrix(self, matrix):
		for row in matrix:
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
		for i in range(0, len(text), self.size):
			old_indices = []
			for j in range(self.size):
				index = self.alphabet.index(text[i+j])
				old_indices.append([index])
			new_indices = util.matrix_multiply(self.matrix, old_indices)
			for x in new_indices:
				ciphertext += self.alphabet[x[0] % len(self.alphabet)]
		return ciphertext
		
	def decrypt(self, text):
		text = self.prep_text(text, 
							  keep_spaces = False)
		assert len(text) % self.size == 0
		plaintext = ""
		for i in range(0, len(text), self.size):
			old_indices = []
			for j in range(self.size):
				index = self.alphabet.index(text[i+j])
				old_indices.append([index])
			new_indices = util.matrix_multiply(self.inverse, old_indices)
			for x in new_indices:
				plaintext += self.alphabet[x[0] % len(self.alphabet)]
		return plaintext

	def get_inverse(matrix, modulo = 26):
		adj_matrix = []
		inv_det = util.modular_inverse(util.matrix_determinant(matrix), modulo)
		if inv_det == 0:
			return None
		if len(matrix) == 2:
			## matrix in form [[a, b], [c, d]]
			a = matrix[0][0]
			b = matrix[0][1]
			c = matrix[1][0]
			d = matrix[1][1]
			adj_matrix = [[d, -b]
					    ,[-c, a]]
		else:
			adj_matrix = util.transpose_matrix(util.matrix_cofactors(matrix))

		inv_matrix = []
		for row in range(len(matrix)):
			inv_row = []
			for col in range(len(matrix)):
				inv_row.append((inv_det * adj_matrix[row][col]) % modulo)
			inv_matrix.append(inv_row)

		return inv_matrix
			
		