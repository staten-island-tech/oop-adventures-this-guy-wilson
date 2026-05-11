import tkinter as tk
import random

class Hero:
    def __init__(self, name, health, speed, strength, balance, inventory, stats):
        self.name = name
        self.health = health
        self.balance = balance
        self.inventory = inventory
        self.speed = speed
        self.strength=strength
        self.stats = stats
        

class Market:
    def __init__(self):
        pass

    def check(self, market_items):
        print(market_items)
    
    def buy(self, balance, cost, item, items):
        item = input("What would you like to buy?")
        while item != "exit":
            if item in items:
                try:
                    int(balance) - int(cost)
                except int(cost) > int(balance):
                    print("You cannot buy this item")
                else:
                    if item == "health potion":
                        Hero.health += 20
                    elif item == "speed potion":
                        Hero.speed +=20
                    elif item == "strength potion":
                        Hero.strength +=20
                       
                        Hero.inventory.append(item)
                        return balance
            else:
                print("No item found.")
            item = input("What would you like to buy?")

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

store = [
    {"name": "wooden armour",
    "price": 10,
    "department": "defense",},
    
    {"name": "steel armour",
    "price": 50,
    "department": "defense",},
    
    {"name": "diamond armour",
    "price": 100,
    "department": "defense"},

    {"name": "wooden sword",
    "price": 10,
    "department": "offense",},

    {"name": " steel sword",
    "price": 50,
    "department": "offense",},

    {"name": "diamond sword",
    "price": 100,
    "department": "offense"},

    {"name": "cat",
    "price": 100000,
    "department": "test subjects",},

    {"name": "human hand",
    "price": 100000000,
    "department": "test subjects",},

    {"name": "pickle",
    "price": 10,
    "department": "food"},

    {"name": "health potion",
    "price": 150,
    "department": "potion",},

    {"name": "strength potion",
    "price": 150,
    "department": "potion",},

    {"name": "speed potion",
    "price": 150,
    "department": "potion"}
]

charactername = input("Choose character name.""\n")

window = tk.Tk()
window.title("OOP Adventures") 
window.geometry("1200x800") 
window.resizable(False, False)

prompt = tk.Label(window, text="Type your message below:",
font=("Calibri", 28))
prompt.pack(pady=20)
entry = tk.Entry(window, font=("Calibri", 28), width=50)
entry.pack(pady=10)

Elias = Hero(f"{charactername}", 100, 100, 100, 1000, ["wooden sword", "Wooden Shield"], 0)
The_Market = Market()

windowname = tk.Label(window, text=f"{Elias.name}", font=("Calibri", 30))
windowname.pack(pady=20)
windowname.place(x=200, y= 590)

healthstatus = tk.Label(window, text=f"{Elias.health}/100", font=("Calibri", 20))
healthstatus.pack(pady=20)
healthstatus.place(x=600, y=600)

while Elias.health <= 0:
    pass
print(Elias.name, "has died! Your final score is", Elias.stats)

window.mainloop()
