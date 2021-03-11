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
  
  #Asking if the user wants to role the dice again. 

  roll_again = input("Roll It again?: ")
  if roll_again == 'n':
    break
  
  if roll_again != 'n' and roll_again != 'y' :
      print("Error: Not Acceptable Input Value (y/n). Please try run the code again.")
      break

