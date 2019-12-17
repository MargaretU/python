from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')

#Перевірка рівняння чи нерівність
def d(text):
    i = text.find("<") 
    i1 = text.find(">")
    if i != -1 or i1 != -1:
        return 0 #нерівність
    else:
        return 1 #рівняння
#Максимальний степінь

def stepin(text):
    step = 0
    j = 0
    k = int(len(text))
    while j < k:
        if text[j] == "^":
            temp = int(text[j+1])
            if temp > step:
                step = temp
        j = j + 1
    return step

    
f = open('lab11.txt', 'r')
text = f.readline()
my_string = "1"
text = f.readlines()
n = int(len(text))
nev_text = []
for i in range(n):
    text[i] = text[i].lower()
for i in range(n):
    stroka = text[i]
    stroka = stroka.replace("^", "**")
    stroka = stroka.replace('x', '*x')
    stroka = stroka.replace('-*x', '-1*x')
    if stroka[0] == '*':
        stroka = my_string + stroka
    nev_text.append(stroka)
f.close()


for i in range(n):
    p = text[i]
    s = stepin(p)
    if s == 0:
        print("Рівняння першого степеня")
    else:
        print("Максимальний степінь:", s)
    riv = d(nev_text[i])
    kus = nev_text[i]
    if riv == 1:
        print(nev_text[i], end = '')
        kus = kus.split('=')
        res = solve(kus[0], x )
        print("Рівняння")
        print("Розв'язок: ", res)
    else:
        print(nev_text[i], end = '')
        print(" Нерівність", end = '\n')
        n = solve(kus)
        if n == False:
            print("Немає розв`язків")
        elif n == True:
            print("Розв'язок: (x > -oo) & (x < oo)", end = '\n')
        else:
            print("Розв'язок: ", n)
    print("______________________________________________________")
