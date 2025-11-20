def divider():
    """This function is used to divide the text

    Args:
      None

    Returns:
      None
    """
    print("--------------------------------")


# *args
def describe_user(*args: dict)-> None:
    """This function is used to describe the user information

    Args:
      *args: dict: the user information

    Returns:
      None
    """
    for arg in args:
      for key, value in arg.items():
        print(f"{key}: {value}")

describe_user({"name": "John", "age": 30, "city": "New York"})

divider()

# **kwargs
def describe_user_kwargs(**kwargs: dict)-> None:
    """This function is used to describe the user information

    Args:
      **kwargs: dict: the user information

    Returns:
      None
    """
    print(kwargs)

describe_user_kwargs(name="John", age=30, city="New York")


divider()


def calculate(**kwargs):
    """This function is used to calculate the sum of the numbers or the user information

    Args:
      **kwargs: dict: the user information

    Returns:
      int: the sum of the numbers
      str: the user information
      str: "No data provided"
    """
    # if all(k in kwargs for k in ["a", "b", "c"]):
    if all(k in kwargs for k in ["a","b","c"]):
        return kwargs['a'] + kwargs['b'] + kwargs['c']

    if all(k in kwargs for k in ["name","age","city"]):
        return f"My name is {kwargs['name']} and i am {kwargs['age']} years old and i live in {kwargs['city']}"

    return "No data provided"

print(calculate(a=1, b=2, c=3))

divider()

print(calculate(name="Mohammad", age=30, city="Tehran"))