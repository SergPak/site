#В этом блоке кода импортируются необходимые модули - `random` и `tkinter`.
# `random` используется для генерации случайного числа,
# а `tkinter` - для создания графического интерфейса приложения.

import random
from tkinter import *

# Dictionary and vars
# создается словарь `schema`, который содержит правила для
# определения победителя в игре "Камень, Бумага, Ножницы"

schema = {
    "Камень": {"Камень": 1, "Бумага": 0, "Ножницы": 2},
    "Бумага": {"Камень": 2, "Бумага": 1, "Ножницы": 0},
    "Ножницы": {"Камень": 0, "Бумага": 2, "Ножницы": 1}
}

# инициализируются переменные `comp_score` и `player_score`
# для хранения счета игры.

comp_score = 0
player_score = 0

# Functions
# В этом блоке кода определена функция `outcome_handler`, которая вызывается
# при выборе игроком своего варианта - "Камень", "Бумага" или "Ножницы".
# Внутри функции генерируется случайное число для выбора варианта компьютера.
# После этого с помощью словаря `schema` определяется результат игры и о
# бновляется счет игрока и компьютера в зависимости от результата.
# Также обновляются надписи на экране с выбором игрока, выбором компьютера и результатом игры.
def outcome_handler(user_choice):
    global comp_score
    global player_score
    outcomes = ["Камень", "Бумага", "Ножницы"]
    random_number = random.randint(0, 2)
    computer_choice = outcomes[random_number]
    result = schema[user_choice][computer_choice]

    player_choice_label.config(fg="red", text="Выбор игрока: " + str(user_choice))
    computer_choice_label.config(fg="green", text="Выбор компьютера: " + str(computer_choice))

    if result == 2:
        player_score += 2
        player_score_label.config(text="Игрок: " + str(player_score))
        outcome_label.config(fg="blue", text="Результат: Игрок победил")
    elif result == 1:
        player_score += 1
        comp_score += 1
        player_score_label.config(text="Игрок: " + str(player_score))
        computer_score_label.config(text="Компьютер: " + str(comp_score))
        outcome_label.config(fg="blue", text="Результат: Ничья")
    elif result == 0:
        comp_score += 2
        computer_score_label.config(text="Компьютер: " + str(comp_score))
        outcome_label.config(fg="blue", text="Результат: Компьютер победил")


# Main screen
# Этот блок кода отвечает за создание графического интерфейса игры с помощью библиотеки `tkinter`.
# Создается основное окно приложения с названием "КНМ".
# Затем создаются метки, которые отображают текущий счет игры, выбор игрока, выбор компьютера и результат игры.

master = Tk()
master.title("КНМ")

# Labels
# создаются кнопки для выбора варианта игры - "Камень", "Бумага" и "Ножницы".


Label(master, text="Камень, Ножницы, Бумага", font=("Calibri", 14)).grid(row=0, sticky=N, pady=10, padx=200)
Label(master, text="Пожалуйста, выберите вариант", font=("Calibri", 12)).grid(row=1, sticky=N)
player_score_label = Label(master, text="Игрок: 0", font=("Calibri", 12))
player_score_label.grid(row=2, sticky=W)
computer_score_label = Label(master, text="Компьютер: 0", font=("Calibri", 12))
computer_score_label.grid(row=2, sticky=E)
player_choice_label = Label(master, font=("Calibri", 12))
player_choice_label.grid(row=3, sticky=W)
computer_choice_label = Label(master, font=("Calibri", 12))
computer_choice_label.grid(row=3, sticky=E)
outcome_label = Label(master, font=("Calibri", 12))
outcome_label.grid(row=3, sticky=N)

# Buttons
Button(master, text="Камень", width=15, command=lambda: outcome_handler("Камень")).grid(row=4, sticky=W, padx=5, pady=5)
Button(master, text="Бумага", width=15, command=lambda: outcome_handler("Бумага")).grid(row=4, sticky=N, pady=5)
Button(master, text="Ножницы", width=15, command=lambda: outcome_handler("Ножницы")).grid(row=4, sticky=E, padx=5, pady=5)

# Dummy Label
# создается пустая метка для отступа и запускается основной цикл обработки событий `mainloop()`

Label(master).grid(row=5)

master.mainloop()