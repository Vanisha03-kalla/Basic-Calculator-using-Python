def sumb(a,b):
    return a+b
def minus(a,b):
    return a-b
def mul(a,b):
    return a*b
def divd(a,b):
    if b==0:
        return "Error! Division by zero is not allowed."
    return a/b

while True:
    num1=float(input('Enter the 1st Number:'))
    num2=float(input('Enter the 2nd Number:'))
    a=input('Enter  an Operator(Type exit to quit):')
    if a=='+':
         print(f"Result: {sumb(num1, num2)}")
    elif a=='-':
         print(f"Result: {minus(num1, num2)}")
    elif a=='*':
         print(f"Result: {mul(num1, num2)}")
    elif a=='/':
         print(f"Result: {divd(num1, num2)}")
    elif a=='exit':
        print('BYE 😭')
        break    

    else:
        print("Please choose a valid operator.")               
