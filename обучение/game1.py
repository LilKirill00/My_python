import random

print('Игра (Угадай число)')

n = 0
vveli = []
print('Привет, как тебя зовут')
name = input()

number = random.randint(1, 100)

print('Итак, ' + name + ', Я загадал число между 1 и 100.')

while n < 8:
    print('Я загадал:')
    g = input()

    try:
        vveli.index(g)
        print('Такое число уже было введено')
        continue
    except ValueError:
        vveli.append(g)

    n = n + 1

    if int(g) < number:
        print('Нет, моё число больше')

    if int(g) > number:
        print('Нет, моё число меньше')

    if int(g) == number:
        break

if int(g) == number:
    print('Отлично,' + name + '! Вы угадали мое число! Ваше количество попыток в этой игре:', n)

if int(g) != number:
    print('Не угадал. Моё число -', number)