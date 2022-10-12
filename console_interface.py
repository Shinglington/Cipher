import cipher_ui
import analysis_ui
import myciphers.utility as util
import myciphers.config


def start():
	print("AFTER ENTERING PLAIN / CIPHERTEXT, USE CTRL + D TO CONTINUE")
	choices = {"Cipher Tool":cipher_ui.main
			  ,"Analysis Tool":analysis_ui.main}
	util.display_menu("My Cipher Python", choices)
start()