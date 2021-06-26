import random


def toss_on_a_day():
    count = 0
    for i in range(100):
        result = random.randint(0, 1)
        if result == 0:
            count = count +1
    return count


def toss_in_a_year():
    day_result = []
    for i in range(36500):
        day_result.append(toss_on_a_day())
    return day_result
