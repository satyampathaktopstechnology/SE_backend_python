# class Car:
#     name = "Mustang"
#     model_year = "2026"

#     def showcar(self):
#         print("Parent:", self.name, self.model_year)


# class Car1(Car):
#     name = "BMW"
#     model_year = "2025"

#     def showcar(self):
#         print("Child:", self.name, self.model_year)
#         super().showcar()


# c1 = Car1()
# c1.showcar()
# c2=Car1()
# c2.showcar()


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




class car:
    def get_car_info(self,name,model_year):
        self.name=name
        self.model_year=model_year
    

    def show_car_info(self):
        print(" car name: ",self.name,"\n model_year: ",self.model_year)

class supercar(car):
    def get_car_info(self, name, model_year):
        name="mustang"
        return super().get_car_info(name, model_year)
    def show_car_info(self):
        return super().show_car_info()
    
class fav():

    def favcar(self):
        self.name = []  
        for i in range(5):
            car = input("Enter your favorite car: ")
            self.name.append(car)

    def showfav(self):
        print("Your favorite cars are:")
        for car in self.name:
            print(car)
    


obj = fav()
obj.favcar()
obj.showfav()

        

    





# c1=car()
# c2=supercar()
# c2.get_car_info("bmw",2022)
# c2.show_car_info()

