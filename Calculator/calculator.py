def add(x,y): 
    return x+y

def sub(x,y): 
    return x-y 

def mul(x,y): 
    return x*y 

def div(x,y): 
    if y == 0: 
        return "Error!, Please enter valid number!"
    else: 
        return x/y

def calculator(): 
    print("select your operation")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    
    choice = input("enter your choice:")
    num1 = int(input("enter your number1:"))
    num2 = int(input("enter your number2:"))
    if choice in ['1','2','3','4']: 
        if choice == '1': 
            print(f"{num1}+{num2} = {add(num1, num2)}")
        elif choice == '2': 
            print(f"{num1}+{num2} = {add(num1, num2)}")
        elif choice == '3': 
            print(f"{num1}+{num2} = {add(num1, num2)}")
        elif choice == '4':
            out = div(num1,num2)
            if out == "Error!, Please enter valid number!": 
                print(out)
            else:
                print(f"{num1}+{num2} = {add(num1, num2)}")
    else: 
        print("Please enter correct input!!!")
        
calculator()