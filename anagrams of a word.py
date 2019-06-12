import operator

def read_file():
    return open("words.txt").readlines()


def product_of_letters(word):
    letter_dictionary = {'e' : 2, 't': 3, 'a' : 5, 'o' : 7, 'i' : 11, 'n': 13, 's':17, 'h' : 19, 'r' : 23, 'd' : 29, 'l' : 31, 'c' : 37, 'u' : 41, 'm' : 43, 'w' : 47, 'f': 53, 'g' : 59,'y' : 61, 'p' : 67, 'b' : 71, 'v' : 73,'k' : 79,'j' : 83,'x' : 89,'q' : 97,'z': 101}
    prod = 1
    for letter in word.strip():
        prod = prod * letter_dictionary[letter]
    return prod


def compute_anagrams():
    words = read_file()
    dict_of_words = {}
    for word in words:
        dict_of_words[word.lower().strip()] = product_of_letters(word.lower().strip())
    sorted_dict = sorted(dict_of_words.items(), key=operator.itemgetter(1))
    print(sorted_dict)
    i = 1
    anagrams = []
    while i < len(sorted_dict)-1:
        anagrams_of_the_word = []
        anagrams_of_the_word.append(sorted_dict[i][0])
        print(anagrams_of_the_word)
        has_anagrams = False
        while sorted_dict[i][1] == sorted_dict[i+1][1]:
            has_anagrams = True
            anagrams_of_the_word.append(sorted_dict[i + 1][0])
            i += 1
        if has_anagrams:
            anagrams.append(anagrams_of_the_word)
        i += 1
        return anagrams


print(compute_anagrams())




