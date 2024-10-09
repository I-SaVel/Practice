import subprocess
from tkinter import *
import sys
import os
from threading import Timer
from tkinter import messagebox


def create_window():
    window = Tk()
    window.title("Test")
    label = Label(window, text="v0.1")
    label.pack(pady=20)
    update_button = Button(window, text="Update",command=update_from_github)
    update_button.pack(pady=20)


    window.mainloop()


def update_from_github():
    try:
        subprocess.run(["git", "fetch"], check=True)
        result = subprocess.run(["git", "diff", "origin/main"], capture_output=True, text=True)
        if result.stdout:
            subprocess.run(["git", "pull"], check=True)
            messagebox.showinfo("Обновление", "Приложение обновлено с GitHub.")
            restart_program()
        else:
            print("Нет новых изменений.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Ошибка", f"Ошибка при обновлении: {e}")
    Timer(10, update_from_github).start()

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


if __name__ == "__main__":
    create_window()