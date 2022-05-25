import math

def task6(lst: list):
    new = []
    for item in lst:
        if item > 0:
            new.append(math.log(item))
        else:
            new.append(None)
    return new
print(task6([1, 3, 2.5, -1, 9, 0, 2.71]))
