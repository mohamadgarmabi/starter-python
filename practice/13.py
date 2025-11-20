def divider():
    """This function is used to divide the text

    Args:
      None

    Returns:
      None
    """
    print("--------------------------------")


def sum_numbers(*args: int)-> int:
    """This function is used to sum the numbers

    Args:
      *args: int: the numbers

    Returns:
      int: the sum of the numbers
    """
    return sum(args)

print(sum_numbers(7 ,3 ,2 ,1 ,9))

divider()


def is_even(number: int)-> bool:
    """This function is used to check if the number is even
    Args:
      number: int: the number
    Returns:
      bool: True if the number is even, False otherwise
    """
    return number % 2 == 0


def pick_evens(*args: int) -> list:
    """This function is used to pick the even numbers from the given arguments
    Args:
      *args: int: the numbers
    Returns:
      list: the list of the even numbers
    """
    return [arg for arg in args if is_even(arg)]

print(pick_evens(1, 2, 3, 4, 5, 6))
print(pick_evens(7, 13, 19, 21))

divider()

def skyline(*args: int) -> int:
    """This function is used to find the skyline of the given arguments
    Args:
      *args: int: the numbers
    Returns:
      int: the skyline of the given arguments
    """
    return max(args)

print(skyline(3, 7, 15, 2, 9))
print(skyline(1, 1, 1, 1))

divider()
