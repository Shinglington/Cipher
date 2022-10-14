import cipher_ui
from console_io import display_menu
import analysis_ui
import myciphers

def start():
	print("AFTER ENTERING PLAIN / CIPHERTEXT, USE CTRL + D TO CONTINUE")
	choices = {"Cipher Tool":cipher_ui.main
			  ,"Analysis Tool":analysis_ui.main}
	display_menu("My Cipher Python", choices)
start()