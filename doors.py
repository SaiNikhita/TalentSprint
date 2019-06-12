def num_of_factors(num):
    fac=[1,num]
    i = 2
    while i * i < num:
        if num % i == 0:
            fac.append(i)
        i += 1
    if i * i == num:
        fac.append(i)
    return len(fac)


def manipulate_doors(doors_open):
    for door in range(100,4,-1):
        num_of_facs = num_of_factors(door)
        if num_of_facs % 2 != 0:
            doors_open[door] = not doors_open[door]
    return doors_open

doors_open=[False]*100
print(manipulate_doors(doors_open))