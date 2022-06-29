print("Good day Bro Olamide this is a code that accepts a list and multiplies it sir ")
def multiplyAll(input):
    sum =  1
    for nums in input:
        print(nums)
        sum = sum * nums
        print(sum)
multiplyAll()        

print("this is a code that prints all primenumbers")
def printPrimeNums():
    nums = range(101)
    for n in nums:
        if n%2 == 0:
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
factorial()

def takesInput():
    pull = input("enter: ")
    print(pull)
    return pull

takesInput()   


def myfunc(name):
    counter = name
    print(counter.strip(name))

    figures = {}
    for count in counter:
        if count in figures:
            figures[count] += 1
        else:
            figures[count] = 1
    print(figures) 
myfunc()

print("Thank you")
