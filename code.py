import tkinter as tk
import random
import json

items = open("./items.json", encoding="utf8")
item_data = json.load(items)


class Hero:
    def __init__(self, name, health, balance, inventory, stats, maxhealth, speed, strength):
        self.name = name
        self.health = health
        self.balance = balance
        self.inventory = inventory
        self.stats = stats
        self.maxhealth = maxhealth
        self.speed = speed
        self.strength = strength

class Market:
    def __init__(self):
        pass

    def check(self, market_items):
        print(market_items)
    
    def buy(self, balance):
        item = input("What would you like to buy?")
        while (item != "exit") or (item != "end"):
            for i in item_data:
                if item == i["name"]:
                    try:
                        int(balance) - int(i["price"])
                    except int(i["price"]) > int(balance):
                        print("You cannot buy this item")
                    else:
                        int(balance) -= int(i["price"])
                        if item == "health potion":
                            Hero.health += 20
                        elif item == "speed potion":
                            Hero.speed +=20
                        elif item == "strength potion":
                            Hero.strength +=20
                        else:
                            Hero.inventory.append(item)
                            print(f"{i["name"]} was purchased!")
                            return balance
                else:
                    print("No item found.")
            item = input("What else would you like to buy?")

class Enemy:
    def __init__(self):
        pass
    
    def battle_hill(self, enemyname, enemyhealth, baseattack, enemyscore, enemyspeed, attackname, attackpower):
        print(f"An {enemyname} has spawned!""\n")
        print(f"Health:{enemyhealth}, Base Attack:{baseattack}")
        while (enemyhealth > 0) or (Hero.health > 0):
            enemy_attack_choose = random.randint(0,4)
            if Hero.speed >= enemyspeed:
                hero_choice = input("Select action")
                if hero_choice == "potion":
                    pass
                elif hero_choice == "defense":
                    pass
                elif hero_choice == "flee":
                    flee = random.randint(0,10)
                    if flee <= 1:
                        enemyscore = 0
                        break
                    pass
                elif hero_choice == "attack":
                    enemyhealth -= Hero.health
                    pass
                else:
                    pass
                if enemy_attack_choose == 4:
                    print(f"The {enemyname} uses the base attack.")
                    attackpower = baseattack
                    Hero.health -= attackpower
                elif enemy_attack_choose == 3:
                    enemyspeed += attackpower[enemy_attack_choose]
                else:
                    print(f"The {enemyname} uses {attackname[enemy_attack_choose]}.")
                    Hero.health -= attackpower[enemy_attack_choose]
            else:
                if enemy_attack_choose == 4:
                    print(f"The {enemyname} uses the base attack.")
                    attackpower = baseattack
                    Hero.health -= attackpower
                elif enemy_attack_choose == 3:
                    enemyspeed += attackpower[enemy_attack_choose]
                else:
                    print(f"The {enemyname} uses {attackname[enemy_attack_choose]}.")
                    Hero.health -= attackpower[enemy_attack_choose]
                hero_choice = input("Select action")
                if hero_choice == "potion":
                    pass
                elif hero_choice == "defense":
                    pass
                elif hero_choice == "flee":
                    flee = random.randint(0,10)
                    if flee <= 1:
                        enemyscore = 0
                        break
                    pass
                elif hero_choice == "attack":
                    pass
                else:
                    pass
        Enemy.death("Money")
        Hero.stats += enemyscore
        pass

    def death(self, loot):
        print(f"The {Enemy.battle_hill.enemyname} has been slained.")
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
        maxhealth = Hero.maxhealth
        if Hero.health < maxhealth:
            Hero.health += (maxhealth*0.05)
        if randomeventmodifier >= 90:
            if (randomeventmodifier <= 91) and (randomeventmodifier <= 94):
                Enemy.battle_hill("Goblin", 25, 5, 100, 25, ("Cut", "Treasure-Dive", "Lock", "Metronome"), (2, 6, 10, 5))
            elif randomeventmodifier == (95 or 96):
                Enemy.battle_hill("Vampire", 75, 10, 200, 40, ("Batwave", "Bite", "Bloodshear", "Floatation Dive"), (5, 10, 20, 5))
            elif randomeventmodifier == 97:
                Enemy.battle_hill("Witch", 150, 15, 500, 20, ("Staffswing", "Potions", "Blind Illusions", "Speed Potion"), (8, 15, 25, 10))
            elif randomeventmodifier == 98:
                Enemy.battle_hill("Regi", 500, 30, 2000, 20, ("Ice Shard", "Bulk Stomp", "Mirage Blast", "Weight Loss"), (15, 30, 50, 15))
            elif randomeventmodifier == 99:
                Enemy.battle_hill("Balrog", 1000, 100, 5000, 30, ("Fire Punch", "Rojogrund", "Hellblast", "Burnt Terrain"), (50, 100, 500, 20))
            elif randomeventmodifier == 100:
                Enemy.battle_hill("Garry Kasparov", 2851, 285, 28510, 10, ("Check", "1996", "Kasparov's Immortal", "Rapid"), (100, Hero.maxhealth*0.1, 913, 10))

charactername = input("Choose character name.""\n")

window = tk.Tk()
window.title("OOP Adventures") 
window.geometry("1200x800") 
window.resizable(False, False)

prompt = tk.Label(window, text="Character status",
font=("Calibri", 28))
prompt.pack(pady=20)

Elias = Hero(f"{charactername}", 100, 1000, ["Stone Sword", "Wooden Shield"], 0, 100, 50, 100)
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
