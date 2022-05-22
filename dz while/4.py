import random

def generate():
    kolvo = 0
    while True:
        quan = random.randint(7, 11)
        password = ""
        for item in range(1, quan+1):
            password += chr(random.randrange(33,126))
        kolvo += 1
        k = 0
        if len(password) >= 8:
            k += 1
        low = 0
        high = 0
        digit = 0
        for item in password:
            if item.isupper():
                low += 1
            else:
                high += 1
            if item.isdigit():
                digit += 1
        if k > 0 and low > 0 and high > 0 and digit > 0:
            print(f'Пароль создан с {kolvo} раза')
            print(f'Пароль: {password}')
            break

generate()