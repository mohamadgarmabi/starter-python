

def divider():
    """This function is used to divide the text

    Args:
      None

    Returns:
      None
    """
    print("--------------------------------")



## old way

family_ages = [31, 32, 60, 64]

def add_one(age: int)-> int:
    """This function is used to add one to the age
    Args:
      age: int: the age
    Returns:
      int: the age + 1
    """
    return age + 1

for age in family_ages:
    print(add_one(age))

# new way with map method

# map with anonymous function (lambda function)
family_ages_map = map(lambda age: age ** 2, family_ages)

print(list(family_ages_map))

# filter

family_ages_filter = filter(lambda age: age >= 60, family_ages)

print(list(family_ages_filter))


names = ["mohammad", "ali", "reza", "hassan", "hossein", "reyhaneh"]


shorten_names = filter(lambda name: len(name) >= 2 and name.startswith("r") , names )
print(list(shorten_names))