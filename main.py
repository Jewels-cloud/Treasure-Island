print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
choice = input("Type \"left\" or \"right: ")

if choice == "left":
    print("You've come to a lake. There is an island in the middle of the lake."
          "\nType \"wait\" to wait for a boat. Type \"swim\" to swim across.")

    choice = input("Type \"swim\" or \"wait: ")

    if choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors."
              "\nOne red, one yellow and one blue. \nWhich colour do you choose?")

        choice = input('Type "red", "yellow" or "blue": ')

        if choice == "yellow":
            print("Congratulation!!!! - YOU WON!!!")
        elif choice == "blue":
            print("Eaten by beasts \n GAME OVER!")
        elif choice == "red":
            print("Burned by fire \n GAME OVER!")
        else:
            print("Crushed by rock \n GAME OVER!")

    else:
        print("Attacked by a trout \nGAME OVER!")
else:
    print("Fall into a hole \nGAME OVER!")



