
from tkinter import *
from tkinter import messagebox as mb
import random


def check():
    s = e.get()
    s = int(s)
    rnd = random.randint(1, 2)
    if s == rnd:
        mb.showinfo(title="Результат", message="Угадал!")
    else:
        mb.showinfo(title="Результат", message="Неудача :(")

    answer = mb.askretrycancel(title="Вопрос", message="Загадать еще одно число?")
    if answer:
        e.delete(0, END)
    else:
        window.destroy()


window = Tk()
window.title('Игра "Угадай число"')
m1 = Label(height=3, text="Введи число, которое я загадал, и нажми на кнопку")
m1.pack()
e = Entry()
e.pack()
b = Button(text="Передать", command=check)
b.pack()
m = Label(height=3)
m.pack()
window.mainloop()
