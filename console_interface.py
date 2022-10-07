import cipher_tool
import analysis
import myciphers.utility as util

def start():
	choices = {"Cipher Tool":cipher_tool.main
			  ,"Analysis Tool":analysis.main}
	util.display_menu("My Cipher Python", choices)
start()