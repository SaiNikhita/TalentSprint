def is_panagram(letters_frequency):
    return len(letters_frequency.keys()) == 26


def count_letter_frequency(input):
    letters_frequency = {}
    for i in input:
        if i.isalpha() and i not in letters_frequency:
            letters_frequency[i.lower()] = 1
        elif i.isalpha() and i in letters_frequency:
            letters_frequency[i.lower()] += 1
    return letters_frequency


def check_panagram(input):
    letters_frequency = count_letter_frequency(input)
    return is_panagram(letters_frequency)


input_string = "Pack my box with five dozen liquor jugs"
print(check_panagram(input_string))