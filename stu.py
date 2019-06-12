import itertools

def get_num_subjects(list_of_students, marks_of_students):
    return len(marks_of_students[list_of_students[0]])


def read_marks():
    marks_of_students = {}
    for line in open("student-ranking.txt").readlines():
        marks_of_students[line.split()[0]] = [int(i) for i in line.split()[1:]]
    return list(marks_of_students.keys()), marks_of_students

def compute_relationships(list_of_students, marks_of_students):
    list_of_relationships = []
    num_subjects = get_num_subjects(list_of_students, marks_of_students)
    for combination in itertools.combinations(list_of_students, 2):
        count = 0
        for i in range(0, num_subjects):
            if marks_of_students[combination[0]][i] > marks_of_students[combination[1]][i]:
                count += 1
        if count == num_subjects:
            list_of_relationships.append(combination[1] + '<' + combination[0])
        elif count == 0:
            list_of_relationships.append(combination[0] + '<' + combination[1])
    return list_of_relationships

def reduceExpression (all_expression):
    i = 0
    while i < len(all_expression) - 1:
        pick = all_expression[i][2]
        j = 0
        while j < len(all_expression) :
            if j != i and pick == all_expression[j][0]:
                if (all_expression[i][0] + str('<') + all_expression[j][2]) in all_expression:
                    all_expression.remove(all_expression[i][0] + str('<') + all_expression[j][2])
            j += 1
        i += 1
    return all_expression

list_of_students, marks_of_students = read_marks()
relationships = compute_relationships(list_of_students, marks_of_students)
print(reduceExpression(relationships))