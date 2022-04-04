import requests
import random
import statistics
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
    resp = requests.get('https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat')
    a = list(map(float,resp.text.split()))
    print(max(a), min(a), statistics.mean(a))
zadanie2()

(*Задание 3*)

def zadanie3():
    file = requests.get("https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/moby.txt").content.split()
    new = []
    for elem in file:
        new.append(str(elem)[2:-1].lower().replace(",", '').replace(".", '').replace("--", ''))
    with open("moby_clean.txt", "w", encoding='cp1251') as file:
        for elem in new:
            file.write(elem + "\n")
           
print(zadanie3())

(*Задание 4*)

def zadanie4():
    with open("moby_clean.txt", "r", encoding='cp1251') as file:
        new = file.read().split()
        counter = {elem: new.count(elem) for elem in new}
        sorter = sorted(counter.items(), key=lambda x: x[1])[::-1]
        print(f"Самые частые слова {sorter[0:5]},\n"
              f"Cамые редкие слова {sorter[-5:]}")
print(zadanie4())

(*Задание 5*)

def zadanie5():
    answer = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/responses.txt").text.split("\n")
    ask = input("Введите вопрос: ")
    while ask != "close":
        print(random.choice(answer))
        ask = input("Введите вопрос: ")
print(zadanie5())

(*Задание 6*)

def zadanie6():
    file = requests.get("http://dfedorov.spb.ru/python3/src/romeo.txt").text.split()
    counter = {elem: file.count(elem) for elem in file}
    sorter = sorted(counter.items(), key=lambda x: x[1])[::-1]
    print("Частота использования слов:")
    for elem in sorter:
        print(dict({elem})
print(zadanie6())
              
              
