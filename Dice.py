import random

def roll_dice(possible_outcomes):
    return random.choice(possible_outcomes)

def count_freq(possible_outcomes, freq):
    freq[roll_dice(possible_outcomes) - 1] += 1
    return freq


def freq_distribution(throws):
    possible_outcomes = [1, 2, 3, 4, 5, 6]
    freq = [0]*6
    for throw in range(0, throws):
        freq = count_freq(possible_outcomes, freq)
    for i in freq:
        freq[freq.index(i)] = i / throws
    return freq

freq = freq_distribution(10000)
print("Actual  ", freq)
print("Expected", [1666/10000]*6)
print("Actual","Expected")
for i in range(0, len(freq)):
    print(freq[i],1666/10000)
