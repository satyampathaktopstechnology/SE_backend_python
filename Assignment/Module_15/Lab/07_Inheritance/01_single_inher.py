class animal:
    def eat(self):
        print("Animal is eating")

class dog(animal):
    def bark(self):
        print("dog is barking")

d = dog()

d.eat()
d.bark()