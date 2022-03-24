(*Задание 1*)

try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = input("Введите операцию: +, -, /: ")
    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "/":
        if c == '0':
            print("Ошибка деления на ноль")
        else:
            print(a/b)
    else:
        print("Неправильно введена операция")
except ValueError:
    print("Ошибка преобразования типов")
    
    
(*Задание 2*)
def zadanie2():
    import requests
    import statistics 
    resp = requests.get('https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat')
    a = list(map(float,resp.text.split()))
    print(max(a), min(a), statistics.mean(a))
zadanie2()

(*Задание 3*)

