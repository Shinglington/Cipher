import myciphers

while True:
    ciphertext = myciphers.utility.raw_input("Enter Cipher Text:")
    shift = int(input("Enter Shift: "))

    this_caesar = myciphers.Caesar(shift)
    plaintext = this_caesar.decrypt(ciphertext)
    print(plaintext)

    
