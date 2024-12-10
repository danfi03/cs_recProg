import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import threading
import time

# Уровень угроз
risks = {"Без обновлений": 100, "Q$*@%^E": 0, "С обновлениями": 0}
virus_labels = []

# Новый и расширенный список символов вирусов
virus_symbols = [
    "🦠", "💀", "⚠️", "👾", "🤖", "💻", "🧟", "☠️", "🦠", "🐍", "👻", "💣",
    "🧬", "🦠", "🔥", "🧪", "🧩", "💢", "⚡", "⚔️", "🌐", "🔒", "📡", "🛑",
    "🚨", "⚔️", "🔴", "🦠", "🧠", "🚨", "🌍", "⚠️", "🔑", "💥", "💻", "🖥️",
    "⚡", "🕷️", "🧫", "🧬", "🦠", "🧪", "🚨", "💻", "🌐", "🧠", "💡", "🧊",
    "⚙️", "🦾", "💀", "⚡", "📲", "🔍", "🌪️"
]


class UpdateTab:
    def __init__(self, parent, root_window):
        self.tab = ttk.Frame(parent)
        self.root = root_window  # Сохраняем ссылку на root

        self.label = tk.Label(self.tab, text="Обновления крайне важны!", font=("Arial", 16))
        self.label.pack(pady=10)

        self.description_label = tk.Label(
            self.tab,
            text=(
                "Исследования показывают, что 70-90% атак происходят из-за известных уязвимостей, которые могли быть устранены с помощью обновлений.\n\n"
                "Источник: Verizon Data Breach Investigations Report 2020,\nCVE (Common Vulnerabilities and Exposures) и исследования безопасности от Microsoft и Google"
            ),
            font=("Arial", 14),
            wraplength=800,
            justify="center",
            bg='#f0f0f0',
            fg="blue"
        )
        self.description_label.pack(pady=20)

        # Создаем стиль для Checkbutton
        self.style = ttk.Style()
        self.style.configure("TCheckbutton", font=("Arial", 12), background='#f0f0f0')

        # Переключатель автоматических обновлений
        self.auto_update_var = tk.BooleanVar(value=False)
        self.auto_update_check = ttk.Checkbutton(
            self.tab, text="Включить автоматические обновления", variable=self.auto_update_var,
            style="TCheckbutton"
        )
        self.auto_update_check.pack(pady=10)

        # Кнопка обновления
        self.update_button = ttk.Button(self.tab, text="Запустить обновление ПО", command=self.update_software,
                                        width=25, )
        self.update_button.pack(pady=20)

        # Прогресс-бар
        self.progress = ttk.Progressbar(self.tab, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        self.info_label = tk.Label(self.tab, text="", font=("Arial", 12), bg='#f0f0f0')
        self.info_label.pack(pady=20)

        # График
        self.graph_frame = tk.Frame(self.tab, bg='#f0f0f0')
        self.graph_frame.pack(pady=10)

        # Показать начальные вирусы и график
        self.update_virus_labels()
        self.show_update_statistics()

    def update_software(self):
        """Симуляция обновления ПО."""
        if not self.auto_update_var.get():
            self.info_label.config(text="Пожалуйста, включите автоматические обновления!", fg="red")
            return

        self.progress['value'] = 0
        self.info_label.config(text="Процесс обновления запущен...", fg="black")

        def process():
            for i in range(101):
                time.sleep(0.03)
                self.progress['value'] = i
                self.root.update_idletasks()

            # Обновление данных и графика
            risks["Без обновлений"] = 100
            risks["С обновлениями"] = 20
            self.update_virus_labels()
            self.show_update_statistics()
            self.info_label.config(text="Обновление завершено! Все угрозы устранены.", fg="green")

        threading.Thread(target=process).start()

    def update_virus_labels(self):
        """Обновить отображение вирусов."""
        # Удаляем старые вирусы
        for label in virus_labels:
            label.destroy()
        virus_labels.clear()

        if risks["С обновлениями"] > 0:  # После обновления вирусы исчезают
            return

        # Показать вирусы до обновления
        virus_count = 50  # Увеличено количество вирусов
        available_virus_symbols = virus_symbols.copy()

        for _ in range(virus_count):
            if available_virus_symbols:  # Пока есть вирусы в списке, случайным образом выбираем
                virus_symbol = random.choice(available_virus_symbols)
                available_virus_symbols.remove(virus_symbol)  # Убираем символ из списка, чтобы не повторялся
            else:
                break  # Если символы закончились, останавливаем создание вирусов

            virus = tk.Label(self.tab, text=virus_symbol, font=("Arial", 18), fg="white", bg="black")

            # Обновление размеров окна, чтобы убедиться, что они правильно инициализированы
            self.root.update_idletasks()
            window_width = self.root.winfo_width()
            window_height = self.root.winfo_height()

            # Позиция по X и Y, ограниченная размерами окна
            x = random.randint(50, window_width - 50)
            y = random.randint(150, window_height - 150)
            virus.place(x=x, y=y)
            virus_labels.append(virus)

        # Запустить анимацию для перемещения вирусов
        self.move_viruses()

    def move_viruses(self):
        """Анимация перемещения вирусов."""
        for virus in virus_labels:
            # Получаем случайные новые позиции в пределах всего окна
            window_width = self.root.winfo_width()
            window_height = self.root.winfo_height()
            new_x = random.randint(50, window_width - 50)
            new_y = random.randint(150, window_height - 150)
            virus.place(x=new_x, y=new_y)

        if risks["С обновлениями"] == 0:  # Если обновление не завершено, обновляем позицию каждую секунду
            self.root.after(1000, self.move_viruses)  # Через 1000 миллисекунд (1 секунда) снова меняем позицию

    def show_update_statistics(self):
        """Обновить график угроз."""
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        # График с двумя столбцами: "Без обновлений" и "С обновлениями"
        ax.bar(["Без обновлений", "С обновлениями"], [risks["Без обновлений"], risks["С обновлениями"]],
               color=["red", "green"])

        ax.set_title("Угрозы", fontsize=14)
        ax.set_ylabel("Риск (%)", fontsize=12)

        # Обновить график на экране
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
