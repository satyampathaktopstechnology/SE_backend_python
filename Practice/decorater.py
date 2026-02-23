# def args(func):
#     def exe():
#         print("hello rahul")

#         value = func()  

#         if value.isdigit():
#             print("is numeric")
#         else:
#             print("is alphabetic")

#         return value

#     return exe


# @args
# def arg1():
#     return "1"


# print(arg1())











# def args(func):
#     def exe():
#         print("hello rahul")

#         value = func()  
#         try:
#            if value==int(input(func())):
#               print("is numeric")
#            else:
#                print("is alphabetic")
#         except Exception as e:
#             print("Some error occurred:", e)
#             return e

            

#         return value

#     return exe


# @args
# def arg1():
#     return "jns,bf"


# print(arg1())



# def demo1(fun):
#     def exe(a,b,c):
#         a=int(input("enter a value of a"))
#         b=int(input("enter a value of a")) 
#         c=a+b
#         print("it is demo",c)
#         return demo1(fun())
#     return  exe('a','b','c')

# @demo1
# def demo():
#     print("hello")
# demo()

def add(func):
    def exe():
        a,b, d = func()
        print(d)
        print("Addition of A abd B is : ", a+b)
        return func
    return exe


@add
def sub():
    a = int(input("enter a value of a"))
    b = int(input("enter a value of b"))
    return a,b, f"Subtraction of {a} and {b} is: {a-b}"
    

sub()
