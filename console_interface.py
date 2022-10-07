import cipher_tool
import analysis
import myciphers.utility as util

def start():
	print("AFTER ENTERING PLAIN / CIPHERTEXT, USE CTRL + D TO CONTINUE")
	choices = {"Cipher Tool":cipher_tool.main
			  ,"Analysis Tool":analysis.main}
	util.display_menu("My Cipher Python", choices)
start()