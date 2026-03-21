print("Simple Calcutor")

try:
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))

    op = input("Enter the operator(+,-,*,/,)")

    if op == "+":
        result = num1 + num2
        print("Addition of two number:",result)

    elif op == "-":
        result = num1 - num2
        print("Substarection of two number:",result)

    elif op == "*":
        result = num1 * num2
        print("Multipliaction of two number:",result)
    
    elif op == "/":
        result = num1 / num2
        print("Division of two number:",result)

    else:
        print("Invalid choice")

except ValueError:
    print("Invalid input! To enter the valid input")

except ZeroDivisionError:
    print("Error ! Division of zeor is not allowed")

except Exception as e:
    print("Somthing went wrong",e)