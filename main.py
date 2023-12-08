import sys
import threading
import time

import pyautogui
import keyboard

from tkinter import Tk

PAUSE_POS = (-1, -1)  # позиция которую мы отлавливаем (-1, -1) - калибровка

COLOR_PAUSE = (-1, -1)  # цвет rgb паузы (-1, -1) - калибровка Только с калибровкой позиции

print()

if PAUSE_POS[0] < 0:  # Калибруем позицию
    print("В течении 8 секунд поставьте курсор на кнопку паузы")

    time.sleep(8)

    # Собственно калибруемся
    PAUSE_POS = (pyautogui.position().x, pyautogui.position().y)

    pyautogui.moveRel(-15, -15, duration=0.1)
    pyautogui.moveRel(15, 15, duration=0.1)
    pyautogui.moveRel(15, -20, duration=0.1)
    pyautogui.moveRel(-15, 20, duration=0.1)

    # Выводим значения на экран
    print(F"\nПозиция паузы - {PAUSE_POS}, можете вставить это значение в переменную 'PAUSE_POS' "
          "чтобы избежать повторную калибровку\n")

if COLOR_PAUSE[0] < 0:  # Нужно откалибровать цвет
    print("В течении 5 секунд считается цвет пикселя при остановке" +
          "\n!НЕ ЗАБЫВАЙТЕ ЧТО ЦВЕТ МОЖЕТ МЕНЯТСЯ ПРИ НАВЕДЕНИИ КУРСОРА!")

    time.sleep(8)
    COLOR_PAUSE = pyautogui.screenshot().getpixel((PAUSE_POS[0], PAUSE_POS[1]))

    # рисуем курсором мыши галочку
    pyautogui.moveRel(-15, -15, duration=0.1)
    pyautogui.moveRel(15, 15, duration=0.1)
    pyautogui.moveRel(15, -20, duration=0.1)
    pyautogui.moveRel(-15, 20, duration=0.1)
    time.sleep(0.5)

    print(F"Цвет паузы откалиброван как {COLOR_PAUSE}, можете вставить это значение в переменную 'COLOR_PAUSE'\n")

print("Работа программы начнётся через 10 секунд")
time.sleep(8)
pyautogui.moveTo(PAUSE_POS[0], PAUSE_POS[1], 1)
time.sleep(1)
pyautogui.moveRel(0, -50, 0.5)
time.sleep(1)
print("Началась, для выхода зажмите 'Esc'")


def chek():
    if pyautogui.screenshot().getpixel((PAUSE_POS[0], PAUSE_POS[1])) == COLOR_PAUSE:
        keyboard.press("Shift + Alt")
        time.sleep(0.1)
        keyboard.press("Tab")
        time.sleep(0.1)
        keyboard.release("Shift + Alt + Tab")

        pyautogui.moveTo(pyautogui.size().height, pyautogui.size().width, duration=0.3)
        print("Переключение")

    if not keyboard.is_pressed("Esc"):
        threading.Timer(0.2, chek).start()
    else:
        gui.destroy()
        sys.exit("Вы нажали Esc для выхода")


gui = Tk(className="Ninja")
gui.attributes("-fullscreen", True)
gui.configure(bg="black")

threading.Timer(5, chek).start()

gui.mainloop()
