import myciphers
from myciphers.columntransposition import ColTransposition



def main():
    text = myciphers.utility.raw_input("Enter cipher text:")
    print(ColTransposition("GERMAN").calc_indices())
 
main()