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

class Item:
    def __init__(self):
        pass

class Market:
    def __init__(self, market_items):
        self.market_items = market_items

    def buy_menu(self, hero):
        print("\nThis is the market")
        print("Type 'check' to see the items, 'buy' to purchase an item, 'inventory' to see your bag, or 'exit' to leave")
    
        choice = input("What would you like to do in the Market?""\n")
        while (choice != "exit") or (choice != "end"):
            if choice == "check":
               Market.check(item_data)
            elif choice == "inventory":   
                print(Hero.inventory)
            elif choice == "buy":
                Market.cashier(Hero.balance)
            choice = input("What else would you like to do?")

    def check(self, market_items):
        for e in market_items:
            print(e["name"])

    def cashier(balance):
        sonion = input("What do you want to buy.")
        for i in item_data:
            if sonion == i["name"]:
                print("Item Price:",int(i["price"]),"\n","Your balance:", balance, "\n")
                if int(i["price"]) > int(balance):
                    print("You cannot buy this item""\n")
                else:
                    inventory_amount = len(Hero.inventory)
                    if inventory_amount < 5:
                        balance -= int(i["price"])
                        if sonion == "health potion":
                            Hero.health += 20
                        elif sonion == "speed potion":
                            Hero.speed +=20
                        elif sonion == "strength potion":
                            Hero.strength +=20
                        else:
                            Hero.inventory.append(sonion["name"])
                            print(f"{i["name"]} was purchased!""\n")
                            Hero.balance == balance
                    else:
                        print("You have too much items in your inventory.")

class Enemy:
    def __init__(self):
        pass
    
    def enemy_attack(self, name, baseattack, speed, attackname, power):
        enemy_attack_choose = random.randint(0,4)
        if enemy_attack_choose == 4:
            print(f"The {name} uses the base attack.")
            power = baseattack
            Hero.health -= power
        elif enemy_attack_choose == 3:
            speed += power[enemy_attack_choose]
        else:
            print(f"The {name} uses {attackname[enemy_attack_choose]}.")
            Hero.health -= power[enemy_attack_choose]
    
    def hero_attack(self, enemyscore, enemyhealth):
                hero_choice = input("Select action")
                if hero_choice == "potion":
                    pass      
                elif hero_choice == "defense":
                    pass
                elif hero_choice == "flee":
                    flee = random.randint(0,10)
                    if flee <= 2:
                        enemyscore = 0
                    pass
                elif hero_choice == "attack":
                    enemyhealth -= Hero.health
                    pass
                else:
                    pass
                return enemyscore, enemyhealth

    def battle_hill(self, enemyname, enemyhealth, baseattack, enemyscore, enemyspeed, attackname, attackpower):
        print(f"An {enemyname} has spawned!""\n")
        print(f"Health:{enemyhealth}, Base Attack:{baseattack}")
        while (enemyhealth > 0) or (Hero.health > 0):            
            if Hero.speed >= enemyspeed:
                Enemy.hero_attack(enemyscore, enemyhealth)
                Enemy.enemy_attack(enemyname, baseattack, enemyspeed, attackname, attackpower)
                enemyspeed = Enemy.enemy_attack.speed
            else:
                Enemy.enemy_attack(enemyname, baseattack, enemyspeed, attackname, attackpower)
                enemyspeed = Enemy.enemy_attack.speed
                Enemy.hero_attack(enemyscore, enemyhealth)
        Enemy.death("Money", enemyname)
        Hero.stats += import tkinter as tk
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

class Item:
    def __init__(self):
        pass

class Market:
    def __init__(self):
        pass

    def buy(self):
        item = input("What would you like to buy in the Market?""\n")
        while (item != "exit") or (item != "end"):
            if item == "check":
               Market.check(item_data)
            elif item == "inventory":   
                print(Hero.inventory)
            elif item == "buy":
                Market.cashier(Hero.balance)
            item = input("What else would you like to do?")

    def check(self, market_items):
        for e in market_items:
            print(e["name"])

    def cashier(balance):
        sonion = input("What do you want to buy.")
        for i in item_data:
            if sonion == i["name"]:
                print("Item Price:",int(i["price"]),"\n","Your balance:", balance, "\n")
                if int(i["price"]) > int(balance):
                    print("You cannot buy this item""\n")
                else:
                    inventory_amount = len(Hero.inventory)
                    if inventory_amount < 5:
                        balance -= int(i["price"])
                        if sonion == "health potion":
                            Hero.health += 50
                            if Hero.health > Hero.maxhealth:
                                Hero.health = Hero.maxhealth
                        elif sonion == "speed potion":
                            Hero.speed += 20
                        elif sonion == "strength potion":
                            Hero.strength += 20
                        elif sonion == "boost potion":
                            Hero.maxhealth += 50
                        else:
                            Hero.inventory.append(sonion["name"])
                            print(f"{i["name"]} was purchased!""\n")
                            Hero.balance == balance
                    else:
                        print("You have too much items in your inventory.")

