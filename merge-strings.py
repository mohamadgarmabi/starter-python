my_first_name = "mohammad"
my_last_name = "garmabi"
my_age = 31
my_height = 175.723444


# old way
my_full_name = "my full name is: " + my_first_name + " " + my_last_name
print("old way to merge strings: my full name is:", my_full_name) 

# old way to merge strings (oldest way)
my_full_name = "my full name is: %s %s" % (my_first_name, my_last_name)
print("new way to merge strings:(3) my full name is:", my_full_name)

# masood way
masood_way = "masood name is %(label)s and his age is %(age)d" % {"label": "masood", "age": 31}
print("masood way to merge strings:", masood_way)


# new way
# new way to merge strings (first way)
my_full_name = f"my full name is: {my_first_name} {my_last_name}" 
print("new way to merge strings:(1) my full name is:", my_full_name)

# new way to merge strings (second way)
my_full_name = "my full name is: {} {}".format(my_first_name, my_last_name)
my_full_name_v2 = "my full name is: {1} {0} and i am {2} years old".format(my_first_name, my_last_name, my_age)
my_full_name_v3 = "my full name is: {my_first_name} {my_last_name} and i am {my_age} years old".format(my_first_name=my_first_name, my_last_name=my_last_name, my_age=my_age)
print("new way to merge strings:(2) my full name is:", my_full_name)
print("new way to merge strings:(2) my full name is:", my_full_name_v2)
print("new way to merge strings:(2) my full name is:", my_full_name_v3)

# for practice
my_full_description = f"my full description is: my name is {my_first_name} {my_last_name} and i am {my_age} years old"
print("my full description is:", my_full_description)

my_full_description_v2 = f"my full description is: my name is {my_first_name} {my_last_name} and i am {my_age} years old and my height is {my_height:1.2f}"
print("my full description is:", my_full_description_v2)