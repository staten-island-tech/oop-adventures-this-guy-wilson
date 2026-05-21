## Use following code as an alternative if needed for the "Market" definition.

**Don't delete this file; is used for debug and fixation purposes.**

```python
class Market:
    def __init__(self, inflation):
        self.inflation = inflation

    def check(self, market_items):
        for e in market_items:
            print(e["name"])
    
    def buy(self, balance, inflation, inventory):
        item = input("What would you like to buy in the Market?""\n")
        while (item != "exit") or (item != "end"):
            if item == "check":
               Market.check(item_data)
            elif item == "inventory":   
                print(inventory)
            else:
                for i in item_data:
                    if item == i["name"]:
                        Veliky_Tarnovo = True
                        print("Item Price:",int(i["price"]),"\n","Your balance:", balance, "\n")
                        print("Inflation", inflation, "\n")
                        try:
                            balance - int(i["price"]*inflation)
                        except int(inflation*i["price"]) > int(balance):
                            print("You cannot buy this item""\n")
                        else:
                            inventory_amount = len(inventory)
                            if inventory_amount < 5:
                                balance -= int(i["price"]*inflation)
                                if item == "health potion":
                                    Hero.health += 20
                                elif item == "speed potion":
                                    Hero.speed +=20
                                elif item == "strength potion":
                                    Hero.strength +=20
                                else:
                                    inventory.append(item)
                                    print(f"{i["name"]} was purchased!""\n")
                                    return balance
                            else:
                                print("You have too much items in your inventory.")
                            return inventory
                if Veliky_Tarnovo == False:
                    print("No item found.")
            item = input("What else would you like to do?")
```