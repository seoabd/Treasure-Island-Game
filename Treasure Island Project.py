print(r'''
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

user_choice = input("You're at a cross road. Would you go left or right?: ").lower()
if user_choice == "right":
    print("Fall into a hole, Game Over!")
    exit()

user_choice1 = input("You have come to a lake. There is an island in the middle of the lake. Would you swim or wait?: ").lower()
if user_choice1 == "swim":
    print("You got eaten by beasts, Game Over!")
    exit()

user_choice2 = input("You arrived at the island unharmed.There is a house with three doors.Open one door, yellow, blue or red?: ").lower()
if user_choice2 == "yellow":
    print("You WON!")
elif user_choice2 == "blue":
    print("You got attacked by trout, Game Over!")
    exit()
elif user_choice2 == "red":
    print("Burned by fire, Game Over!")
    exit()
else:
    print("Sorry, Game Over!")