# Импорт библиотек
import tkinter as tk
from tkinter import *
import os


# Импорт настроек
import calc_settings as cs


# Создание окна приложения
calc = tk.Tk()
calc.geometry(cs.main_set[0])
calc.title(cs.localization(0))
calc.option_add("*Font", cs.main_set[1])  # Установка шрифта по умолчанию 
calc.resizable(False, False)  # Запрет изменения размеров окна
# Установка иконки
ico_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), cs.main_set[2])
#calc.iconbitmap(ico_path) #Раскомментируйте, если у вас есть файл иконки

# Создание окна ввода
input_box = tk.Entry(calc, font=(cs.main_set[3], 15))
input_box.place(x=20, y=10, height=40, width=310)
# Создание окна вывода результата
input_box2 = tk.Entry(calc, font=(cs.main_set[3], 15))
input_box2.place(x=100, y=60, height=40, width=230)
input_box2.config(state='readonly')

# Функция для вычисления выражения
def answer():
    ans = str(input_box.get())
    # Обработка ошибок выражения
    try: 
        
        evaluate = eval(ans)
    except SyntaxError:  # Обработка синтаксических ошибок:  
        evaluate = cs.localization(1)  
    except ZeroDivisionError:  # Обработка ошибки деления на ноль:  
        evaluate = cs.localization(2) 
        

    input_box2.config(state='normal')
    input_box2.delete(0, END)
    input_box2.insert(END, evaluate)
    input_box2.config(state='readonly')

# Функция для ввода символов
def input_num(num):
    dv = str(input_box.get())
    num = dv + str(num)
    input_box.delete(0, END)
    input_box.insert(END, num)
    
# Функция для очистки окна ввода
def clear_display():
    input_box.delete(0,END)
    input_box2.config(state='normal')
    input_box2.delete(0,END)
    input_box2.config(state='readonly')
  
# Функция для удаления последнего символа в строке ввода    
def backspace():
    bs = input_box.get()
    input_box.delete(0, END)
    input_box.insert(0, bs[0:-1])

# Первая строка кнопок
Button(text="%", font=(cs.main_set[3], 15), command=lambda: input_num("%")).place(x=20, y=110, height=50, width=70)
Button(text="CE", font=(cs.main_set[3], 14), bg=main_set[4], command=clear_display).place(x=100, y=110, height=50, width=70)
Button(text="C", font=(cs.main_set[3], 14), bg=main_set[4], command=clear_display).place(x=180, y=110, height=50, width=70)
Button(text="⌫", font=(cs.main_set[3], 12), bg=main_set[4], command=backspace).place(x=260, y=110, height=50, width=70)

# Вторая строка кнопок
Button(text="(", font=(cs.main_set[3], 15), command=lambda: input_num("(")).place(x=20, y=170, height=50, width=70)
Button(text="𝑥²", font=(cs.main_set[3], 15), command=lambda: input_num("**2")).place(x=100, y=170, height=50, width=70)
Button(text=")", font=(cs.main_set[3], 15), command=lambda: input_num(")")).place(x=180, y=170, height=50, width=70)
Button(text="÷", font=(cs.main_set[3], 18), command=lambda: input_num("/")).place(x=260, y=170, height=50, width=70)

# Третья строка кнопок
Button(text="7", font=(cs.main_set[3], 15), command=lambda: input_num(7)).place(x=20, y=230, height=50, width=70)
Button(text="8", font=(cs.main_set[3], 15), command=lambda: input_num(8)).place(x=100, y=230, height=50, width=70)
Button(text="9", font=(cs.main_set[3], 15), command=lambda: input_num(9)).place(x=180, y=230, height=50, width=70)
Button(text="×", font=(cs.main_set[3], 15), command=lambda: input_num("*")).place(x=260, y=230, height=50, width=70)

# Четвертая строка кнопок
Button(text="4", font=(cs.main_set[3], 15), command=lambda: input_num(4)).place(x=20, y=290, height=50, width=70)
Button(text="5", font=(cs.main_set[3], 15), command=lambda: input_num(5)).place(x=100, y=290, height=50, width=70)
Button(text="6", font=(cs.main_set[3], 15), command=lambda: input_num(6)).place(x=180, y=290, height=50, width=70)
Button(text="-", font=(cs.main_set[3], 15), command=lambda: input_num("-")).place(x=260, y=290, height=50, width=70)

# Пятая строка кнопок
Button(text="1", font=(cs.main_set[3], 15), command=lambda: input_num(1)).place(x=20, y=350, height=50, width=70)
Button(text="2", font=(cs.main_set[3], 15), command=lambda: input_num(2)).place(x=100, y=350, height=50, width=70)
Button(text="3", font=(cs.main_set[3], 15), command=lambda: input_num(3)).place(x=180, y=350, height=50, width=70)
Button(text="+", font=(cs.main_set[3], 15), command=lambda: input_num("+")).place(x=260, y=350, height=50, width=70)

# Шестая строка кнопок
Button(text="+/-", font=(cs.main_set[3], 15), command=lambda: input_num("-")).place(x=20, y=410, height=50, width=70)
Button(text="0", font=(cs.main_set[3], 15), command=lambda: input_num(0)).place(x=100, y=410, height=50, width=70)
Button(text=".", font=(cs.main_set[3], 15), command=lambda: input_num(".")).place(x=180, y=410, height=50, width=70)
Button(text="=", font=(cs.main_set[3], 15), bg=cs.main_set[5], command=answer).place(x=260, y=410, height=50, width=70)


#Запуск программы
calc.mainloop()