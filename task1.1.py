# the calculator app 
# ------- the function ---------




def add (x , y):
    return x + y 

def subtraction(x , y):
    return x - y 

def multiplication (x , y):
    return x * y 

def davidson (x , y ):
    if y == 0:
        return ("error")
    else: 
        return x / y 
    




#------------user input ---------


while True:
    print("enter 'add' and add two numbers. ")
    print("enter 'subtract' and add two numbers. ")
    print("enter 'multiply' and add two numbers. ")
    print("enter 'divide' and add two numbers. ")
    print("enter 'exit' to exit the program ")
    user = input(": ")

    if input == "exit":
        print ("peace!")
        break
        
            
    num1 = (input("enter your first number here: "))
    num2 = (input("enter your second number here:  "))
            

        
    if user == "add":
        print  (num1 , num2)
    elif user == "subtraction":
        print ({(num1 , num2)})
    elif user == "multiplication":
        print ({(num1 , num2 )})
    elif user == "division ":
        print ({ (num1 , num2)})
    else:
        print ("error!")
            

