print("Good day Bro Olamide this is a code that accepts a list and multiplies it sir ")
  

print("this is a code that prints all primenumbers")
def printPrimeNums():
    nums = range(2,101)
    for n in nums:
        if n%2 == 0:
           return 0 
        else:
            print(n)
printPrimeNums()           
print("this is a code that gets the factorial ")           
def factorial(info):
    info = range(1,info + 1)
    multiply = 1
    for info in info:
        multiply = multiply * info
        print(info)
        print(multiply)
factorial(3)

def takesInput():  
    pull = input("enter: ")
    #print(pull)
    return pull

#takesInput()   


def myfunc(name):
    counter = name
    print(counter.strip(name))
    

    figures = {}
    for count in counter:
        if count in figures:
            figures[count] += 1
        else:
            figures[count] = 1
    
    dict.fromkeys(figures)
    print(figures)
myfunc("This is a boy That")

print("Thank you")
def getPrimenums(nums):
   if nums < 2:
        return 0
   x = nums // 2
   for j in range(2,x +1):
     if nums % j == 0:
        return 0                 
   return 1


for i in range(1, 100 + 1):
    if getPrimenums(i):
        print(i, end=" ")

 
