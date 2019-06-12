"""def str_to_letters(string):
    return [alphabet for alphabet in string]

def higher(a_letters, b_letters, max):
    return a_letters if len(a_letters) == max else b_letters

def interleave_upto_smaller_string(a_letters, b_letters, min):
    new_str = ""
    for i in range(0, min):
        new_str = new_str + a_letters[i]
        new_str = new_str + b_letters[i]
    return new_str

def interleave_beyond_smaller_string(higherword, min, max):
    new_str = ""
    for j in range(min, max):
        new_str = new_str + higherword[j]
    return new_str

def interleave(a_letters, b_letters, max, min):
    string1 = interleave_upto_smaller_string(a_letters, b_letters, min)
    higherword = higher(a_letters, b_letters, max)
    string2 = interleave_beyond_smaller_string(higherword, min, max)
    return string1 + string2


a = "abcde"
b = "pqrstuv"
a_letters = str_to_letters(a)
b_letters = str_to_letters(b)
max_len = max(len(a_letters), len(b_letters))
min_len = min(len(a_letters), len(b_letters))
print(interleave(a_letters, b_letters, max_len, min_len))"""


def larger(a, b):
    return a if len(a) > len(b) else b


def my_zip(a, b):
    string = ""
    for i in list(zip(a, b)):
        for j in i:
            string = string + j
    min_size = min(len(a), len(b))
    larger_word = larger(a, b)
    string = string + larger_word[min_size :]
    return string

a = "abcde"
b = "pqrstuv"
string = my_zip(a, b)
print(string)

