def rle(input_string):
    new_string = ""
    i = 0
    while i < len(input_string):
        if input_string.count(input_string[i]) > 2:
            new_string = new_string + str(input_string.count(input_string[i])) + input_string[i]
            i = i + input_string.count(input_string[i])
        else:
            new_string = new_string + input_string[i]
            i = i + 1
    return new_string


def irle(coded_string):
    new_string = ""
    i = 0
    while i < len(coded_string):
        if coded_string[i].isdigit():
            new_string = new_string + coded_string[i + 1] * int(coded_string[i])
            i = i + 2
        else:
            new_string = new_string + coded_string[i]
            i = i + 1
    return new_string


print(irle(rle("aaabbbbccaaad")))