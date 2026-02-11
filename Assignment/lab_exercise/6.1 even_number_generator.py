# Generator function to generate first 10 even numbers

def even_numbers():
    for i in range(1, 11):
        yield i * 2   # Generates even numbers
        

# Using the generator
gen = even_numbers()

print("First 10 even numbers are:")
for num in gen:
    print(num)
