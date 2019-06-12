import itertools
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def num_to_tuple(num):
    return tuple([int(i) for i in str(num)])


def tuple_to_num(tuple):
    string = ""
    for i in tuple:
        string = string + str(i)
    return int(string)


def generate_possible_readings(size):
    combinations = itertools.combinations(digits, size)
    return [i for i in combinations]


def initialize(size):
    combos = generate_possible_readings(size)
    return combos[0]


def next_reading(current_reading):
    combos = generate_possible_readings(len(str(current_reading)))
    current_reading_list = num_to_tuple(current_reading)
    return combos[(combos.index(current_reading_list) + 1) % len(combos)]


def prev_reading(current_reading):
    combos = generate_possible_readings(len(str(current_reading)))
    current_reading_list = num_to_tuple(current_reading)
    if combos.index(current_reading_list) == 0:
        return combos[len(combos)-1]
    return combos[(combos.index(current_reading_list) - 1)]


def next_nth_reading(current_reading, n):
    combos = generate_possible_readings(len(str(current_reading)))
    current_reading_list = num_to_tuple(current_reading)
    return combos[(combos.index(current_reading_list) + n) % len(combos)]


def prev_nth_reading(current_reading, n):
    for i in range(0, n):
        new_reading = prev_reading(current_reading)
        current_reading = tuple_to_num(new_reading)
    return new_reading


def distance_between_readings(a, b):
    combos = generate_possible_readings(len(str(a)))
    a_list = num_to_tuple(a)
    b_list = num_to_tuple(b)
    if a > b:
        return combos.index(a_list) - combos.index(b_list)
    else:
        return combos.index(b_list) - combos.index(a_list)


print(initialize(3))
print(next_reading(689))
print(prev_reading(123))
print(next_nth_reading(123, 5))
print(prev_nth_reading(789, 5))
print(distance_between_readings(123, 789))