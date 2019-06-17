import itertools


class Odometer:
    def __init__(self, size):
        self.digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.combos = [i for i in itertools.combinations(self.digits, size)]

    def num_to_tuple(self, num):
        return tuple([int(i) for i in str(num)])

    def tuple_to_num(self, tuple):
        string = ""
        for i in tuple:
            string = string + str(i)
        return int(string)

    def next_reading(self, current_reading):
        current_reading_list = self.num_to_tuple(current_reading)
        return self.tuple_to_num(self.combos[(self.combos.index(current_reading_list) + 1) % len(self.combos)])

    def prev_reading(self, current_reading):
        current_reading_list = self.num_to_tuple(current_reading)
        if self.combos.index(current_reading_list) == 0:
            return self.tuple_to_num(self.combos[len(self.combos) - 1])
        return self.tuple_to_num(self.combos[(self.combos.index(current_reading_list) - 1)])

    def next_nth_reading(self, current_reading, n):
        current_reading_list = self.num_to_tuple(current_reading)
        return self.tuple_to_num(self.combos[(self.combos.index(current_reading_list) + n) % len(self.combos)])

    def prev_nth_reading(self, current_reading, n):
        for i in range(0, n):
            new_reading = self.prev_reading(current_reading)
            current_reading = new_reading
        return new_reading

    def distance_between_readings(self, a, b):
        a_list = self.num_to_tuple(a)
        b_list = self.num_to_tuple(b)
        if a > b:
            return (self.combos.index(a_list) - self.combos.index(b_list)) % len(self.combos)
        else:
            return (self.combos.index(b_list) - self.combos.index(a_list)) % len(self.combos)


odo = Odometer(3)
print(odo.next_reading(689))
print(odo.prev_reading(123))
print(odo.next_nth_reading(123, 5))
print(odo.prev_nth_reading(789, 5))
print(odo.distance_between_readings(123, 789))