import myciphers
from myciphers.caesar import Caesar
from myciphers.utility import raw_input

while True:
    ciphertext = raw_input("Enter Cipher Text:")
    shift = int(input("Enter Shift: "))

    this_caesar = Caesar(shift)
    plaintext = this_caesar.decrypt(ciphertext)
    print(plaintext)

    
