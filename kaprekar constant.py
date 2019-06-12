def num_to_list(num):
    return [int(digit) for digit in str(num)]


def list_to_num(digits):
    num = ""
    for digit in digits:
        num = num + str(digit)
    return int(num)


def has_unique_digits(digits):
    return len(digits) == len(set(digits))


def compute_kaprekar_constant(num):
    prev_diff = num
    digits = num_to_list(num)
    if not has_unique_digits(digits) or num == 0:
        return "No Kaprekar Constant"
    smallest_num = list_to_num(sorted(digits))
    largest_num = list_to_num(sorted(digits, reverse=True))
    current_dif = largest_num - smallest_num
    if current_dif == prev_diff:
        return current_dif
    else:
        return compute_kaprekar_constant(current_dif)


num = 123
print(compute_kaprekar_constant(num))