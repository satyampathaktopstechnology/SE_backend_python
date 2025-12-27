percentage=int(input("enter your percentage"))
if(percentage>90 and percentage<100):
    print("your grade is A+")
elif(percentage>80 and percentage<=90):
    print("your grade is A")
elif(percentage>70 and percentage<80):
    print("your grade is B+")
elif(percentage>60 and percentage<70):
    print("your grade is  B")
elif(percentage>50 and percentage<60):
    print("your grade is c+")
elif(percentage>35 and percentage<50):
    print("your grade is c")
elif(percentage<=35):
    print("you are fail")
else:
    print("invalid number")

