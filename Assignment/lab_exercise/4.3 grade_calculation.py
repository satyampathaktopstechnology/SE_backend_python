# Write a Python program to calculate grades based on percentage using
# if-else ladder.
input("enter name of student: ")
print("Take marks between 1 to 100")
sub1=int(input("enter the marks of subject1: "))
sub2=int(input("enter the marks of subject1: "))
sub3=int(input("enter the marks of subject1: "))
sub4=int(input("enter the marks of subject1: "))
sub5=int(input("enter the marks of subject1: "))
total_marks=sub1+sub2+sub3+sub4+sub5
percentage=(total_marks/500)*100
print(percentage)

# Grade Calculator Program
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

