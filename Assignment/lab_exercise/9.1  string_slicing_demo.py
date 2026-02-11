# string_slicing_demo.py

text = "HelloWorld"

# Slice from index 0 to 5 (characters 0 to 4)
print("text[0:5] =", text[0:5])

# Slice from index 5 to end
print("text[5:]  =", text[5:])

# Slice from beginning to index 5
print("text[:5]  =", text[:5])

# Slice the whole string
print("text[:]   =", text[:])

# Slice with step value
print("text[::2] =", text[::2])

# Slice using negative index
print("text[-5:] =", text[-5:])
