import tkinter as tk
import random

class Hero:
    def __init__(self, name, health, balance, inventory, stats):
        self.name = name
        self.healh = health
        self.balance = balance

        
window = tk.Tk()
window.title("OOP Adventures") 
window.geometry("400x250") 
window.resizable(False, False)

prompt = tk.Label(window, text="Type your message below:",
font=("Calibri", 14))
prompt.pack(pady=10)

entry = tk.Entry(window, font=("Calibri", 14), width=30)
entry.pack(pady=5)


result_label = tk.Label(window, text="", font=("Calibri", 14, "bold"),
fg="blue")
result_label.pack(pady=15)


window.mainloop()