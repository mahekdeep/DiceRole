#DiceRole
import random

#Setting Input Variables
min = 1 
max = 6
#Setting Dices at Ints 
dice1 = 0
dice2 = 0

#Using "Y or N" to incidcate if user wants to role again. 
roll = "y"



#Asking Users Input for role 
print("Would you like to Roll the Dice? ")
roll =input("Please Type y/n: ")

while roll == "y":
  print("Rolling the dice...")
  dice1 = random.randint(min,max)
  dice2 = random.randint(min,max) 
  print("The values are ", dice1,", ",dice2)
  #print(dice1,dice2)
  
  roll_again = input("Roll It again?: ")
