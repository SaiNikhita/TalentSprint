def is_ambiguous(date):
    date = date.split("/")
    return int(date[0]) < 12 and int(date[1]) < 12


date = "01/02/1999"
print(is_ambiguous(date))