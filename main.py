import random
import PySimpleGUI as sg

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = None

    layout = [[sg.Text("Введіть число від 1 до 100:")],
              [sg.Input()],
              [sg.Button('Перевірити'), sg.Button('Вихід')]]

    window = sg.Window('Вгадай число', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Вихід':
            break
        guess = int(values[0])
        if guess > number_to_guess:
            sg.popup("Завелике! Спробуйте ще раз.")
        elif guess < number_to_guess:
            sg.popup("Замале! Спробуйте ще раз.")
        else:
            sg.popup("Вітаємо! Ви вгадали число.")
            break

    window.close()

if __name__ == "__main__":
    guess_the_number()
