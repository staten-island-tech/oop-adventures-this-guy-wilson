# menu, bug fix, option to open market

while True:
    print("what do you want to do?""\n""[1] check current health""\n""[2] check current speed""\n""[3] check current strength""\n""[4] open the market")
    menu_input = int(input("What do you want to do?"))
    if menu_input == 1:
        print(Hero.Health)
    elif menu_input == 2:
        print(Hero.Speed)
    elif menu_input == 3:
        print(Hero.Strength)
    elif menu_input == 4:
        print("Okay, browsing the market")
