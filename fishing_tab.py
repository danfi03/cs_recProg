import tkinter as tk


class FishingTab:
    def __init__(self, parent, root):
        self.tab = tk.Frame(parent)
        self.root = root

        # Канвас для рисования элементов
        self.canvas = tk.Canvas(self.tab, width=1000, height=700, bg='#f0f0f0')
        self.canvas.pack(fill="both", expand=True)

        # Заголовок с URL (как на фишинговом сайте)
        self.url_label = self.canvas.create_text(500, 30, text="https://secure.mysecurebank.com", font=("Arial", 14),
                                                 fill="green")

        # Рисуем поля ввода с правильными размерами
        self.username_rect = self.canvas.create_rectangle(300, 100, 700, 150, outline="black", width=2)
        self.username_label = self.canvas.create_text(150, 125, text="Имя пользователя:", anchor="w",
                                                      font=("Arial", 12))

        self.password_rect = self.canvas.create_rectangle(300, 200, 700, 250, outline="black", width=2)
        self.password_label = self.canvas.create_text(150, 225, text="Пароль:", anchor="w", font=("Arial", 12))

        # Кнопка "Отправить"
        self.submit_button = self.canvas.create_rectangle(400, 270, 600, 320, fill="#4CAF50", outline="black")
        self.submit_button_text = self.canvas.create_text(500, 295, text="Отправить", font=("Arial", 12), fill="white")
        self.canvas.tag_bind(self.submit_button, "<Button-1>", self.submit_data)

        # Кнопка для проверки сертификата
        self.check_button = self.canvas.create_rectangle(400, 340, 600, 390, fill="#2196F3", outline="black")
        self.check_button_text = self.canvas.create_text(500, 365, text="Проверить сертификат", font=("Arial", 12),
                                                         fill="white")
        self.canvas.tag_bind(self.check_button, "<Button-1>", self.check_certificate)

        # Место для отображения статуса сертификата
        self.cert_status_label = self.canvas.create_text(500, 470, text="", font=("Arial", 12), fill="red")

        # Место для сообщения о безопасности
        self.security_status_label = self.canvas.create_text(500, 500, text="", font=("Arial", 14), fill="red")

        # Интерактивные поля ввода с привязкой
        self.username_entry = tk.Entry(self.tab, font=("Arial", 12))
        self.password_entry = tk.Entry(self.tab, font=("Arial", 12), show="*")  # Показывать звездочки для пароля

        # Добавление полей ввода в канву с правильными размерами
        self.username_window = self.canvas.create_window(500, 125, window=self.username_entry, width=380, height=25)
        self.password_window = self.canvas.create_window(500, 225, window=self.password_entry, width=380, height=25)

        # Интерактивность: возможность ввода данных
        self.username_entry.bind("<FocusIn>", self.focus_username)
        self.password_entry.bind("<FocusIn>", self.focus_password)

        # Отслеживание изменения размера окна
        self.root.bind("<Configure>", self.resize)

    def focus_username(self, event):
        """Фокус на поле имени пользователя для ввода данных"""
        self.username_entry.config(fg="black")

    def focus_password(self, event):
        """Фокус на поле пароля для ввода данных"""
        self.password_entry.config(fg="black")

    def submit_data(self, event):
        """Имитация отправки данных на фишинговый сайт"""
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Если поля не пустые
        if username and password:
            # Запускаем анимацию отправки данных
            self.animate_sending_data()

    def animate_sending_data(self):
        """Анимация отправки данных на фишинговый сайт"""
        self.canvas.itemconfig(self.url_label, text="https://secure.mysecurebank.com (Отправка данных...)", fill="blue")

        # Анимация "Отправка данных"
        data_sending_text = self.canvas.create_text(850, 300, text="📂", font=("Arial", 52),
                                                    fill="orange")

        # Перемещение текста "Отправка данных..."
        for i in range(50):
            self.canvas.move(data_sending_text, 5, 0)  # Двигаем текст вправо
            self.canvas.after(30)  # Пауза для анимации
            self.root.update()

        # После анимации данные отправлены
        self.canvas.delete(data_sending_text)  # Удаляем анимацию текста
        self.canvas.itemconfig(self.url_label, text="https://secure.mysecurebank.com (Повторите попытку позже...)", fill="red")

    def check_certificate(self, event):

        # Имитация появления формы с данными сертификата
        self.root.after(1000, self.display_certificate_form)

    def display_certificate_form(self):
        """Отображаем фальшивую форму сертификата с более детализированной информацией"""
        # Поднимаем сертификат выше
        self.canvas.create_rectangle(100, 420, 650, 800, outline="black", width=2)  # Рамка формы
        self.canvas.create_text(380, 460, text="Детали сертификата SSL", font=("Arial", 14, "bold"), fill="black")

        # Добавляем более правдоподобные фальшивые данные о сертификате
        self.canvas.create_text(150, 500, text="Имя владельца:\t\tTrustedBank", font=("Arial", 12), fill="black",
                                anchor="w")
        self.canvas.create_text(150, 520, text="Тип сертификата:\t\tEV SSL (Extended Validation)", font=("Arial", 12),
                                fill="black", anchor="w")
        self.canvas.create_text(150, 540, text="Дата истечения:\t\t07 Января 2030", font=("Arial", 12), fill="black",
                                anchor="w")
        self.canvas.create_text(150, 560, text="Сертификат выдан:\tGlobal CA", font=("Arial", 12), fill="black",
                                anchor="w")

        # Более правдоподобные детали сертификата, скрывая явные признаки фишинга
        self.canvas.create_text(150, 580, text="Серийный номер:\t\t7684-6347-8921-0429", font=("Arial", 12),
                                fill="black", anchor="w")
        self.canvas.create_text(150, 600, text="Подписывающий орган:\tTrusted Certificate Authority",
                                font=("Arial", 12), fill="black", anchor="w")
        self.canvas.create_text(150, 620, text="Алгоритм подписи:\t\tSHA256", font=("Arial", 12), fill="black",
                                anchor="w")
        self.canvas.create_text(150, 640, text="Статус:\t\t\tПодтвержден", font=("Arial", 12), fill="green",
                                anchor="w")

        # Добавляем еще подробностей о сертификате
        self.canvas.create_text(150, 660, text="Срок действия:\t\tс 07 Декабря 2024", font=("Arial", 12),
                                fill="black", anchor="w")
        self.canvas.create_text(150, 680, text="Ключи:\t\t\tRSA 2048", font=("Arial", 12), fill="black",
                                anchor="w")
        self.canvas.create_text(150, 700, text="Сертификат содержит расширенные атрибуты", font=("Arial", 12),
                                fill="black", anchor="w")
        self.canvas.create_text(150, 720, text="Протокол безопасности:\tTLS 1.2", font=("Arial", 12), fill="black",
                                anchor="w")
        self.canvas.create_text(150, 740, text="Адрес:\t\t\thttps://secure.mysecurebank.com",
                                font=("Arial", 12), fill="black", anchor="w")
        self.canvas.create_text(150, 760, text="Подтвержден на уровне:\tДоменное имя и организация", font=("Arial", 12),
                                fill="black", anchor="w")

    def resize(self, event):
        """Обновляем положение полей ввода при изменении размера окна"""
        self.canvas.coords(self.username_window, 500, 125)
        self.canvas.coords(self.password_window, 500, 225)

        # Обновляем расположение кнопок и статусов
        self.canvas.coords(self.submit_button, 400, 270, 600, 320)
        self.canvas.coords(self.check_button, 400, 340, 600, 390)
        self.canvas.coords(self.cert_status_label, 500, 470)
        self.canvas.coords(self.security_status_label, 500, 500)


# Пример использования
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Фишинговая страница")
    root.geometry("1000x700")

    notebook = tk.Notebook(root)
    fishing_tab = FishingTab(notebook, root)
    notebook.add(fishing_tab.tab, text="Фишинг")

    notebook.pack(expand=True, fill="both")
    root.mainloop()
