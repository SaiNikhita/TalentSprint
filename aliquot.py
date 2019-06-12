def is_factor(divisor, num):
    return num % divisor == 0


def aliquot(num):
    aliquot = 0
    for i in range(1, int(num/2)+1):
        if is_factor(i, num):
            aliquot = aliquot + i
    return aliquot


print(aliquot(12))

