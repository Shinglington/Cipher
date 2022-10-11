from myciphers.cipher import SubCipher
import myciphers.utility as util
class Vigenere(SubCipher):
	def __init__(self, key = "ABCDEF", alphabet = SubCipher.uppercase, keep_case = False):
		SubCipher.__init__(self, key.upper(), alphabet, keep_case)
		self.grid = self.tabula_recta()

	def tabula_recta(self):
		grid = []
		for i in range(len(self.alphabet)):
			grid.append(self.alphabet[i: len(self.alphabet)] + self.alphabet[0:i])
		return grid
	
	def get_cipherchar(self, plainchar, keychar):
        # Go to row corresponding to plainchar
        # Go to column corresponding to keychar
        # Return cipherchar
		return self.grid[self.alphabet.index(plainchar)][self.alphabet.index(keychar)]

	def get_plainchar(self, cipherchar, keychar):
        # Go to row corresponding to keychar
        # Find position of cipherchar in row
        # Use position to get corresponding plainchar
		return 		self.alphabet[self.grid[self.alphabet.index(keychar)].index(cipherchar)]

	def get_keychar(self, plainchar, cipherchar):
		# go to row corresponding to plainchar
		# find position of cipherchar 
		# return corresponding alphabet letter in position
		return self.alphabet[self.grid[self.alphabet.index(plainchar)].index(cipherchar)]
		

		
	def encrypt(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
		text = self.prep_text(text, keep_spaces, keep_punct, keep_num)
		ciphertext = ""
		keyindex = 0
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				print(new_char)
				new_char = self.get_cipherchar(new_char, self.key[keyindex])
				keyindex = (keyindex + 1) % len(self.key)
			if self.keep_case and c.islower:
				new_char = new_char.lower()
			ciphertext += new_char
		return ciphertext
                

	def decrypt(self, text, keep_spaces = False, keep_punct = False, keep_num = False):
		text = self.prep_text(text, keep_spaces, keep_punct, keep_num)
		plaintext = ""
		keyindex = 0
		for c in text:
			new_char = c.upper()
			if new_char in self.alphabet:
				new_char = self.get_plainchar(new_char, self.key[keyindex])
				keyindex = (keyindex + 1) % len(self.key)
			if self.keep_case and c.islower:
				new_char = new_char.lower()
			plaintext += new_char
		return plaintext

def guess_key_length(text, max_length = 20):
	text = text.replace(" ","").upper().replace(SubCipher.punctuation,"")
	ioc_list = []
	for col_len in range(1, max_length):
		columns = []
		for col_num in range(col_len):
			this_column = ""
			for j in range(col_num, len(text), col_len):
				this_column += text[j]
			columns.append(this_column)

		column_iocs = []
		for c in columns:
			ioc = 0
			if len(c) > 1:
				ioc = util.calc_ioc(c)
			column_iocs.append(ioc)
		average_ioc = sum(column_iocs) / len(column_iocs)
		ioc_list.append(average_ioc)

		## print iocs
		print("Length {0}, IOC {1}".format(col_len, average_ioc))

	key_length = 0
	for i in range(len(ioc_list)):
		if key_length == 0:
			key_length = i+1
		elif ioc_list[i] > ioc_list[key_length - 1]:
			key_length = i+1
	
	return key_length


def guess_column_key(column):
	from myciphers.caesar import Caesar
	possible_letters = []
	# First, get letter frequencies in column
	col_freq = list(util.ngram(column, 1).keys())
	# Add missing letters to frequency list
	for letter in SubCipher.uppercase:
		if letter not in col_freq:
			col_freq.append(letter)

	possible_shifts = {}
	# check each caesar shift
	# perform chi squared test on each shift
	for shift in range(26):
		decryption = Caesar(shift).decrypt(column)
		chi_score = util.calc_chi_squared(decryption)
		possible_shifts.update({shift:chi_score})

	possible_decryptions = dict(sorted(possible_shifts.items(), key = lambda item : item[1]))
	lowest_chi = list(possible_decryptions.values())[0]
	for i in range(len(possible_decryptions)):
		shift = list(possible_decryptions.keys())[i]
		if possible_decryptions[shift] < (2 * lowest_chi):
			possible_letters.append(SubCipher.uppercase[shift])
		else:
			break
	"""
	# Map most frequent letters in column to most frequent letters in english
	E_keys = []
	for i in range(6):
		col_letter = col_freq[i]
		key_letter = Vigenere().get_keychar("E", col_letter)
		E_keys.append(key_letter)

	# Map least frequent letters letters in column to least frequent letters in english
	Z_keys  = []
	for i in range(1, 7):
		col_letter = col_freq[-i]
		key_letter = Vigenere().get_keychar("Z", col_letter)
		Z_keys.append(key_letter)

	# Check for common letters in z and e keys
	for key in E_keys:
		if key in Z_keys:
			possible_letters.append(key)
	"""
	return possible_letters
	

def guess_key(text, length = 0):
	if length == 0:
		length = guess_key_length(text)
	print(length)
	text = text.replace(" ","").upper().replace(SubCipher.punctuation,"")
	possible_keyword = []
	# guess key of each "column"
	for col_num in range(length):
		this_column = ""
		for j in range(col_num, len(text), length):
			this_column += text[j]
		# add guessed key to possible keyword
		possible_keyword.append(guess_column_key(this_column))

	keywords = [""]
	# loop through each "column" possible key
	for i in range(length):
		key_letters = possible_keyword[i]
		# If no possible letter, add a "?"
		if len(key_letters) == 0:
			key_letters = ["?"]
		# for existing partial keywords, add new possibilities
		new_keywords = []
		for j in range(len(keywords)):
			for k in key_letters:
				new_keywords.append(keywords[j] + k)
		keywords = new_keywords
	return keywords


	