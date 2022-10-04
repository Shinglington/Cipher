from faulthandler import cancel_dump_traceback_later
from myciphers.cipher import Cipher

class ColTransposition(Cipher):
    def __init__(self, key = "ABCDEF"):
        Cipher.__init__(self, key.lower(), "abcdefghijklmnopqrstuvwxyz", True)
        self.order = self.calc_indices()

    def calc_indices(self):
        indices = []
        unsorted_letters = [(self.key[i], i) for i in range(len(self.key))]
        sorted_letters = [(letter, index) for letter, index in sorted(unsorted_letters)]
        return [pair[1] for pair in sorted_letters]


    