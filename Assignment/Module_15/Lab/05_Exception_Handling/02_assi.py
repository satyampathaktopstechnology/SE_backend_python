print("Program start")
try:

    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second nunber:"))

    c = num1 / num2
    print("Result:",c)

    l1 = [10,20,30]
    print("Element:",l1[5]) #indexError

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot division by zero")

except IndexError:
    print("list index is out of range")

except Exception as e:
    print("Error",e)

print("program ended")