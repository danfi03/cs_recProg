import tkinter as tk
from tkinter import messagebox
import random
import string
import re


class PasswordTab:
    def __init__(self, parent, root):
        self.tab = tk.Frame(parent)
        self.root = root

        self.label = tk.Label(self.tab, text="Добро пожаловать в Менеджер паролей и 2FA!", font=("Arial", 16))
        self.label.pack(pady=10)

        # Секция для создания паролей
        self.generate_button = tk.Button(self.tab, text="Сгенерировать пароль", command=self.generate_password, font=("Arial", 12))
        self.generate_button.pack()

        self.password_display = tk.Label(self.tab, text="", font=("Arial", 14))
        self.password_display.pack(pady=5)

        self.generated_password_strength = tk.Label(self.tab, text="Сложность сгенерированного пароля: ")
        self.generated_password_strength.pack()

        # Секция для проверки паролей
        self.check_password_label = tk.Label(self.tab, text="Проверьте ваш пароль:")
        self.check_password_label.pack(pady=10)

        self.check_password_entry = tk.Entry(self.tab, font=("Arial", 14))
        self.check_password_entry.pack()

        self.check_password_button = tk.Button(self.tab, text="Проверить пароль", command=self.check_password)
        self.check_password_button.pack(pady=5)

        self.check_password_result = tk.Label(self.tab, text="Сложность введенного пароля: ", font=("Arial", 14))
        self.check_password_result.pack()

        # Секция для двухфакторной аутентификации
        self.two_fa_label = tk.Label(self.tab, text="Двухфакторная аутентификация (2FA)", font=("Arial", 16))
        self.two_fa_label.pack(pady=20)

        self.two_fa_button = tk.Button(self.tab, text="Активировать 2FA", command=self.activate_2fa)
        self.two_fa_button.pack(pady=10)

        self.two_fa_result = tk.Label(self.tab, text="", font=("Arial", 14))
        self.two_fa_result.pack()

        self.phone_canvas = None
        self.message_label = None
        self.two_fa_entry = None
        self.two_fa_verify_button = None

    def generate_password(self):
        """Генерация случайного пароля"""
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
        self.password_display.config(text=password)
        self.update_strength(password, self.generated_password_strength)

    def check_password(self):
        """Проверка введенного пароля на сложность"""
        password = self.check_password_entry.get()
        if password:
            self.update_strength(password, self.check_password_result)
        else:
            self.check_password_result.config(text="Пожалуйста, введите пароль для проверки.", fg="red")

    def update_strength(self, password, label):
        """Оценка сложности пароля"""
        length = len(password)
        has_upper = bool(re.search(r'[A-Z]', password))
        has_lower = bool(re.search(r'[a-z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        common_patterns = ["12345", "password", "qwerty", "letmein", "11111"]

        is_common = any(pattern in password.lower() for pattern in common_patterns)

        if is_common:
            strength = "Очень слабый"
            color = "red"
        elif length >= 12 and has_upper and has_lower and has_digit and has_special:
            strength = "Сильный"
            color = "green"
        elif length >= 8 and ((has_upper and has_lower) or (has_digit and has_special)):
            strength = "Средний"
            color = "orange"
        else:
            strength = "Слабый"
            color = "red"

        label.config(text=f"Сложность пароля: {strength}", fg=color, font=("Arial", 12))

    def activate_2fa(self):
        """Имитация активации двухфакторной аутентификации"""
        self.two_fa_result.config(text="2FA активирована. Ожидание кода на телефон...", fg="blue")
        self.two_fa_button.config(state="disabled")

        if self.phone_canvas:
            self.phone_canvas.destroy()

        # Создаем компактный телефон
        self.phone_canvas = tk.Canvas(self.tab, width=100, height=200, bg="black", highlightthickness=0)
        self.phone_canvas.pack(pady=20)

        # Корпус телефона
        self.phone_canvas.create_rectangle(5, 5, 95, 195, outline="#555", fill="#333", width=2)
        self.phone_canvas.create_rectangle(10, 20, 90, 180, fill="#ddd", outline="black")  # Экран
        self.phone_canvas.create_oval(45, 10, 55, 15, fill="gray")  # Динамик

        # Кнопка на экране
        self.phone_canvas.create_rectangle(40, 170, 60, 175, fill="gray", outline="black")

        self.root.after(1000, self.animate_message)

    def animate_message(self):
        """Анимация получения сообщения на телефон"""
        if self.message_label:
            self.message_label.destroy()

        code = random.randint(100000, 999999)
        code_str = str(code)

        self.message_label = self.phone_canvas.create_text(
            50, 100, text="", font=("Arial", 10), fill="blue"
        )

        def type_message(index=0):
            if index < len(code_str):
                current_text = self.phone_canvas.itemcget(self.message_label, "text")
                self.phone_canvas.itemconfig(self.message_label, text=current_text + code_str[index])
                self.root.after(300, type_message, index + 1)
            else:
                self.prepare_2fa_verification(code)

        type_message()

    def prepare_2fa_verification(self, code):
        """Подготовка ввода кода"""
        if self.two_fa_entry:
            self.two_fa_entry.destroy()
        if self.two_fa_verify_button:
            self.two_fa_verify_button.destroy()

        self.two_fa_entry = tk.Entry(self.tab, font=("Arial", 14))
        self.two_fa_entry.pack(pady=5)

        self.two_fa_verify_button = tk.Button(
            self.tab, text="Подтвердить", command=lambda: self.verify_2fa_code(code)
        )
        self.two_fa_verify_button.pack(pady=5)

    def verify_2fa_code(self, correct_code):
        """Проверка правильности введенного кода 2FA"""
        entered_code = self.two_fa_entry.get()
        if entered_code == str(correct_code):
            self.two_fa_result.config(text="Код верный! Доступ разрешен.", fg="green")
            self.phone_canvas.delete(self.message_label)  # Удаляем текст сообщения
            self.two_fa_entry.destroy()
            self.two_fa_verify_button.destroy()
        else:
            self.two_fa_result.config(text="Неверный код! Попробуйте снова.", fg="red")

