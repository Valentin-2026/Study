import tkinter as tk


def set_line_width():
    """Функция обновления толщины пера с обработкой исключений."""
    global current_width
    try:
        # Получаем текст из поля ввода и преобразуем в целое число
        value = int(entry_width.get())
        if value <= 0:
            print("Толщина должна быть положительным числом.")
            return
        current_width = value
        print(f"Толщина линии установлена: {current_width}")
    except ValueError:
        # Обработка случая, если введено не целое число
        print("Ошибка: пожалуйста, введите корректное целое число.")


def draw(event):
    """Функция рисования линии при движении мыши."""
    # Получаем координаты мыши
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)

    # Рисуем линию, используя глобальную переменную толщины
    canvas.create_line(x1, y1, x2, y2, fill=current_color, width=current_width, capstyle=tk.ROUND, smooth=True)


# --- Инициализация приложения ---
root = tk.Tk()
root.title("Графический редактор")

# Переменные состояния
current_width = 1  # Начальная толщина линии
current_color = "red"  # Цвет по умолчанию (как на вашем скриншоте)

# --- Создание холста ---
canvas = tk.Canvas(root, bg="white", width=800, height=600)
canvas.pack()

# Привязка событий мыши к функции draw
canvas.bind("<B1-Motion>", draw)

# --- Панель управления (нижняя часть) ---
control_frame = tk.Frame(root)
control_frame.pack(fill=tk.X, padx=10, pady=5)

# Палитра цветов (упрощенная, как на скриншоте)
colors = ["red", "green", "blue", "black"]
for color in colors:
    btn = tk.Button(control_frame, bg=color, width=5, command=lambda c=color: set_color(c))
    btn.pack(side=tk.LEFT, padx=2)


def set_color(color):
    global current_color
    current_color = color


# Поле ввода толщины
label_width = tk.Label(control_frame, text="Толщина линии:")
label_width.pack(side=tk.LEFT, padx=(20, 5))

entry_width = tk.Entry(control_frame, width=5)
entry_width.insert(0, str(current_width))  # Значение по умолчанию
entry_width.pack(side=tk.LEFT, padx=5)

# Кнопка установки толщины
btn_set_width = tk.Button(control_frame, text="Установить толщину", command=set_line_width)
btn_set_width.pack(side=tk.LEFT, padx=5)

# Запуск главного цикла
root.mainloop()