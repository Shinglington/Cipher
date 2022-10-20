from myciphers.cipher import Cipher
import myciphers.config as config
import myciphers.utility as util

class ColTrans(Cipher):
	def __init__(self, key = "ABCDEF",
				 detailed = config.detailed):
		Cipher.__init__(self, detailed = detailed)
		self.key = key.upper()

	def get_order(self, keyword):
		## \/ DETAILED DISPLAY \/ ##
		if self.detailed:
			print("\n\n## FINDING ORDER OF COLUMNS ##")
			print("Keyword is {0} -> convert keyword to index numbers".format(self.key))
		## /\ DETAILED DISPLAY /\ ##
			
		unsorted_letters = [(keyword[i], i) for i in range(len(keyword))]
		sorted_letters = [(letter, index) for letter, index in sorted(unsorted_letters)]
		col_order = [pair[1] for pair in sorted_letters]
		
		## \/ DETAILED DISPLAY \/ ##
		if self.detailed:
			print("Found order to be " 
				  + "".join(str(x) for x in col_order))
		## /\ DETAILED DISPLAY /\ ##
		return col_order


	def display_cols(self, columns):
		for row in range(len(columns[0])):
			current_row = ""
			# loop through each column
			for col in range(len(columns)):
				if len(columns[col]) > row:
					current_row += columns[col][row]
			print(current_row)
        
	def cols_from_plaintext(self, text, pad_text = True):
		columns = []
		keylen = len(self.key)
		if pad_text:
			while len(text) % keylen != 0:
				text += config.padding
		for col_num in range(keylen):
			columns.append("")
		for i in range(len(text)):
			columns[i%keylen] = columns[i%keylen] + text[i]
			
        ## \/ DETAILED DISPLAY \/ ##
		if self.detailed:
			print("\n\n## COLUMNS FROM PLAINTEXT ##")
			self.display_cols(columns)
		## /\ DETAILED DISPLAY /\ ##
		return columns

	def cols_from_ciphertext(self, text):
		columns = []
		keylen = len(self.key)
		col_len = int(len(text) / keylen)
		for col_num in range(keylen):
		    col = ""
		    for i in range(col_len):
		    	col += text[col_num * col_len + i]
		    columns.append(col)
			
		## \/ DETAILED DISPLAY \/ ##
		if self.detailed:
			print("\n\n## COLUMNS FROM CIPHERTEXT ##")
			self.display_cols(columns)
		## /\ DETAILED DISPLAY /\ ##
		return columns

	def ciphertext_from_col(self, columns, order):
		string = ""
		for i in range(len(order)):
			string += columns[order[i]]
		return string

	def plaintext_from_col(self, columns, order):
		string = ""
		for i in range(len(columns[0])):
			for j in range(len(order)):
				if len(columns[order.index(j)]) > i:
					string += columns[order.index(j)][i]
		return string
          
            
	def encrypt(self, text, 
				keep_spaces = False, 
				keep_punct = False):
		# Remove spaces and extra punctuation
		text = self.prep_text(text, keep_spaces = keep_spaces, keep_punct = keep_punct)
		columns = self.cols_from_plaintext(text)
		col_order = self.get_order(self.key)
		return self.ciphertext_from_col(columns, col_order)


	def decrypt(self, text):
		## If ciphertext contains numbers and punctuation, likely need them to get columns correct
		text = self.prep_text(text, 
							  keep_num = True, 
							  keep_punct = True)
		columns = self.cols_from_ciphertext(text)
		col_order = self.get_order(self.key)
		return self.plaintext_from_col(columns, col_order)


	## BRUTEFORCE STUFF	
	def brute_force_length(text, key_length):
		key = config.alphabet_upper[0:key_length]
		key_permutations = util.permutations(key)
		decryptions = {}
		for k in key_permutations:
			str_k = "".join(k)
			decryptions.update({str_k:ColTrans(str_k, False).decrypt(text)})
		decryptions = util.order_by_likelihood(decryptions)
		return decryptions

	
	def guess_key(text, length = 0, maxlength = 9):
		most_likely_keys = []
		if length == 0:
			for i in range(2, maxlength+1):
				print("Checking key lengths of {0}".format(i))
				keys = ColTrans.guess_key(text, i)
				for k in keys:
					most_likely_keys.append(k)
		else:
			decryptions = ColTrans.brute_force_length(text, length)
			decrypt_keys = list(decryptions.keys())
			for i in range(min(10, len(decrypt_keys))):
				most_likely_keys.append(decrypt_keys[i])
		return most_likely_keys
		
		

	def brute_force(text, key_length = 0):
		## if known key length, use that, else generate array of factors to guess key length
		possible_keys = ColTrans.guess_key(text, key_length)
		if config.detailed:
			print("Possible keys:")
			print(possible_keys)
		decryptions = {}
		for k in possible_keys:
			decryptions.update({k:ColTrans(k, detailed = False).decrypt(text)})
		return decryptions
	
