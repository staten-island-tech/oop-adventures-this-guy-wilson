import tkinter as tk
import random
import json

items = open("./items.json", encoding="utf8")
item_data = json.load(items)

defense = 0

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

class Item:
    def __init__(self):
        pass

class Market:
    def __init__(self):
        pass

    def buy(self):
        item = input("What would you like to do in the Market?""\n")
        while item not in ("exit","end"):
            if item == "check":
                self.check(item_data)
            elif item == "inventory":
                print("Inventory:", Elias.inventory)
            elif item == "buy":
                self.cashier(Elias.balance)
            
            item = input("What would you like to do in the Market?""\n")

    def check(self, market_items):
        for e in market_items:
            print(e["name"])

    def cashier(self, balance):
        sonion = input("What do you want to buy?")
        for i in item_data:
            if sonion == i["name"]:
                print(f"Item Price: {int(i['price'])}\nYour balance: {balance}\n")
                if int(i["price"]) > int(balance):
                    print("You cannot buy this item""\n")
                else:
                    if len(Elias.inventory) < 5:
                        balance -= int(i["price"])
                        if sonion == "health potion":
                            Elias.health += 50
                            if Elias.health > Elias.maxhealth:
                                Elias.health = Elias.maxhealth
                        elif sonion == "speed potion":
                            Elias.speed += 20
                        elif sonion == "strength potion":
                            Elias.strength += 20
                        elif sonion == "boost potion":
                            Elias.maxhealth += 50
                        else:
                            Elias.inventory.append(sonion)
                            print(f"{i['name']} was purchased!""\n")
                            Elias.balance = balance
                    else:
                        print("You have too much items in your inventory.")

4
class Enemy:
    def __init__(self):
        pass
    
    def enemy_attack(self, name, baseattack, speed, attackname, power):
        global defense
        enemy_attack_choose = random.randint(0,4)
        if enemy_attack_choose == 4:
            print(f"The {name} uses the base attack.")
            power = baseattack
            defense -= power
            if defense <= 0:
                Elias.health += defense
                defense = 0
            else:
                print("Successful defense.")
        elif enemy_attack_choose == 3:
            speed += power[enemy_attack_choose]
        else:
            print(f"The {name} uses {attackname[enemy_attack_choose]}.")
            defense -= power[enemy_attack_choose]
            if defense <= 0:
                Elias.health += defense
                defense = 0
            else:
                print("Congratulations!")
    
    def hero_attack(self, enemyscore, enemyhealth):
        global defense
        hero_choice = int(input("Select action"))
        print("Select options\n""[1] - Attack\n""[2] - Inventory\n""[3] - Defend\n""[4] - Flee\n")
        if hero_choice == 3:
            defense += 20
        elif hero_choice == 4:
            flee = random.randint(0,10)
            if flee <= 1:
                enemyscore = 0
                enemyhealth = 0
            else:
                print("You failed to flee!")
        elif hero_choice == 1:
            enemyhealth -= Elias.strength
        elif hero_choice == 2:
            print(Elias.inventory)
            item_usage = input("What item do you want to use?")
            item_found = False
            if item_usage in Elias.inventory:
                for item in item_data:
                    if item["name"] == item_usage:
                        if item["department"] == "defense":
                            Elias.health += int(item["price"])
                            if Elias.health > Elias.maxhealth:
                                Elias.health = Elias.maxhealth
                        elif item["department"] == "offense":
                            Elias.strength += int(item["price"])
                        elif item["department"] == "attack":
                            Elias.speed += int(item["price"])
                        Elias.inventory.remove(item_usage)
                        print(f"{item_usage} was used!")
                        item_found = True
                        break
            if not item_found:
                print("You don't have this item in your inventory.")
                    
        return enemyscore, enemyhealth

    def battle_hill(self, enemyname, enemyhealth, baseattack, enemyscore, enemyspeed, attackname, attackpower):
        print(f"An {enemyname} has spawned!""\n")
        print(f"Health:{enemyhealth}, Base Attack:{baseattack}")
        while (enemyhealth > 0) and (Elias.health > 0):            
            if Elias.speed >= enemyspeed:
                enemyscore, enemyhealth = Neuabgrund.hero_attack(enemyscore, enemyhealth)
                Neuabgrund.enemy_attack(enemyname, baseattack, enemyspeed, attackname, attackpower)
            else:
                Neuabgrund.enemy_attack(enemyname, baseattack, enemyspeed, attackname, attackpower)
                enemyscore, enemyhealth = Neuabgrund.hero_attack(enemyscore, enemyhealth)
            
            print(f"Your health:{Elias.health}")
            print(f"Enemy health:{enemyhealth}")
        4

        if enemyhealth <= 0:
            Neuabgrund.death("Money", enemyname)
            Elias.stats += enemyscore
            Elias.balance += enemyscore
            print(f"Your balance and score has increased by {enemyscore}!")

    def death(self, loot, name):
        print("The",name,"has been slained.")
        print(f"{loot}""\n")
        weapon_drop = random.choice(["wooden sword", "iron sword", "steel sword", "diamond sword"])
        if len(Elias.inventory) <= 5:
            Elias.inventory.append(weapon_drop)
            print(f"The {name} dropped a {weapon_drop}!")
        else:
            print("Your inventory is full, you cannot pick up the dropped item.")

        Elias.strength = round(Elias.strength*1.1, 2)

    
