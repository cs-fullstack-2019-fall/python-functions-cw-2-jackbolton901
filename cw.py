# !! : "Create a function that will ask the user for a number." This is not a funciton 
num1 = int(input("enter a number  "))
num2 = int(input("enter a second number  "))

def useNum(num1, num2):

    calculations(num1, num2)

def calculations(this, that):
    print(this + that)
    print(this - that)
    print(this * that)
    print(this / that)
    
useNum(num1, num2)

