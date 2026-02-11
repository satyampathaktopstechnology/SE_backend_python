# string_methods_demo.py

text = "  Hello World  "

print("Original String:", text)

# Convert to uppercase
print("Uppercase:", text.upper())

# Convert to lowercase
print("Lowercase:", text.lower())

# Remove leading and trailing spaces
print("Stripped:", text.strip())

# Replace a word
print("Replace 'World' with 'Python':", text.replace("World", "Python"))

# Find position of a substring
print("Index of 'Hello':", text.find("Hello"))

# Check if string starts with a word
print("Starts with 'Hello':", text.strip().startswith("Hello"))

# Check if string ends with a word
print("Ends with 'World':", text.strip().endswith("World"))

# Split the string into a list
print("Split:", text.split())

# Join strings
words = ["Python", "is", "fun"]
print("Joined String:", " ".join(words))
