import tkinter as tk
import random

class Hero:
    def __init__(self, name, health, balance, inventory, stats):
        self.name = name
        self.health = health
        self.balance = balance
        self.inventory = inventory
        self.stats = stats

class Market:
    def __init__(self):
        pass

    def buy(self, balance, cost, item):
        try:
            int(balance) - int(cost)
        except int(cost) > int(balance):
            print("You cannot buy this item")
        else:
            Hero.inventory.append(item)
            return balance
class Event:
    def __init__(self):
        pass

    def random_event_modifier(self):
        randomeventmodifier = random.randint(0,100)
        if randomeventmodifier < 80:
            pass

Elias = Hero("Elias", 100, 1000, ["Stone Sword", "Wooden Shield"], 10, 0)
The_Market = Market()

window = tk.Tk()
window.title("OOP Adventures") 
window.geometry("1200x800") 
window.resizable(False, False)

prompt = tk.Label(window, text="Type your message below:",
font=("Calibri", 28))
prompt.pack(pady=20)

entry = tk.Entry(window, font=("Calibri", 28), width=50)
entry.pack(pady=10)


result_label = tk.Label(window, text="", font=("Calibri", 28, "bold"),
fg="blue")
result_label.pack(pady=30)


window.mainloop()