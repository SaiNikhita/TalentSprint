def cube_root(n):
    return int(n ** (1/3))


def get_triples(max):
    triples = ""
    count = 0
    c = 3
    while count != max:
        cube_of_numbers = [i ** 3 for i in range(1, c)]
        for a_cube in cube_of_numbers:
            for b_cube in cube_of_numbers:
                if a_cube + b_cube == c ** 2:
                    count = count + 1
                    triples = triples + str(cube_root(a_cube)) + "," + str(cube_root(b_cube)) + "," + str((c)) + "\n"
        c = c + 1
    return triples


print(get_triples(10))