import time, signal, sys
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

mouse = Controller()

toggleKey = KeyCode(char='x'); "кнопка для переключения режимов"
isClicking = False; "переключатель"
Pause = 0; "задержка в секундах"


def clicker():
    global Pause
    while True:
        if isClicking:
            mouse.click(Button.left, 1)
            time.sleep(pause/1000)


def toggle_event(key):
    if key == toggleKey:
        global isClicking
        isClicking = not isClicking
        print(isClicking)


def main():
    clicking_thread = threading.Thread(target=clicker)
    clicking_thread.daemon = True
    clicking_thread.start()

    with Listener(on_press=toggle_event) as listener:
        listener.join()

if __name__ == '__main__':
    try:
        pause = int(input("Задержка в ms: "))
        print("Для переключения кликера нажмите", toggleKey)
        print(isClicking)
        main()
    except KeyboardInterrupt:
        print("\nПрограмма была прервана. Завершение работы...")
