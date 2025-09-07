class Animal:
    def __init__(self, name, age):
        self.name = name  
        self.age = age   

    def make_sound(self):
        print("Some animal sound...") 

animal = Animal("nonname", 3)
print(f"{animal.name}, {animal.age} лет")
animal.make_sound()

class Lion(Animal):
    def make_sound(self):
        print("Roar!")


class Monkey(Animal):
    def make_sound(self):
        print("Ooh-ooh!")


class Elephant(Animal):
    def make_sound(self):
        print("Trumpet!")

lion = Lion("Aknazar", 5)
monkey = Monkey("Yerassyl", 3)
elephant = Elephant("Batyr", 10)

lion.make_sound()      
monkey.make_sound()   
elephant.make_sound() 

class Lion(Animal):
    def make_sound(self):
        print("Roar! ")

    def feed(self):
        print(f"{self.name} eats meat.")


class Monkey(Animal):
    def make_sound(self):
        print("Ooh-ooh!")

    def feed(self):
        print(f"{self.name} eats banana.")


class Elephant(Animal):
    def make_sound(self):
        print("Trumpet!")

    def feed(self):
        print(f"{self.name} eats grass.")

lion = Lion("Aknazar", 5)
monkey = Monkey("Yerassyl", 3)
elephant = Elephant("Batyr", 10)

lion.feed()     
monkey.feed()    
elephant.feed() 
