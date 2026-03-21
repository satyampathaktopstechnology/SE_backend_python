file = open("sample.txt","w")

lines = [ 
    "Python is a powerful programming language.\n",
    "File handling is an important concept in Python.\n",
    "This program writes multiple strings into a file.\n"
    ]

file.writelines(lines)

file.close()

print("Multiple strings written successfully.")