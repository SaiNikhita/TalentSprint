def list_of_numbers(n):
    return [i for i in range(1, n+1)]


def is_end_of_line(num):
    temp = 1
    while temp <= num:
        if temp*(temp + 1)/2 == num:
            return True
        temp = temp + 1
    return False

def print_pattern(num):
    list_of_nums =  list_of_numbers(num)
    pattern = ""
    for i in list_of_nums:
        if is_end_of_line(i):
            pattern = pattern + str(i) + "\n"
        else:
            pattern = pattern + str(i) + "\t"
    return pattern

n = 13
print(print_pattern(n))