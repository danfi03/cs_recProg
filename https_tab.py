import tkinter as tk
from tkinter import ttk
import random
import time


class HttpTab:
    def __init__(self, parent, root_window):
        self.tab = ttk.Frame(parent)
        self.root = root_window  # Сохраняем ссылку на root

        # Заголовок
        self.header_label = tk.Label(
            self.tab,
            text="Почему важно использовать HTTPS?",
            font=("Arial", 16, "bold"),
            bg='#f0f0f0'
        )
        self.header_label.pack(pady=10)

        # Описание
        self.description_label = tk.Label(
            self.tab,
            text=(
                "Предположим, мы вернулись в старые времена. "
                "Кругом царит HTTP и Вам предстоит защитить свои данные."
            ),
            font=("Arial", 15),
            wraplength=800,
            justify="center",
            bg='#f0f0f0'
        )
        self.description_label.pack(pady=20)

        # Кнопка для начала квеста
        self.start_button = ttk.Button(self.tab, text="Поиск", command=self.start_quest)
        self.start_button.pack(pady=20)

        # Поле для отображения результатов квеста
        self.result_label = tk.Label(
            self.tab,
            text="",
            font=("Arial", 12),
            fg="green",
            bg='#f0f0f0'
        )
        self.result_label.pack(pady=20)

        # Кнопка для включения HTTPS
        self.lock_button = None
        self.step = 0  # Индикатор текущего этапа квеста
        self.hacker_computer = None  # Хакерский компьютер

    def start_quest(self):
        """Запуск квеста с очисткой предыдущих элементов."""
        # Очищаем экран от предыдущих элементов
        for widget in self.tab.winfo_children():
            widget.destroy()

        # Снова добавляем заголовок и описание
        self.header_label = tk.Label(
            self.tab,
            text="Почему важно использовать HTTPS?",
            font=("Arial", 16, "bold"),
            bg='#f0f0f0'
        )
        self.header_label.pack(pady=10)

        self.description_label = tk.Label(
            self.tab,
            text=(
                "Предположим, мы вернулись в старые времена. "
                "Кругом царит HTTP и Вам предстоит защитить свои данные."
            ),
            font=("Arial", 15),
            wraplength=800,
            justify="center",
            bg='#f0f0f0'
        )
        self.description_label.pack(pady=20)

        # Кнопка для начала квеста
        self.start_button = ttk.Button(self.tab, text="Поиск", command=self.start_quest)
        self.start_button.pack(pady=20)

        # Поле для отображения результатов квеста
        self.result_label = tk.Label(
            self.tab,
            text="",
            font=("Arial", 12),
            fg="green",
            bg='#f0f0f0'
        )
        self.result_label.pack(pady=20)

        # Переход к началу квеста
        self.result_label.config(text="Вам попался привлекательный форум, где проводите дни напролёт.", fg="blue", font=("Arial", 14))

        # Появление кнопки для активации первого шага
        self.create_lock_button("🔓 http://4chan", self.show_http_simulation)

    def create_lock_button(self, text, action):
        """Создание кнопки с замком для перехода к следующему шагу."""
        if self.lock_button:
            self.lock_button.destroy()  # Убираем старую кнопку, если она есть
        self.lock_button = tk.Button(self.tab, text=text, font=("Arial", 14), command=action, bg="green", fg="white")
        # Центрируем кнопку динамически в зависимости от размеров экрана
        x = (self.root.winfo_width() - self.lock_button.winfo_width()) // 2
        y = self.root.winfo_height() // 2
        self.lock_button.place(x=x, y=y)

    def type_writer_effect(self, text, label, delay=500, on_complete=None):
        """Анимация ввода текста, как будто кто-то печатает."""
        def write_char(i):
            if i < len(text):
                label.config(text=text[:i+1])
                self.tab.after(delay, write_char, i+1)
            elif on_complete:
                on_complete()  # Когда анимация завершена, вызываем callback

        write_char(0)

    def show_http_simulation(self):
        """Симуляция перехвата данных при HTTP."""
        # Убираем старую кнопку
        self.lock_button.destroy()

        # Шаг 1: Анимация ввода логина и пароля
        self.result_label.config(text="Вводим логин и пароль...\nЭто будет происходить через HTTP, который не защищает данные.", fg="blue")

        login_label = tk.Label(self.tab, text="Логин:", font=("Arial", 16), bg="#f0f0f0")
        login_label.pack(pady=10)

        login_entry = tk.Label(self.tab, text="", font=("Arial", 14), fg="green", bg="#f0f0f0")
        login_entry.pack(pady=10)

        password_label = tk.Label(self.tab, text="Пароль:", font=("Arial", 16), bg="#f0f0f0")
        password_label.pack(pady=10)

        password_entry = tk.Label(self.tab, text="", font=("Arial", 14), fg="green", bg="#f0f0f0")
        password_entry.pack(pady=10)

        # Анимация ввода
        self.type_writer_effect("КрутойТип527", login_entry, delay=350, on_complete=lambda: self.type_writer_effect("niktoNeUznaet", password_entry, delay=200, on_complete=self.remove_login_password_labels))

        # После того как логин и пароль введены
        self.tab.after(7000, self.show_file_exchange)

    def remove_login_password_labels(self):
        """Удаление лейблов логина и пароля после завершения ввода."""
        for widget in self.tab.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget("text") in ["Логин:", "Пароль:", "КрутойТип527", "niktoNeUznaet"]:
                widget.destroy()

    def show_file_exchange(self):
        """Симуляция обмена файлами между компьютерами."""
        self.result_label.config(text="На форуме Вы нашли друга и решили обменяться файлами.", fg="blue")

        # Два компьютера (размещаем их ниже текста)
        x1 = (self.root.winfo_width() - 100) // 2 - 150  # Динамическое расположение
        y1 = self.root.winfo_height() // 2 + 100  # Размещаем пониже
        computer1 = tk.Label(self.tab, text="💻", font=("Arial", 40), fg="purple", bg="#f0f0f0")
        computer1.place(x=x1, y=y1)

        x2 = (self.root.winfo_width() - 100) // 2 + 50  # Динамическое расположение
        y2 = self.root.winfo_height() // 2 + 100  # Размещаем пониже
        computer2 = tk.Label(self.tab, text="💻", font=("Arial", 40), fg="green", bg="#f0f0f0")
        computer2.place(x=x2, y=y2)

        # Симуляция обмена файлов
        file_transfer_label = tk.Label(self.tab, text="📂↔📂", font=("Arial", 50), fg="orange", bg="#f0f0f0")
        file_transfer_label.place(x=(self.root.winfo_width() - 350) // 2, y=y1 + 100)

        # После некоторой задержки, появится третий компьютер, который будет перехватывать данные
        self.tab.after(5000, self.show_attack)

    def show_attack(self):
        """Атака с третьего компьютера."""
        self.result_label.config(text="⚠️ О нет! Кто-то подменил маршруты передачи через некорректно защищенную сеть! ⚠️\nТеперь он может просматривать наш диалог!", fg="red")

        # Третий компьютер, перехватывающий данные
        self.hacker_computer = tk.Label(self.tab, text="👾", font=("Arial", 40), fg="red", bg="#f0f0f0")
        self.hacker_computer.place(x=(self.root.winfo_width() - 100) // 2 + 250, y=self.root.winfo_height() // 2 + 100)

        # Появляется кнопка для активации HTTPS
        self.create_lock_button("🔒 Активировать HTTPS", self.activate_https)

    def activate_https(self):
        """Активация HTTPS."""
        # Убираем хакера
        if self.hacker_computer:
            self.hacker_computer.destroy()

        self.result_label.config(
            text="HTTPS использует SSL/TLS для шифрования данных, чтобы их нельзя было перехватить.",
            fg="blue"
        )
        self.lock_button.destroy()

    def show_https_success(self):
        """После активации HTTPS показывается успешная защита."""
        self.result_label.config(
            text="Теперь ваши данные защищены с помощью HTTPS!",
            fg="green"
        )
        # Убираем кнопку
        self.lock_button.destroy()
