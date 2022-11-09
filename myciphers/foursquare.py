from myciphers.cipher import Cipher
import myciphers.config as config
import myciphers.utility as util

class FourSquare(Cipher):
	def __init__(self, alphabet):
		Cipher.__init__(self, alphabet, keep_case = False)
		