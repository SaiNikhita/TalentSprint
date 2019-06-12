def convert2digits(n: int) -> str:
    upto20 = ["", "One ", "Two ", "three ", "Four ", "Five ", "Six ",
            "Seven ", "Eight ", "nine ", "Ten ", "Eleven ", "Twelve ",
            "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ",
            "Seventeen ", "Eighteen ", "Ninteen "]
    tens = ["", "Ten ", "Twenty ", "Thirty ", "Forty ", "Fifty ",
            "Sixty ", "Seventy ", "Eighty ", "Ninety "]

    if n < 20:
        return upto20[n]
    return tens[n // 10] + upto20[ n % 10]

def convert3digits(n: int) -> str:
    if n < 100:
        return convert2digits(n)
    return convert2digits(n // 100) + "Hundred " + convert2digits(n % 100)

def split(n: int, denoms: [int]) -> [(int, int)]:
    if len(denoms) == 1:
        return [(n, denoms[0])]
    return [(n // denoms[0], denoms[0])] + split(n % denoms[0], denoms[1:])

def convert_denoms(pairs: [(int, int)], names: {int:str}) ->[(int, str)]:
    return [(a, names[b]) for a, b in pairs]

def convert_times(pairs:[(int, str)]) -> [(str, str)]:
    denoms = {10000000: "Crore ", 100000: "Lakh ", 1000: "Thousand ", 1:""}
    denom_names = denoms.values()
    denom_values = denom.keys()






"""special_names = ["", " thousand", " million", " billion"]
tens_names = ["", " ten", " twenty", " thirty", " forty", " fifty",\
              " sixty", " seventy", " eighty", " ninety"]
digit_names = ["", " one", " two", " three", " four", " five",\
               " six", " seven", " eight", " nine", " ten",\
               " eleven", " twelve", " thirteen", " fourteen", " fifteen",\
               " sixteen", " seventeen", " eighteen", " nineteen"]


def convert_less_than_hundred(number):
    if number % 100 < 20:
        return digit_names[number % 20]
    else:
        return tens_names[(number // 10) % 10] + digit_names[number % 10]


def convert_less_than_one_thousand(number):
    number_in_words = convert_less_than_hundred(number)
    hundreds_place_digit = number // 100
    if hundreds_place_digit == 0:
        return number_in_words
    else:
        return digit_names[hundreds_place_digit] + " hundred" + number_in_words


def convert_num_to_digits(number):
    if number == 0:
        return "zero"

    prefix = ""
    if number < 0:
        number = -number
        prefix = "negative"

    number_in_words = ""
    num_of_thousands = 0
    while number > 0:
        if number % 1000 != 0:
            number_in_words = convert_less_than_one_thousand(number % 1000) + special_names[num_of_thousands] + number_in_words
        number = number // 1000
        num_of_thousands = num_of_thousands + 1

    return prefix + number_in_words


print(convert_num_to_digits(-212567123345))"""
