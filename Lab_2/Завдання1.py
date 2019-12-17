#Формується список із n дійсних випадкових чисел.
#Вивести ті числа, які після впорядкування за зростанням збільшили свій номер.
import random
n = int(input("Введіть кількість випадкових чисел: "))
mas = []
for i in range(n):
  mas.append(random.uniform(-100, 100))
print(mas)

mascopy = mas.copy()
mascopy.sort()
print(mascopy)
li = []
for i in range(len(mas)):
    li.append([mas[i], i])
li.sort()
sp = []
for i in range(len(mas)):
    if i > li[i][1]:
      sp.append(li[i][0])
print(sp)
