x=int(input("What's x? "))
operator=input("Enter operator(+,-,*,/): ")
y=int(input("What's y? "))
match operator:
    case '+':print("Result = ",x+y)
    case '-':print("Result = ",x-y)
    case '*':print("Result = ",x*y)
    case '/':print("Result = ",x/y)
    case '_':print("Result not found")

