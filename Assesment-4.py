import re


def terminus(lattice_point, steps):
    directions = {'N': (0, 1),'S': (0, -1),'E': (1, 0),'W': (-1, 0),'NE': (1, 1),'NW': (-1, 1),'SE': (1, -1),'SW': (-1, -1)}
    lattice_point = list(lattice_point)
    for step in steps:
        num_of_steps = list(filter(None, re.split('[NSEW+]', step)))
        direction = list(filter(None, re.split('[0-9+]', step)))
        for i in range(int(num_of_steps[0])):
            lattice_point[0] += directions[direction[0]][0]
            lattice_point[1] += directions[direction[0]][1]
    return lattice_point



print(terminus((-1,1),["1NE"]))