score = {0: 'Love', 1: '15', 2: '30', 3: '40'}


def get_score_names(a, b):
    if abs(a - b) >= 2:
        return "Game"
    if a == b:
        if a < 4:
            return score[a] + " all"
        else:
            return " deuce"
    else:
        if a > 4 and a - b == 1:
            return 'Advantage A'
        elif b > 4 and b - a == 1:
            return 'Advantage B'
        return score[a] + "-" + score[b]


print(get_score_names(5,6))