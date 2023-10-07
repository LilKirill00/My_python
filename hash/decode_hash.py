import hashlib

# попробовать расхешировать по списку возможных значений

input_hash = input('Input hash: ')

password_file = open('passwords.txt', 'r')

try:
    with open('passwords.txt', 'r') as password_file:
        for word in password_file:
            # Удаление символов новой строки и пробелов
            word = word.strip()
            hash_obj = hashlib.md5(word.encode())
            word_hex = hash_obj.hexdigest()

            if input_hash == word_hex:
                print(word, ' = ', word_hex)
                break
        else:
            print("Пароль не найден.")
except FileNotFoundError:
    print("Файл passwords.txt не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
