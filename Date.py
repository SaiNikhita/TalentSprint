def preprocess(date):
    date = date.replace(",", " ")
    list = date.split(" ")
    list = [x for x in list if x]
    return list[0], list[1], list[2]


def calcuate_day(day, month, year):
    month_dict = {"jan" : 0, "feb" : 31, "mar" : 28 + month_dict["feb"]}


date = "30 March 2019"
day, month, year = preprocess(date)
print(calcuate_day(day, month, year))