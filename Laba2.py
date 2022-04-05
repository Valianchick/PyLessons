def r():
    file = open("students.txt", "r", encoding="utf8")
    lst = file.readlines()
    file.close()
    return lst

def write(lst):
    lst.sort()
    file = open("students.txt", "w", encoding="utf8")
    for student in lst:
        file.write(student + "\n")
    file.close()

def append(surname: str, name: str):
    lst = r()
    student = surname + ' ' + name + '\n'
    if student in lst:
        return (f"Студент уже есть в списке")
    else:
        lst.append(student)
        write(lst)
        return (f"Студент добавлен")

def find(surname: str, name = None):
    lst = r()
    lst1 = []
    for student in lst:
        if (name == "") and (surname in student):
                lst1.append(student)
        elif surname in student:
            if name in student:
                return (f"Студент в группе")
            else:
                return (f"Студента нет в группе")
    if len(lst1) > 0:
        return [print(item) for item in lst1]
    else:
        return (f"Студенты с данной фамилией не найдены")

def edit(surname: str, name: str, newsurname = None, newname = None):
    lst = r()
    for student in lst:
        if (surname in student) and (name in student):
                cod = lst.cod(surname + " " + name + "\n")
                if newsurname != "":
                    surname = newsurname
                if newname != "":
                    name = newname
                lst[cod] = surname + " " + name + "\n"
                lst.sort()
                write(lst)
                return (f"Данные изменены")
    return (f"Студент не найден")

print('Введите help, чтобы посмотреть команды')
inp = input("Введите команду: ")

while inp != "exit":
    if inp == "help":
        print("exit - выйти\nappend - добавить нового студента\nfind - найти студента\nedit - редактировать информацию о студенте" )
    elif inp == "append":
        surname = input("Введите фамилию студента: ")
        name = input("Введите имя студента: ")
        print(append(surname, name))
    elif inp == "find":
        surname = input("Введите фамилию студента: ")
        name = input("Введите имя студента или ENTER: ")
        print(find(surname, name))
    elif inp == "edit":
        surname = input("Введите фамилию студента: ")
        name = input("Введите имя студента: ")
        newsurname = input("Введите новую фамилию студента: ")
        newname = input("Введите новое имя студента: ")
        print(edit(surname, name, newsurname, newname))
    inp = input("Введите команду: ")

