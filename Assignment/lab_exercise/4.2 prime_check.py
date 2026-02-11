# File Name: prime_check_flag.py
# Program to check if a number is prime using flag and if-else

# Taking input from the user
num = int(input("Enter a number: "))

flag=0
    # Checking divisibility from 2 to num-1
for i in range(2, num):
     if num % i == 0:
          flag = 1  # Number is not prime
          break 

    # Using if-else with flag
if flag == 0:
        print(num, "is a Prime Number")
else:
        print(num, "is Not a Prime Number")

