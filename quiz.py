def quizGame():
    print("Welcome To Birdu World")
    print("Hello There this is Birdu's AI")
    name = input("What is your name?  ")
    print("WELCOME",name)
    print("Okay my name is Alex I'm your AI friend for this game.")
    print("Before you continue rules: all answers must be in lower case!!")
    Question1=("1.From your options below,What Country is the largest country in Africa in  Km2?")
    print(Question1)
    options = input({"a":".Algeria","b":".Nigeria","c":".South Africa"} )
    print('you chose',options) 
    if options== "a":
       print("correct",'advance to the next question ')
    else:
        print("hint: it's a North African country")
        print("try Again")
    Question2 = ("What is the name of the Country with the highest population in the world?  ")
    print(Question2)    
    options2 = input({"a:Tokyo","b:Hong Kong","c:New York"})
    print("you chose",options2)
    if options2=="a":
        print("correct,congratulations you have passed the quiz",name)
    else:
        print("Try again")    

quizGame()    