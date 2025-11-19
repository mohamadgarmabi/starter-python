# print("START OF THE PROGRAM")
# puberty_age = 18

# try:
#   # comment: 
#   age = int(input("enter your age: "))
# except ValueError:
#   print("Invalid input: please enter a number for your age.")
# else:
#   # The following line checks if the user is at the exact puberty threshold (which is 18).
#   if age == puberty_age:
#       print("you are exactly at the puberty age")
#   elif age > puberty_age:
#       print("you are a teenager")
#   else:
#       print("you are not a teenager")

# print(f"END OF THE PROGRAM, your age is {age}")

# FOR LOOP __________________________________________________________
# START __________________________________________________________

from random import random


print("START OF THE FOR LOOP")
count = 0
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for item in my_list:
  if item % 2 == 0:
    count += 1
    print(f"item: {item} is even")
  else:
    print(f"item: {item} is odd")

print(f"count of even numbers: {count}")

print("--------------------")

# END __________________________________________________________

# START __________________________________________________________

characters = "mohammad garmabi is software engineer"
count_m = 0 

for character in characters:
  print(f"character: {character}")
  if character.startswith("m"):
    count_m += 1
    print(f"character: {character} is starting with m")
  else:
    print(f"character: {character} is not starting with m")

print(f"count of m: {count_m}")
print("--------------------")

# END __________________________________________________________


# START __________________________________________________________
people = (("mohammad", 31), ("reyhaneh", 30), ("ali", 25), ("reza", 20))

for person in people:
  name,age = person

  if age > 25:
    print(f"name: {name} is older than 25 years old and age is {age}")
  else:
    print(f"name: {name} is younger than 25 years old and age is {age}")

print("--------------------")

# END __________________________________________________________

# START __________________________________________________________

people = {
  "mohammad": 31,
  "reyhaneh": 30,
  "ali": 25,
  "reza": 20,
  "ahmad": 10,
  "hamed": 0,
}

for person in people:
    print(f"Your name is {person} and your age is {people[person]}")
print(f"All data is here: {people}")
print("--------------------")


# END __________________________________________________________

# START __________________________________________________________

user_info = {
  "name": "mohammad",
  "age": 31,
  "position": "software engineer",
  "living": "tehran"
}

for key, value in user_info.items(): 
    print(f"key is '{key}'")
    print(f"value is '{value}'")
    print("--------------------")

print(f"All data is here: {user_info}")
print("--------------------")

# END __________________________________________________________


# WHILE LOOP __________________________________________________________

print("START OF THE WHILE LOOP")
count = 0

while count < 10:
  print(f"count is {count}")
  count = count + 1

print("--------------------")

# END __________________________________________________________

# Hope game

print("START OF THE HOPE GAME")
n = 0

while n < 20:
  n = n + 1
  if n % 3 == 0 and n % 5 == 0:
    print("HIP HOP HOPE GAME")
    continue
  
  if n % 3 == 0:
    print("HOPE")
    continue
  elif n % 5 == 0:
    print("HOP HOPE GAME")
    continue
  else:
    print(f"n is {n}")
    continue

print("--------------------")

# END __________________________________________________________

# START __________________________________________________________

# OLD WAY __________________________________________________________
l= [1,0.45, 9, -1]

new_l = []

for item in l:
  new_l.append(item * 2)

print(new_l)

print("--------------------")

# END __________________________________________________________

# NEW WAY __________________________________________________________


l= [1, 0.45, 9, -1, 5, 4 , 10]
# LIST COMPREHENSION
new_l = [item * 2 for item in l]
new_l_2 = [n for n in l if n % 2 == 0]

print(new_l)
print(new_l_2)

print("--------------------")

# END __________________________________________________________

# START __________________________________________________________

number = 5

result = "even" if number % 2 == 0 else "odd"
result_2 = "positive" if number > 6 else "negative"

print(f"number is {number} and it is {result}")
print(f"number is {number} and it is {result_2}")


# END __________________________________________________________

# START __________________________________________________________

# NESTED LOOP
# RANGE
row = int(input("Enter a number: "))
column = int(input("Enter a number: "))

for i in range(row):
  for j in range(column):
    print(f"{i} * {j} = {i * j}")

print("--------------------")

# END __________________________________________________________

n = range(2, 10)
print(n)

print("--------------------")

# START __________________________________________________________
# ENUMERATE
my_list = ["mohammad", "ali", "reza", "hamed"]
enumerate_n = enumerate(my_list)

for i, item in enumerate_n:
  print(f"index is {i} and item is {item}")

print("--------------------")

# END __________________________________________________________

# START __________________________________________________________
# ZIP
first_name = ["mohammad", "ali", "reza", "hamed"]
last_name = ["garmabi", "ahmadi", "rezaii", "hamidi"]

for person in zip(first_name, last_name):
  name, last_name = person
  print(f"name is {name} and last name is {last_name}")

print("--------------------")

# END __________________________________________________________

# START __________________________________________________________
names = ["mohammad", "ali", "reza", "hamed"]
people = {
  "mohammad": {
    "age": 31,
    "city": "tehran",
    "country": "iran",
  },
  "ali": {
    "age": 25,
    "city": "tehran",
    "country": "iran",
  },
  "reza": {
    "age": 20,
    "city": "tehran",
    "country": "iran",
  },
}


for name in names:
  if name in people:
    print(f"age of {name} is {people[name]['age']}")
  else:
    print(f"name {name} is not found in the people list")
  print("--------------------")

# END __________________________________________________________

# START __________________________________________________________
from random import randint

number = randint(1, 100)

while True:
  guess = int(input("Enter a number: "))
  if guess == number:
    print("You guessed the number!")
    break
  else:
    print("You guessed the number wrong!")
    continue

# END __________________________________________________________