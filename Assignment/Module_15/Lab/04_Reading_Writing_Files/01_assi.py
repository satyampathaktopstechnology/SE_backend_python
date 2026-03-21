file = open("example.txt","w")

file.write("I am Pathak Satyam.\n")
file.write("In This code file is reading and writting.")

file = open("example.txt","r")

f1 = file.read()

print("File content is:")
print(f1)

file.close()