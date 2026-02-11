# List of fruits
List1 = ['apple', 'banana', 'mango']

# String to search
search_item = input("Enter the fruit name to search: ")

# Using for loop and if condition
for fruit in List1:
    if fruit in  search_item:
        print(search_item, "is found in the list ")
        break
else:
    print(search_item, "is not found in the list ")
