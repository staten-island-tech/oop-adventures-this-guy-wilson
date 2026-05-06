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

class Enemy:
    def __init__(self, name, strength, health, attack):
        self.name = name
        self.strength = strength
        self.health = health
        self.attack = attack
    
    def death(self, loot):
        print(f"The {Enemy.name} has been slained.")
        print(f"{loot}""\n")
        heroinventoryamount = len(Hero.inventory)
        if heroinventoryamount <= 5:
            while lootchoose not in loot:
                lootchoose = input("Choose an item")
                if lootchoose in loot:
                    Hero.inventory.append(lootchoose)
                else:
                    print("Invalid")
        else:
            print("Max inventory.")
        return

class Event:
    def __init__(self):
        pass

    def random_event_modifier(self):
        randomeventmodifier = random.randint(0,100)
        if randomeventmodifier < 80:
            pass

Elias = Hero("Elias", 100, 1000, ["Stone Sword", "Wooden Shield"], 0)
The_Market = Market()

window = tk.Tk()
window.title("OOP Adventures") 
window.geometry("1200x800") 
window.resizable(False, False)

prompt = tk.Label(window, text="Type your message below:",
font=("Calibri", 28))
prompt.pack(pady=20)

healthstatus = tk.Label(window, text=f"{Elias.health}/100", font=("Calibri", 20))
healthstatus.pack(pady=20)
healthstatus.place(x=600, y=600)

entry = tk.Entry(window, font=("Calibri", 28), width=50)
entry.pack(pady=10)


result_label = tk.Label(window, text="", font=("Calibri", 28, "bold"),
fg="blue")
result_label.pack(pady=30)


window.mainloop()

while Elias.health <= 0:
    pass
print(Elias.stats)