class Event:
    def __init__(self):
        pass

    def random_event_modifier(self, randomeventmodifier):
        if randomeventmodifier >= 900:
            if (randomeventmodifier >= 900) and (randomeventmodifier <= 949):
                Neuabgrund.battle_hill("Goblin", 25, 5, 100, 25, ("Cut", "Treasure-Dive", "Lock", "Metronome"), (2, 6, 10, 5))
            elif (randomeventmodifier >= 950) and (randomeventmodifier <= 974):
                Neuabgrund.battle_hill("Vampire", 75, 10, 200, 40, ("Batwave", "Bite", "Bloodshear", "Floatation Dive"), (5, 10, 20, 5))
            elif (randomeventmodifier >= 975) and (randomeventmodifier <= 991):
                Neuabgrund.battle_hill("Witch", 150, 15, 500, 20, ("Staffswing", "Potions", "Blind Illusions", "Speed Potion"), (8, 15, 25, 10))
            elif (randomeventmodifier >= 992) and (randomeventmodifier <= 997):
                Neuabgrund  .battle_hill("Regi", 550, 50, 2000, 20, ("Ice Shard", "Bulk Stomp", "Mirage Blast", "Weight Loss"), (15, 30, 50, 15))
            elif randomeventmodifier >= 998 and randomeventmodifier <= 999:
                Neuabgrund.battle_hill("Balrog", 2500, 150, 5000, 30, ("Fire Punch", "Rojogrund", "Hellblast", "Burnt Terrain"), (50, 100, 500, 20))
            elif randomeventmodifier == 1000:
                Neuabgrund.battle_hill("Garry Kasparov", 28510, 800, 28510, 10, ("Check", "1996", "Kasparov's Immortal", "Rapid"), (100, Hero.maxhealth*0.1, 913, 10))

charactername = input("Choose character name.\n")
turns = 0

window = tk.Tk()
window.title("OOP Adventures") 
window.geometry("1200x800") 
window.resizable(False, False)

prompt = tk.Label(window, text="Character status",
font=("Calibri", 28))
prompt.pack(pady=20)

Elias = Hero(f"{charactername}", 100, 1000, ["wooden armour", "wooden sword"], 0, 100, 50, 30)
Breunat = Market()
Neuabgrund = Enemy()
Abstreich = Event()
windowname = tk.Label(window, text=f"{Elias.name}", font=("Calibri", 30))
windowname.pack(pady=20)
windowname.place(x=200, y=600)

healthstatus = tk.Label(window, text=f"{Elias.health}/{Elias.maxhealth}", font=("Calibri", 30))
healthstatus.pack(pady=20)
healthstatus.place(x=600, y=600)

inventorystatus = tk.Label(window, text=f"Inventory:{Elias.inventory}", font=("Calibri", 20))
inventorystatus.pack(pady=10)
inventorystatus.place(x=100, y=300)

while Elias.health > 0:
    if Elias.health < Elias.maxhealth:
        Elias.health += (Elias.maxhealth*0.05)
    elif Elias.health > Elias.maxhealth:
            Elias.health = Elias.maxhealth
            randomeventmodifier = random.randint(0,1000)
    round(Elias.health, 2)

    enemychance = random.randint(0,1000)
    Abstreich.random_event_modifier(enemychance)

    print("\nPlease select an option\n""[1] Check current health\n""[2] Check current speed\n""[3] Check curret strength\n""[4] Open the market\n""[5] Check inventory\n""[6] Check balance\n""[7] Pass Turn"
    )
    menu_input = input("Choose an action\n")
    while menu_input != "7":
        if menu_input == "1":
            print("Current health is", Elias.health)
        elif menu_input == "2":
            print("Current speed is", Elias.speed)
        elif menu_input == "3":
            print("Current strength is", Elias.strength)
        elif menu_input == "4":
            print("Okay, browsing the market")
            Breunat.buy()
        elif menu_input == "5":
            print("Inventory:", Elias.inventory)
        elif menu_input == "6":
            print("Balance:", Elias.balance)
        elif menu_input == "its time to roast":
            Elias.balance += 100000
        else:
            print("Invalid try again")
        print("\nPlease select an option\n""[1] Check current health\n""[2] Check current speed\n""[3] Check curret strength\n""[4] Open the market\n""[5] Check inventory\n""[6] Check balance\n""[7] Pass Turn"
        )
        menu_input = input("What else do you want to do?\n")
    print("Simulating turn...")
    turns += 1
    
    windowname.config(
        text = f"{Elias.name}")
    healthstatus.config(
        text = f"Health: {int(Elias.health)}/{Elias.maxhealth}")
    inventorystatus.config(
        text = f"Inventory:{Elias.inventory}")
print(f"{Elias.name} has died! Your final score is {Elias.stats}")
print(f"Turns survived:{turns}")



window.mainloop()
