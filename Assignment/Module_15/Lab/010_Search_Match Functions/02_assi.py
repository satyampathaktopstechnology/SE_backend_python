import re

text = input("Enter a sentence: ")

result = re.match("Good", text)

if result:
    print("The sentence starts with 'Good'")
else:
    print("The sentence does not start with 'Good'")