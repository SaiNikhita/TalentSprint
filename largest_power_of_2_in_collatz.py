def next_num(num):
    return int(num/2) if num % 2 == 0 else 3 * num + 1


def compute_series(num,series):
    series.append(num)
    if num == 1:
        return series
    else:
        num = next_num(num)
        series = compute_series(num, series)
        return series


def highest_number_in_series(series):
    return max(series)


def highest_power_of_2(series):
    max_power = 4
    end = highest_number_in_series(series)
    i = max_power
    while i <= end:
        i = 2 * i
        if i in series:
            max_power = i
    return max_power


num = 7
series = []
series = compute_series(num, series)
print(series)
print(highest_power_of_2(series))
