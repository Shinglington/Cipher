import myciphers


def main():
    text = myciphers.utility.raw_input("Enter cipher text:")
    print(myciphers.ColTrans("GERMAN").decrypt(text))
    
 
main()