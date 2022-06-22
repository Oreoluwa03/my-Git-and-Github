
import random
print("WELCOME TO BIRDU WORLD GUESSING GAME")
name =input("please enter your name(import info:let your answer be in lower case e.g a,answer): ")
print("Welcome",name)
print("Note this is a guessing game,you would be required to select a number at random and  if it corresponds with the number the AI chose,so keep trying to guess the number  ")
read = range(100)
while(True):
 gamer = input("pick a number between 1 to 100: ")
 AI = random.choice(read)
 if gamer == AI:
    print(name, "won")
 else :
       print("Oops,Try Again") 
 school = input("do you want to continue(yes\no): ")
 if school == "yes":
        continue
 elif school == "no":
    print("thanks for playing ")
    break




