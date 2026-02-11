# Program to print star pattern using nested for loop

rows = 4

# Outer loop for number of rows
for i in range(1, rows + 1):

    # Inner loop for printing stars in each row
    for j in range(i):
        print("*", end="")

    # Move to next line after each row
    print()
