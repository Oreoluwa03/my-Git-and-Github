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
    options2 = input({"a":"Tokyo","b":"Hong Kong","c":"New York"})
    print("you chose",options2)
    if options2=="a":
        print("correct,congratulations you have passed the quiz",name)
    else:
        print("Try again")    
    Question3 = ("which of the following Teams play in the first Division of the Dutch League?")
    print(Question3)
    options3 = input({"a":"Vitesse","b":"Benfica","c":"Watford"}) 
    print("you chose ",options3)
    if options3== "a":
       print("you chose",options3)
    else:
        print("Try again")
    Question4 = ("When did Nigeria gain her independence? ")    
    print(Question4)
    options4 = input({"a":"1960","b":"1962","c":"1963"})
    print(options4)
    if options4=="a":
        print("you chose",options4)
    else:
        print("try again")
    Question5 =("What is the Capital of Brazil? ")
    print(Question5) 
    options5= input({"a":"Rio","b":"Augustus","c":"Brasilia"})   
    if options5== "c":
        print("Correct")
    else:
        print("try again")  
quizGame()    