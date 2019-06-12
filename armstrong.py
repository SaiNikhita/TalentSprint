def power(num, pow):
    return num ** pow


def order(num):
    return len(str(num))


def is_armstrong(num):
    n = order(num)
    temp = num
    sum = 0
    while temp != 0:
        rem = temp % 10
        sum = sum + power(rem, n)
        temp = temp // 10
    return sum == num


def generate_armstrong_number(min_number, max_number):
    for i in range(min_number, max_number):
        if is_armstrong(i):
            print(i)


generate_armstrong_number(1000, 100000)