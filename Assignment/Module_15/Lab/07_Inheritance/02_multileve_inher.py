class animal:
    def pet(self):
        print("This is the pet animal")

class dog(animal):
    def bark(self):
        print("The dog is barking")

class cat(dog):
    def meow(self):
        print("cat sound is meeow")

class whild(cat):
    def tiger(self):
        print("Tiger is the very denger whild animal")

w = whild()

w.tiger()
w.meow()
w.bark()
w.pet()