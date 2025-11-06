# this scope i want define some variables and print them
hello_world = "hello world"
first_name = "mohammad"
last_name = "garmabi"
age = 31
is_married = False
percentage = 2.98
user_access = ["read", "write", "delete"]
favorites_list = ["reyhaneh", 7, True, 2.98, "python"] # mutable list
user_info = {"name": first_name, "age": age, "is_married": is_married}
max_favorite_item = (favorites_list[0], favorites_list[1], favorites_list[2], favorites_list[3], favorites_list[4]) # immutable tuple


def print_info():
    print("My name is", first_name, last_name, "and i am", age, "years old")
    print("I am married", is_married)
    print("I will learn python soon")

# this function is first my python code and i print some text in the bash terminal
print(hello_world)
print("My name is", first_name, last_name)
print("I will learn python soon")
print("My favorite item is", max_favorite_item)


# this scope i want found type of variable and print it
print(type(hello_world))
print(type(age))
print(type(is_married))
print(type(print_info))
print(type(percentage))
print(type(user_access))
print(type(favorites_list))
print(type(user_info))
print(type(max_favorite_item))

# this scope i want write first class in python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print("Person created")
    print("Name:", self.name)
    print("Age:", self.age)

  def say_hello(self):
    print("Hello, my name is", self.name, "and i am", self.age, "years old")

person = Person(first_name, age)
person.say_hello()

person.name = "ali"

# this scope i want write a function to print the user info

def print_user_info():
  print("start of user info: ______________________________________")
  print("Name:", user_info["name"])
  print("Age:", user_info["age"])
  print("Is married:", user_info["is_married"])
  print("end of user info: ______________________________________")
print_user_info()


