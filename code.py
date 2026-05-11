import tkinter as tk
import random

class Hero:
    def __init__(self, name, health, balance, inventory, stats, maxhealth):
        self.name = name
        self.health = health
        self.balance = balance
        self.inventory = inventory
        self.stats = stats
        self.maxhealth = maxhealth

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
                    else:
                        Hero.inventory.append(item)
                        return balance
            else:
                print("No item found.")
            item = input("What would you like to buy?")

class Enemy:
    def __init__(self, name, strength, health, attack, score):
        self.score = score
        self.name = name
        self.strength = strength
        self.health = health
        self.attack = attack
    
    def battle_hill(self, enemyname, enemyhealth, enemyattack, enemyscore):
        print(f"An {enemyname} has spawned!""\n")
        print(f"Health:{enemyhealth}, Base Attack:{enemyattack}")
        Enemy.death("Money")
        Hero.stats += enemyscore
        pass

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

    def random_event_modifier(self, maxhealth):
        randomeventmodifier = random.randint(0,100)
        if Hero.health < maxhealth:
            Hero.health += (maxhealth*0.05)
        if randomeventmodifier >= 90:
            if (randomeventmodifier <= 91) and (randomeventmodifier <= 95):
                Enemy.battle_hill("Goblin", 25, 2, 100)
            elif randomeventmodifier == 96:
                Enemy.battle_hill("Vampire", 50, 5, 200)
            elif randomeventmodifier == 97:
                Enemy.battle_hill("Witch", 150, 15, 500)
            elif randomeventmodifier == 98:
                Enemy.battle_hill("Regi", 500, 50, 2000)
            elif randomeventmodifier == 99:
                Enemy.battle_hill("Balrog", 1000, 100, 5000)
            elif randomeventmodifier == 100:
                Enemy.battle_hill("Garry Kasparov", 2851, 285, 28510)
        

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
    "department": "animal",},

    {"name": "human hand",
    "price": 100000,
    "department": "human",},

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

prompt = tk.Label(window, text="Character status",
font=("Calibri", 28))
prompt.pack(pady=20)

Elias = Hero(f"{charactername}", 100, 1000, ["Stone Sword", "Wooden Shield"], 0, 100)
The_Market = Market()

windowname = tk.Label(window, text=f"{Elias.name}", font=("Calibri", 30))
windowname.pack(pady=20)
windowname.place(x=200, y= 600)

healthstatus = tk.Label(window, text=f"{Elias.health}/{Elias.maxhealth}", font=("Calibri", 30))
healthstatus.pack(pady=20)
healthstatus.place(x=600, y=600)

while Elias.health <= 0:
    pass
print(Elias.name, "has died! Your final score is", Elias.stats)

window.mainloop()
