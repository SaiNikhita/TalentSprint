def split_number(num, split):
    return num[:split], num[split:]


def is_kaprekar_number(num):
    square = num * num
    number = str(square)
    size = len(number)
    for split_point in range(1, size):
        left, right = split_number(number, split_point)
        if int(left) != 0 and int(right) != 0 and num == int(left) + int(right):
            return True


def generate_kaprekar_number(min_number, max_number):
    for i in range(min_number, max_number):
        if is_kaprekar_number(i):
            print(i)


generate_kaprekar_number(1000, 10000)