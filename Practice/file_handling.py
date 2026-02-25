# with open ("abc.txt","w") as a:
#     data=a.write("""hello
#     world
#                  ashish
#     kushwaha""")

# with open("abc.txt","a+")as a:
#     data=a.write("--------------")
#     print(data)


# with open ("abc.txt","r") as a:
#     data=a.readlines()
#     print(data)

# f = open("abc.txt",'w')
# # f.write("Writing somethong...")
# f.writelines(["Hello Python\n","Hello Tops"])
# f.close()


# f = open("abc.txt",'a')
# f.write("Writing something...")
# f.close()

# f = open("abc.txt",'r')
# # data = f.read()
# data = f.readlines()
# print(data)
# f.close()



# f = open("abc.txt",'r')
# while True:
#     data = f.readline()
#     print(data)
#     if not data:
#         break
# f.close()


# f = open("abc.txt",'r')
# while True:
#     data = f.read()
   
#     if not data:
#         break
#     print(len(data))
# f.close()

# f = open("abc.txt",'r')
# while True:
#     data = f.readlines()
   
#     if not data:
#         break
#     if "Hello" in data : 
#         print(data)
# f.close()



# with open("abc.txt",'r') as f : 
#     print(f.tell())
#     f.seek(10)
#     data  =f.read()
#     print(data)
#     print(f.tell())


# mode : r,w,a,r+,w+,a+,rb,wb

# with open("abc.txt",'r+') as f:
#     f.write("write something")
#     f.seek(0)
#     data = f.read()
#     print(data)

# with open("logo.png",'rb') as f :
#     data = f.read()
#     print(data)

# data = b"\x48\x65\x6C\x6C\x6F\x2C\x20\x57\x6F\x72\x6C\x64\x21"
# with open("db.bin",'wb') as f:
#     f.write(data)


# import json
# d = {"name":"kajal","email":"kajal@gmail.com"}
# with open("data.json",'w') as f:
#     json.dump(d,f)
