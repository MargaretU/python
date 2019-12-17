def symetr(mas):
    for i in range(len(mas)):
        l = len(mas[i])
        for j in range(int(l/2)):
            if mas[i][j] != mas[i][l-j-1]:
                return False
    return True


def Show(mas):
     for i in range(len(mas)):
        for j in range(len(mas[i])):
            print(mas[i][j], end=' ')
        print()


print("Введіть кількість рядків")
rows = int(input())
print("Введіть кількість стовпців")
colums = int(input())
print("Ведіть елементи масиву через пробіл")
text = input()
arr = text.split()
if colums*rows != len(arr):
    print("Некоректна кількість елементів ")
else:
    mas = []
    j = 0
    for i in range(rows):
        row = []
        for i in range(colums):
            row.append(int(arr[j]))
            j = j+1
        mas.append(row)
    print("Масив:")
    Show(mas)
    if symetr(mas):
        print("має вертикальну вісь симетрії")
    else:
        print("НЕ має вертикальну вісь симетрії")
