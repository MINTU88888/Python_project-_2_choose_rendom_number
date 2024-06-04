 # guess number
import random

target = random.randint(1 , 100)
while True:
    userchoice = int(input(" guess the target : "))  
    if(userchoice == target):
        print("success : correct guess !!")
        break
    if(userchoice < target):
        print("your number was too small. take a bigger guess....")
    else:
        print("your number was too big. take a smaller guess....")


print("-----GAME OVER----")
