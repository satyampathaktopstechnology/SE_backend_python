print("\nCheck the you can enter the string is word serach\n")
import re

text = input("Enter the string:")
word = input("Enter word to search:")

result = re.search(word,text)

if result:
    print('Word found in the string')
else:
    print("Word not found")