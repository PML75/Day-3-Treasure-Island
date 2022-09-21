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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

def tRed():
  print("\nA raging fire consumes you.\n*Game Over")
  
def tYellow():
  print("\nA golden chest appears filled treasure beyond your wildest dreams!\n*You Win!")
  
def tBlue():
  print("\nYou hear a rumbling snarls. A group of beasts greets you\n*Game Over")

def tIsland():
  door = input("\nYou arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow, one blue. Which colour do you choose: ").lower()
  if (door == "red"):
    tRed()
  elif (door == "yellow"):
    tYellow()
  else:
    tBlue()

def tLake():
  print("\nA lake awaits you. There is an island in the middle.")
  lake = input('Type "wait" for a boat. Type "swim" to swim across: ').lower()
  if (lake == "swim"):
    print("\nA crowd of sharks awaits you\n*Game Over")
  else:
    tIsland()

print("You're at a crossroad. There are no visible signs,\nbut two trails leading left or right. Your mind\ntells you to go left, but your body sways right.")

tCrossRoad = input('Where do you want to go? Type "left" or "right": ').lower()

if (tCrossRoad == "right"):
  print("\nYou fall into a hole and break your ankle.\n*Game Over")
else:
  tLake()

