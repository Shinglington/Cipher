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

def ngram(text, n=1, continuous = True, display = False, ignore_case = True, ignore_spaces = True):
    frequencies = {}
    increment = 1
    if not continuous:
        increment = n
    if ignore_case:
    	text = text.upper()
    if ignore_spaces:
        text = text.replace(" ","")

		
    for i in range(0, len(text), increment):
        substring = text[i:i+n]
        if substring in frequencies:
            frequencies.update({substring:frequencies[substring]+1})
        else:
            frequencies.update({substring:1})

    return sort_result(frequencies, display)


def sort_result(freq_dict, display=False):
    sorted_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1]))
    if display:
        for k,v in sorted_dict:
            print(k + " : " + v)
    return sorted_dict
