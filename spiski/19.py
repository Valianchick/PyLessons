summa = 0
count = 0
lst = [1, 5, 6.3, 6, None, 2.0, -4, None]
for item in lst:
    if item != None:
        summa += item
        count += 1
sr = summa/count
for i in range(len(lst)):
    if lst[i] == None:
        lst[i] = sr
print(lst)