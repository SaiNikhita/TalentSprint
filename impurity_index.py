def count_letter_frequency(input):
    letters_frequency = {}
    for i in input:
        if i.isalpha() and i not in letters_frequency:
            letters_frequency[i.lower()] = 1
        elif i.isalpha() and i in letters_frequency:
            letters_frequency[i.lower()] += 1
    return letters_frequency


def calculate_impurity_index(input):
    letters_frequency = count_letter_frequency(input)
    impurity_index = 0
    for letter, freq in letters_frequency.items():
        if freq > 1:
            if letter in ['a', 'e', 'i', 'o', 'u']:
                impurity_index += 0.5 * (freq - 1)
            else:
                impurity_index += 0.7 * (freq - 1)
        if freq % 3 == 0:
            impurity_index += 3 * freq // 3
        elif freq % 2 == 0:
            impurity_index += freq // 2
    return impurity_index


input_string = "Pack my box with five dozen liquor jugs"
print(calculate_impurity_index(input_string))