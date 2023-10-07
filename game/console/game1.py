import random

def game1(username: str):
    """
    Игра (Угадай число)

    :param username: имя по которому будем обрашаться
    :return:
    """

    tryCount = 0; "Количество попыток"
    inputList = []; "Список уже введеных значений"
    isFind = False; "Угадано ли число"

    number = random.randint(1, 100); "Загаданное число"

    print("Игра (Угадай число)")
    print('Итак, ' + username + ', Я загадал число между 1 и 100.')

    while tryCount < 8:
        userReply = input('Я загадал: '); "Ответ пользователя"

        # Проверяем введено ли число
        try:
            isinstance(int(userReply), int)
        except ValueError:
            print('Введеное значение не яляется числом, повторите попытку')
            continue

        # Проверяем было ли такое число введено
        try:
            inputList.index(userReply)
            print('Такое число уже было введено')
            continue
        except ValueError:
            inputList.append(userReply)

        tryCount = tryCount + 1

        if int(userReply) < number:
            print('Нет, моё число больше')
        elif int(userReply) > number:
            print('Нет, моё число меньше')
        elif int(userReply) == number:
            print('Отлично,' + username + '! Вы угадали мое число! Ваше количество попыток в этой игре:', tryCount)
            isFind = True
            break

    if not isFind:
        print('Не угадал. Моё число -', number)

    print("Хотите ли сыграть еще раз:\n")
    print("\t1 - Да")
    print("\t0 - Назад")
    again = input("Ваш выбор: ")
    if again == '1':
        game1(username)
    else:
        return

if __name__ == '__main__':
    try:
        print("Привет, как тебя зовут?")
        username = input("Меня зовут: ")
        while True:
            print("Выберите игру:")
            print("\t1 - Угадай число")
            print("\t0 - Выход")
            selectGame = input("Ваш выбор: ")
            if selectGame == '1':
                game1(username=username)
            else:
                exit()
    except KeyboardInterrupt:
        print("\nПрограмма была прервана. Завершение работы...")