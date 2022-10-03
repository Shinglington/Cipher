import myciphers

def raw_input(prompt):
    lines = []
    print(prompt)
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return ' '.join(lines)


def main():
    text = raw_input("Enter cipher text:")
 
main()