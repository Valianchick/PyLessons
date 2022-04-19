import json

flag = True
name_file = input("Введите имя файла формата .json : ")
try:
    with open(name_file, "r", encoding='utf-8') as file:
        todo = json.load(file)
except:
    print("Ошибка")
    flag = False

def add(lst):
    task = input("Сформулируйте задачу: ")
    category = input("Добавьте категорию к задаче: ")
    time = input("Добавьте время к задаче: ")
    with open(name_file, "w", encoding='utf-8') as file:
        todo.append({"task": task, "category": category, "time": time})
        json.dump(todo, file)

def output(lst):
    for item in todo:
        for key, value in item.items():
            print(f"{key}: {value}, ", end="")
        print("")

while (flag):
    print(f"""Простой todo:
 1. Добавить задачу.
 2. Вывести весь список текущих задач.
 3. Выход.""")
    vvod = input("Укажите число: ")

    if vvod == "1":
        add(todo)

    elif vvod == "2":
        output(todo)

    elif vvod == "3":
        print("Задачи сохранены в файл!")
        flag = False
