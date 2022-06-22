import random as r
print("Welcome to Birdu World  ")
name = input("What is your name?\n  ")
print("you're welcome to birdu's model of rock,paper and scissors ",name)
gamelist = ['p','r','s']
print(""""Help:
papeer = p
scissors = s
rock = r
please let all your input be in lowercase! """) 
while(True): 
 UserInput = input("What is your input? ")
 AI = r.choice(gamelist)
 print(UserInput)
 print("AI chose",AI )
Tocontinue = input("Do you want to continue?(yes\no): ")
print(Tocontinue)
if Tocontinue == "yes":
   print(UserInput)
   print("AI chose",AI )   
elif Tocontinue == "no":
   print("thanks for playing this Game" , name)
    
else:
   print("Please enter the right input!")
