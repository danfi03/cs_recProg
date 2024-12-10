import tkinter as tk
from tkinter import ttk
from update_tab import UpdateTab  # Импортируем первую вкладку
from https_tab import HttpTab  # Импортируем вторую вкладку
from password_tab import PasswordTab  # Импортируем третью вкладку
from fishing_tab import FishingTab  # Вкладка "Фишинг"

# Основное окно
root = tk.Tk()
root.title("Безопасность в интернете")
root.geometry("1200x900")
root.configure(bg='#f0f0f0')  # Цвет фона

# Панель вкладок
notebook = ttk.Notebook(root)

# Создаем вкладки
update_tab = UpdateTab(notebook, root)  # Вкладка "Обновление ПО"
notebook.add(update_tab.tab, text="Обновление ПО")

https_tab = HttpTab(notebook, root)  # Вкладка "Использование HTTPS"
notebook.add(https_tab.tab, text="Использование HTTPS")

password_tab = PasswordTab(notebook, root)  # Вкладка "Менеджер паролей и 2FA"
notebook.add(password_tab.tab, text="Менеджер паролей и 2FA")

fishing_tab = FishingTab(notebook, root)  # Вкладка "Фишинг"
notebook.add(fishing_tab.tab, text="Фишинг")

# Запускаем приложение
notebook.pack(expand=True, fill="both")
root.mainloop()