class Enemy:
    def __init__(self):
        pass
    
    def enemy_attack(self, name, baseattack, speed, attackname, power):
        enemy_attack_choose = random.randint(0,4)
        if enemy_attack_choose == 4:
            print(f"The {name} uses the base attack.")
            power = baseattack
            Hero.health -= power
        elif enemy_attack_choose == 3:
            speed += power[enemy_attack_choose]
        else:
            print(f"The {name} uses {attackname[enemy_attack_choose]}.")
            Hero.health -= power[enemy_attack_choose]
    
    def hero_attack(self, enemyscore, enemyhealth):
                hero_choice = input("Select action")
                if hero_choice == "potion":
                    pass      
                elif hero_choice == "defense":
                    pass
                elif hero_choice == "flee":
                    flee = random.randint(0,10)
                    if flee <= 2:
                        enemyscore = 0
                    pass
                elif hero_choice == "attack":
                    enemyhealth -= Hero.health
                    pass
                else:
                    pass
                return enemyscore, enemyhealth

    def battle_hill(self, enemyname, enemyhealth, baseattack, enemyscore, enemyspeed, attackname, attackpower):
        print(f"An {enemyname} has spawned!""\n")
        print(f"Health:{enemyhealth}, Base Attack:{baseattack}")
        while (enemyhealth > 0) or (Hero.health > 0):            
            if Hero.speed >= enemyspeed:
                Enemy.hero_attack(enemyscore, enemyhealth)
                Enemy.enemy_attack(enemyname, baseattack, enemyspeed, attackname, attackpower)
                enemyspeed = Enemy.enemy_attack.speed
            else:
                Enemy.enemy_attack(enemyname, baseattack, enemyspeed, attackname, attackpower)
                enemyspeed = Enemy.enemy_attack.speed
                Enemy.hero_attack(enemyscore, enemyhealth)
        Enemy.death("Money", enemyname)
        Hero.stats += enemyscore
        pass

    def death(self, loot, name):
        print("The",name,"has been slained.")
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
            roll = random.random()
            if roll <= 0.20:
                Enemy.battle_hill("Goblin", 25, 5, 100, 25, ("Cut", "Treasure-Dive", "Lock", "Metronome"), (2, 6, 10, 5))
            elif roll <= 0.05:
                Enemy.battle_hill("Vampire", 75, 10, 200, 40, ("Batwave", "Bite", "Bloodshear", "Floatation Dive"), (5, 10, 20, 5))
            elif roll <= 0.01:
                Enemy.battle_hill("Witch", 150, 15, 500, 20, ("Staffswing", "Potions", "Blind Illusions", "Speed Potion"), (8, 15, 25, 10))
            elif roll <= 0.001:
                Enemy.battle_hill("Regi", 500, 30, 2000, 20, ("Ice Shard", "Bulk Stomp", "Mirage Blast", "Weight Loss"), (15, 30, 50, 15))
            elif roll <= 0.0001:
                Enemy.battle_hill("Balrog", 1000, 100, 5000, 30, ("Fire Punch", "Rojogrund", "Hellblast", "Burnt Terrain"), (50, 100, 500, 20))
            elif roll <= 0.00001:
                Enemy.battle_hill("Garry Kasparov", 2851, 285, 28510, 10, ("Check", "1996", "Kasparov's Immortal", "Rapid"), (100, Hero.maxhealth*0.1, 913, 10))

charactername = input("Choose character name.\n")

window = tk.Tk()
window.title("OOP Adventures") 
window.geometry("1200x800") 
window.resizable(False, False)

prompt = tk.Label(window, text="Character status",
font=("Calibri", 28))
prompt.pack(pady=20)

Elias = Hero(f"{charactername}", 100, 1000, ["Stone Sword", "Wooden Shield"], 0, 100, 50, 100)
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
inventorystatus.place(x=800, y=600)

while Elias.health > 0:
    if Elias.health < Elias.maxhealth:
        Elias.health += (Elias.maxhealth*0.05)
    elif Elias.health > Elias.maxhealth:
            Elias.health = Elias.maxhealth
    Abstreich.random_event_modifier

    print("\nPlease select an option\n""[1] Check current health\n""[2] Check current speed\n""[3] Check curret strength\n""[4] Open the market\n""[5] Check inventory\n""[6] Check balance\n""[7] Pass Turn"
    )
    menu_input = input("Choose an action")
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
        else:
            print("Invalid try again")
        print("\nPlease select an option\n""[1] Check current health\n""[2] Check current speed\n""[3] Check curret strength\n""[4] Open the market\n""[5] Check inventory\n""[6] Check balance\n""[7] Pass Turn"
        )
        menu_input = input("What else do you want to do")
    print("Simulating turn...")
    
    windowname.config(
        text = f"{Elias.name}")
    healthstatus.config(
        text = f"{int(Elias.health)}/{Elias.maxhealth}")
    inventorystatus.config(
        text = f"Inventory:{Elias.inventory}")
print(Elias.name, "has died! Your final score is", Elias.stats)



window.mainloop()
