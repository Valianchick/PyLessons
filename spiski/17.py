import random

array_new = [random.randint(-10,10) for _ in range(10)]
min_i = array_new.index(min(array_new))
max_i = array_new.index(max(array_new))
if min_i < max_i:
    print(sum(array_new[min_i:max_i])/len(array_new[min_i:max_i]))
else:
    array_new[min_i] = (max(array_new)+min(array_new))/2
    array_new[max_i] = (max(array_new)+min(array_new))/2
    print(array_new)