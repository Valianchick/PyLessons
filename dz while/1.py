import random
num = random.randint(1, 10)

while True:
    num_user = int(input("Введите число: "))
    if num == num_user:
        print("Вы ввели случайно выбранное число")
        break
    elif num < num_user:
        print("Загаданное число меньше")
    else:
        print("Загаданное число больше")
