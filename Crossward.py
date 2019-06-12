def check_horizontal_start_of_word(size, row, column, is_white_block, used_in_word):
    is_horizontal_word = False
    i = column + 1
    while i < size:
        if is_white_block[row][i]:
            if used_in_word[row][i] == 0 or used_in_word[row][i] == 2:
                is_horizontal_word = True
                used_in_word[row][i] += 1
                i = i + 1
            else:
                return is_horizontal_word, used_in_word
        else:
            return is_horizontal_word, used_in_word
    if is_horizontal_word:
        used_in_word[row][column] += 1
    return is_horizontal_word, used_in_word


def check_vertical_start_of_word(size, row, column, is_white_block, used_in_word):
    is_vertical_word = False
    i = row + 1
    while i < size:
        if is_white_block[i][column]:
            if used_in_word[i][column] == 0 or used_in_word[i][column] == 1:
                is_vertical_word = True
                used_in_word[i][column] += 2
                i = i + 1
            else:
                return is_vertical_word, used_in_word
        else:
            return is_vertical_word, used_in_word
    if is_vertical_word:
        used_in_word[row][column] += 2
    return is_vertical_word, used_in_word


def number_crossward(size, is_white_block, used_in_word, numbered_crossward):
    number = 1
    for row in range(0, size):
        for column in range(0, size):
            if is_white_block[row][column]:
                is_horizontal_word, used_in_word = check_horizontal_start_of_word(size, row, column, is_white_block, used_in_word)
                is_vertical_word, used_in_word = check_vertical_start_of_word(size, row, column, is_white_block, used_in_word)
                if is_horizontal_word or is_vertical_word:
                    numbered_crossward[row][column] = number
                    number += 1
    return numbered_crossward


size = 7
file = open("Crossward.txt","r+")

input = []

for line in file:
    inp = line.rstrip('\n').split(' ')
    input.append(inp)
#print(input)
is_white_block = []

for line in input:
    line_white_block = []
    for j in line:
        if j == "W":
            line_white_block.append(True)
        else:
            line_white_block.append(False)
    is_white_block.append(line_white_block)

"""print(is_white_block)

used_in_word = [[0, 0, 0, 0, 0, 0, 0],\
               [0, 0, 0, 0, 0, 0, 0],\
               [0, 0, 0, 0, 0, 0, 0],\
               [0, 0, 0, 0, 0, 0, 0],\
               [0, 0, 0, 0, 0, 0, 0],\
               [0, 0, 0, 0, 0, 0, 0],\
               [0, 0, 0, 0, 0, 0, 0]]

numbered_crossward = [[0, 0, 0, 0, 0, 0, 0],\
                      [0, 0, 0, 0, 0, 0, 0],\
                      [0, 0, 0, 0, 0, 0, 0],\
                      [0, 0, 0, 0, 0, 0, 0],\
                      [0, 0, 0, 0, 0, 0, 0],\
                      [0, 0, 0, 0, 0, 0, 0],\
                      [0, 0, 0, 0, 0, 0, 0]]


is_white_block = [[False, True, False, True, True, True, True],\
                  [True, True, True, True, False, True, False],\
                  [False, True, False, True, False, True, False],\
                  [True, True, True, True, True, True, True],\
                  [False, True, False, True, False, True, False],\
                  [False, True, False, True, True, True, True],\
                  [True, True, True, True, False, True, False]]"""

used_in_word = [[0]*7]*7

numbered_crossward = [[0]*7]*7

print(number_crossward(size, is_white_block, used_in_word, numbered_crossward))