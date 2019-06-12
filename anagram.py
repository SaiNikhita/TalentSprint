"""def word_to_letters(word):
    return [letter for letter in word]


def are_anagrams(a, b):
    a_letters = word_to_letters(a)
    b_letters = word_to_letters(b)
    if len(a_letters) != len(b_letters):
        return False
    for i in a_letters:
        if i in b_letters:
            a_letters[a_letters.index(i)] = ""
            b_letters[b_letters.index(i)] = ""
        else:
            return False
    return True


a = "spaa"
b = "rasp"
print(are_anagrams(a, b))"""


def word_to_dict(word):
    letter_dict = {}
    for letter in word:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict


def are_anagrams(a, b):
    a_letter_dict = word_to_dict(a)
    b_letter_dict = word_to_dict(b)
    return a_letter_dict == b_letter_dict

print(are_anagrams("spar", "rpas"))



