def aliquot(num):
    aliq = 1
    i = 2
    while i * i < num:
        if num % i == 0:
            aliq = aliq + i + num/i
        i += 1
    if i*i == num:
        aliq += i
    return aliq

def is_amicable_pair(first, second):
    return aliquot(first) == second and aliquot(second) == first


def generate_amicable_pairs(min_number, max_number):
    for i in range(min_number, max_number):
        aliqn = int(aliquot(i))
        if aliqn > i and aliqn <= max_number:
            if aliquot(aliqn) == i:
                print((i, aliqn))


generate_amicable_pairs(100000, 1000000)