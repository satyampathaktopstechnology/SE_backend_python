

# class A:
#     a = 10
#     def display(self):
#         print("Display")

# #simple or single inheritance
# class B(A):
#     b = 20
#     def show(self):
#         super().display()
#         print(self.b)
#         print(self.a)
# b1=B()
# b1.show()




# class car:
#     def get_car_info(self,name,model_year):
#         self.name=name
#         self.model_year=model_year
    

#     def show_car_info(self):
#         print(" car name: ",self.name,"\n model_year: ",self.model_year)

# class supercar(car):
#     def get_car_info(self, name, model_year):
#         name="mustang"
#         return super().get_car_info(name, model_year)
#     def show_car_info(self):
#         return super().show_car_info()
    
# class fav():

#     def favcar(self):
#         self.name = []  
#         for i in range(5):
#             car = input("Enter your favorite car: ")
#             self.name.append(car)

#     def showfav(self):
#         print("Your favorite cars are:")
#         for car in self.name:
#             print(car)
    


# obj = fav()
# obj.favcar()
# obj.showfav()

    

# c1=car()
# c2=supercar()
# c2.get_car_info("bmw",2022)
# c2.show_car_info()

class tree():
    def get_info(self,name ,colour):
        self.name=name
        self.colour=colour
    

    def show_data(self):
        print(self.name,self.colour)

class inhritence(tree):
    def get_info(self, name, colour,place):
        self.place=place
        return super().get_info(name, colour)
    def show_data(self):
        print(self.place)
        return super().show_data()
    
class multipleinheritence(inhritence):
    def get_info(self, name, colour, place,owner):
        self.owner=owner
        return super().get_info(name, colour, place)
     
    def show_data(self):
        print(self.owner)
        return super().show_data()


t=multipleinheritence()
t.get_info("apple","red","kim","ashish")
t.show_data()