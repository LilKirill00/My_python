#перевод градус цельсия в фаренгейтр
t_c=float(input("введите сколько градусов цельсия "))
def temp(t_c):
    t_c=9/5*t_c+32
    return t_c
print("в фаренгейтерах это будет",round(temp(t_c),3))

#вычисление площадь и периметр квадрата
a=int(input("введите сторону квадрата "))
def plshad(a):
    return a**2
def perimetr(a):
    return 4*a
print("площадь равна",plshad(a))
print("периметр равен",perimetr(a))

#среднее арифметическое трех чисел
sh1=float(input("первое число "))
sh2=float(input("второе число "))
sh3=float(input("третье число "))
def sred():
    summ=sh1+sh2+sh3
    return summ/3
print("среднее этих трех чисел равно",round(sred(),3))

#среднее трех чисел с значениями по умолчанию
def cred(x=0,y=0,z=0):
    return print('среднее этих трех чисел равно',round((x+y+z)/3,3))
x=input('первое число ')
if len(x)==0:
    x=0
    print(x)
else: x=float(x)
y=input('второе число ')
if len(y)==0:
    y=0
    print(y)
else: y = float(y)
z=input('третье число ')
if len(z)==0:
    z=0
    print(z)
else: z = float(z)
cred(x,y,z)

#формула герона
def F_gerona():
    from math import sqrt
    print("вычисление площади треугольника по трем сторонам")
    a = float(input("превая сторона: "))
    b = float(input("вторая сторона: "))
    c = float(input("третья сторона: "))
    p=(a+b+c)/2
    x=p*(p-a)*(p-b)*(p-c)
    if x>=0:
        print('площадь равна: ', sqrt(x))
    else: print('треугольник с такими сторонами невозможен')
    return