# MY SOLUTION FOR THE 14TH PRACTICE

# class Animal:
#   def __init__(self, name: str, species: str, age: int, sound: str):
#     self.name = name
#     self.species = species
#     self.age = age
#     self.sound = sound

#   def make_sound(self):
#     return f"{self.name} makes {self.sound}"

#   def info(self):
#     return f"This is a {self.species} named {self.name} and it is {self.age} years old and it makes {self.sound}"

#   def __str__(self):
#     return f"Animal(name={self.name}, species={self.species}, age={self.age}, sound={self.sound})"

#   def __len__(self):
#     return self.age

# class Lion(Animal):
#   def __init__(self, name: str, species: str, age: int, sound: str):
#     super().__init__(name, species, age, sound)

# lion = Lion("Lion", "Lion", 10, "Roar")
# dog = Animal("Dog", "Dog", 5, "Woof")

# print(lion.info())
# print(dog.info())

# class Bird(Animal):
#   def __init__(self, name: str, species: str, age: int, sound: str):
#     super().__init__(name, species, age, sound)

#   def make_sound(self):
#     return f"This function is overridden in the Bird class"

# bird = Bird("Bird", "Bird", 2, "Tweet")
# print(bird.make_sound())

# print(str(bird))
# print(len(bird))


# CURSOR SOLUTION FOR THE 14TH PRACTICE
class Animal:
    zoo_name = "Tehran Zoo"
    
    def __init__(self, name: str, species: str, age: int, sound: str):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        
    def make_sound(self):
        print(self.sound)
    
    def info(self):
        print(f"This is a {self.species} named {self.name}, aged {self.age}, makes '{self.sound}', and belongs to {self.zoo_name}.")

    def __str__(self):
        return f"Animal(name={self.name}, species={self.species}, age={self.age}, sound={self.sound})"

lion = Animal("Simba", "Lion", 10, "Roar")
lion.info()
lion.make_sound()

dog = Animal("Max", "Dog", 5, "Woof")
dog.info()
dog.make_sound()

class Bird(Animal):
    def __init__(self, name: str, species: str, age: int, sound: str, wing_span: float):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} the bird sings: {self.sound}")

    def info(self):
        print(f"This is a {self.species} named {self.name}, aged {self.age}, wing span {self.wing_span}m, makes '{self.sound}', and belongs to {self.zoo_name}.")

parrot = Bird("Polly", "Macaw", 3, "Squawk", 0.4)
parrot.info()
parrot.make_sound()
print(parrot)
