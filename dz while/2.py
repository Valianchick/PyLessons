import random

def generate():
    quan = random.randint(7, 11)
    print(quan)
    password = ""
    for item in range(1, quan+1):
        password += chr(random.randrange(33,126))
    print(f'Пароль: {password}')

generate()