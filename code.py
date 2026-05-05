import tkinter as tk
import random

class Hero:
    def __init__(self, name, health, balance, inventory, stats):
        self.name = name
        self.health = health
        self.balance = balance
        self.inventory = inventory
        self.stats = stats

window = tk.Tk()
window.title("OOP Adventures") 
window.geometry("1200x800") 
window.resizable(False, False)

prompt = tk.Label(window, text="Type your message below:",
font=("Calibri", 28))
prompt.pack(pady=20)

entry = tk.Entry(window, font=("Calibri", 28), width=60)
entry.pack(pady=10)


result_label = tk.Label(window, text="", font=("Calibri", 28, "bold"),
fg="blue")
result_label.pack(pady=30)


window.mainloop()