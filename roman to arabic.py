def is_roman_num(roman_num):
    max_consequent_roman_count = {'M': 3, 'CM': 1, 'D': 1, 'CD': 1, 'C': 3, 'XC': 1, 'L': 1, 'XL': 1, 'X': 3, 'IX': 1, 'V': 1, 'IV': 1, 'I': 3}
    count = 1
    for i in range(0, len(roman_num)-1):
        if roman_num[i] == roman_num[i+1]:
            count += 1
            if count > max_consequent_roman_count[roman_num[i]]:
                return False
        else:
            count = 1
    return True


def next_roman_num(roman_num, index, roman_to_arabic_dict):
    if index == len(roman_num)-1:
        return roman_num[index]
    else:
        next_two_literals=roman_num[index:index+2]
        return next_two_literals if next_two_literals in roman_to_arabic_dict else roman_num[index]


def roman_to_int(roman_num, roman_to_arabic_dict):
    roman_num = roman_num.upper(  )
    index=0
    result=0
    if is_roman_num(roman_num):
        while index < len(roman_num):
            next_roman = next_roman_num(roman_num, index, roman_to_arabic_dict)
            result = result + roman_to_arabic_dict[next_roman]
            index = index + len(next_roman)
        return result
    else:
        return "Not Roman"


roman_to_arabic_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
print(roman_to_int("XIV", roman_to_arabic_dict))