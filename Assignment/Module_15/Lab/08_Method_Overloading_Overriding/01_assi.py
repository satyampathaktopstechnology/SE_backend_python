class demo:
    def add(self,*num):
        s=0
        for i in num:
            s=s+i
        print('Sum=',s)

d =demo()

d.add(20,40)
d.add(40,50,60)
d.add(10,20,30,40)


#user can input the number

n = int(input("Enter how many number you want to add:"))

numbers = []
for i in range(n):
    x = int(input("Enter the numbers:"))
    numbers.append(x)

d.add(*numbers)
