big_number = 100
small_number = 10

# True
print(big_number > small_number)

# False
print(big_number < small_number)


# None
print(None)

# False
print(None is None)

# True
print(None is not None)

# True
print(None == None)

# False
print(None != None)

# Type of None
print(type(None))

# And operator
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Or operator
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Not operator
print(not True)
print(not False)

# And operator with None
print(None and True)
print(None and False)
print("None and None", None and None)

# Or operator with None
print("None or True", None or True)
print("None or False", None or False)

# In operator
my_list = [1, 2, 3, 4, 5, "mohammad", 3.14, True, False]
print("'mohammad' in list:", "mohammad" in my_list)

# Not in operator
print("'mohammad' not in list:", "mohammad" not in my_list)

# Is operator
print("1 is 1:", 1 is 1)
print("1 is not 1:", 1 is not 1)

# dictionary
my_dictionary = {"name": "mohammad", "age": 31, "city": "tehran"}
print("'name' in dictionary:", "name" in my_dictionary)