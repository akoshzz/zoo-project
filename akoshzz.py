class Animal:
    def __init__(self, name, age):
        self.name = name  
        self.age = age   

    def make_sound(self):
        print("Some animal sound...") 


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


class Zoo:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен(а) в зоопарк.")
    
    def show_all(self):
        print("\nВсе животные в зоопарке:")
        for animal in self.animals:
            print(f"{animal.name}, {animal.age} лет")
    
    def make_all_sounds(self):
        print("\nВсе животные издают звуки:")
        for animal in self.animals:
            animal.make_sound()


zoo = Zoo()

lion = Lion("Aknazar", 5)
monkey = Monkey("Yerassyl", 2)
elephant = Elephant("Batyr", 10)

zoo.add_animal(lion)
zoo.add_animal(monkey)
zoo.add_animal(elephant)

zoo.show_all()
zoo.make_all_sounds()
