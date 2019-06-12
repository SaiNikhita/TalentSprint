import operator


def readfile():
    return open("marklist.txt").readlines()


def preprocess():
    file = readfile()
    marks_dictionary = {}
    for entry in file:
        marks_dictionary[entry.strip().split(" ")[0]] = int(entry.strip().split(" ")[1])
    return marks_dictionary


def tuple_to_dict(sorted_marks_tuple):
    return {a:b for (a,b) in sorted_marks_tuple}


def compute_ranks():
    rank_str = ""
    rank = 1
    prev_marks = 0
    marks = preprocess()
    sorted_tuple = sorted(marks.items(), key=operator.itemgetter(1), reverse=True)
    marks_dict = tuple_to_dict(sorted_tuple)
    for student in marks_dict:
        if prev_marks != marks_dict[student]:
            rank_str = rank_str + str(rank) + "\t" + str(student) + "\t" + str(marks_dict[student]) + "\n"
        else:
            rank_str = rank_str + " " + "\t" + str(student) + "\t" + str(marks_dict[student]) + "\n"

        prev_marks = marks_dict[student]
        rank = rank + 1
    return rank_str


print(compute_ranks())