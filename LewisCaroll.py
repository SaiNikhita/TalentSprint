def read_words():
    words = open("sowpods1.txt").readlines()
    return [word.rstrip() for word in words]


def check_valid_word(word):
    words = read_words()
    return word in words


def count_number_of_letters(initial_word, final_word, count):
    unchanged = True
    word = initial_word
    for i in range(len(initial_word)):
        if initial_word[i] != final_word[i]:
            if check_valid_word(word[:i] + final_word[i] + word[i+1:]):
                word = word[:i] + final_word[i] + word[i+1:]
                count += 1
                unchanged = False
    if unchanged:
            return -1
    if i == len(initial_word) - 1 and word != final_word:
            count = count_number_of_letters(word, final_word, count)
    return count


print(count_number_of_letters('salt', 'gold', 0))