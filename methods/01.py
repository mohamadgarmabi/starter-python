def calculate_average(numbers = list[int]):
  """ This function calculates the average of the provided list of numbers.
  Args:
      numbers (list): A list of numbers to calculate the average of.

  Returns:
      int: The average of the provided list of numbers.
  """
  return int(sum(numbers) / len(numbers))


def average(numbers = list[int]):
  return calculate_average(numbers)

# default argument
numbers = [1,3,4,5,6,7,8,9,10]
# print the average of the numbers using the average function
print(average(numbers))

print("________________________________________________________")


def counter_keyword_characters(
    text: str = "default text", 
    keyword: str = "a"
) -> int:
    """ This function counts the number of occurrences of a keyword in a text.

    Args:
        text (str): The text to count the keyword in.
        keyword (str): The keyword to count in the text.

    Returns:
        int: The number of occurrences of the keyword in the text.
    """
    return text.count(keyword)

print(counter_keyword_characters("hello mohammad jan and how are you ?", "a"))

print("________________________________________________________")


def is_even(number: int)-> bool:

  """ This function checks if a number is even.
  Args:
      number (int): The number to check if it is even.

  Returns:
      bool: True if the number is even, False otherwise.
  """
  if type(number) != int:
    return False

  return number % 2 == 0


print(is_even(10))

print(is_even("mohammad"))

print("________________________________________________________")

def count_even_numbers_of_list(numbers: list[int])-> int:
  """ This function counts the number of even numbers in a list.
  Args:
      numbers (list[int]): The list of numbers to count the even numbers in.

  Returns:
      int: The number of even numbers in the list.
  """
  return sum(is_even(number) for number in numbers)

print(count_even_numbers_of_list([number for number in range(1,21)]))
print("________________________________________________________")


def first_even_number_of_list(numbers: list[int])-> int:
  """ This function finds the first even number in a list.
  Args:
      numbers (list[int]): The list of numbers to find the first even number in.

  Returns:
      int: The first even number in the list.
  """
  # return next(number for number in numbers if is_even(number))

  return next(number for number in numbers if is_even(number))

print(first_even_number_of_list([number for number in range(1,21)]))

print("________________________________________________________")
def big_even_number_of_list(numbers: list[int])-> int:
  """ This function finds the last even number in a list.
  Args:
      numbers (list[int]): The list of numbers to find the last even number in.

  Returns:
      int: The last even number in the list.
  """
  return max(number for number in numbers if is_even(number))

print(big_even_number_of_list([number for number in range(1,21)]))

print("________________________________________________________")

def check_even_number_of_list(numbers: list[int])-> bool:
  """ This function checks if a list contains any even numbers.
  Args:
      numbers (list[int]): The list of numbers to check if it contains any even numbers.

  Returns:
      bool: True if the list contains any even numbers, False otherwise.
  """
  return any(is_even(number) for number in numbers)

print(check_even_number_of_list([number for number in range(1,3)]))

print("________________________________________________________")


def found_largest_numbers(numbers: list[int])-> int:
    """ This function finds the largest number in a list.

    Args:
        numbers (list[int]): The list of numbers to find the largest number in.

    Returns:
        int: The largest number in the list.
    """
    return max(numbers)
 
print(found_largest_numbers([number for number in range(1,4)]))

print("________________________________________________________")

def found_largest_number_other_way(numbers: list[int])-> int:
    """ This function finds the largest number in a list without using the max function.

    Args:
      numbers (list[int]): The list of numbers to find the largest number in.

    Returns:
      int: The largest number in the list.
    """
    placeholder_number = numbers[0]

    for number in numbers:
      if number > placeholder_number:
        placeholder_number = number
    return placeholder_number


print(found_largest_number_other_way([number for number in range(1,4)]))


print("________________________________________________________")

def found_odd_numbers_of_list(numbers: list[int])-> list[int]:
  """ This function finds the odd numbers in a list.
  Args:
      numbers (list[int]): The list of numbers to find the odd numbers in.

  Returns:
      list[int]: The list of odd numbers in the list.
  """
  return [number for number in numbers if not is_even(number)]

print(found_odd_numbers_of_list([number for number in range(1,10)]))

print("________________________________________________________")

def ret_tuple_values(numbers: list[int]) -> tuple:
    """ This function returns a tuple of (number, is_even) for each number in the list.

    Args:
        numbers (list[int]): The list of numbers.

    Returns:
        tuple: Tuple of (number, is_even) pairs for all numbers.
    """
    # result = tuple((number, is_even(number)) for number in numbers)

    result = tuple((number, is_even(number)) for number in numbers)
    return result

print(ret_tuple_values([number for number in range(1,10)]))

print("________________________________________________________")

def multi_calculate_number(first_number: int, second_number: int)-> tuple:

    """ This function calculates the sum, difference, product, and quotient of two numbers.
    Args:
      first_number (int): The first number.
      second_number (int): The second number.

    Returns:
      tuple: Tuple of (sum, difference, product, quotient).
    """
    plus = first_number + second_number
    minus = first_number - second_number
    multiply = first_number * second_number
    divide = int(first_number / second_number)
    return tuple((plus, minus, multiply, divide))

print(multi_calculate_number(10, 5))
print(found_largest_number_other_way(multi_calculate_number(10, 5)))
print("________________________________________________________")

donations = {
  "mohammad": 1900,
  "ali": 200,
  "reza": 1300,
  "mahan": 500,
}

def found_name_of_donation(donations: dict[str, int], donation_amount: int) -> str:
  """ This function finds the name of the donor whose donation is closest to the integer average (could be multiple)
  Args:
      donations (dict[str, int]): The dictionary of donations.
      donation_amount (int): The amount of the donation.

  Returns:
      str: The name of the donor whose donation is closest to the integer average (could be multiple).
  """
  return next(name for name, amount in donations.items() if amount == donation_amount)

def donations_analysis(donations: dict[str, int]) -> dict:
    """ This function analyzes the donations and returns a dictionary of the analysis.
    Args:
        donations (dict[str, int]): The dictionary of donations.

    Returns:
        dict: The dictionary of the analysis.
    """
    all_amount_of_donations = donations.values()
    
    total_donations_amount = sum(all_amount_of_donations) ## sum of all donations
    max_donation_amount = max(all_amount_of_donations) ## max of all donations
    min_donation_amount = min(all_amount_of_donations) ## min of all donations
    average_donation_amount = int(total_donations_amount / len(donations)) if donations else 0
    # Find the name of the donor whose donation is closest to the integer average (could be multiple)
    max_donation_name = found_name_of_donation(donations, max_donation_amount)
    min_donation_name = found_name_of_donation(donations, min_donation_amount)

    return {
        "total_donations_amount": total_donations_amount,
        "average_donations_amount": average_donation_amount,
        "max_donation_info": {
          "name": max_donation_name,
          "amount": max_donation_amount,
        },
        "min_donation_info": {
          "name": min_donation_name,
          "amount": min_donation_amount,
        },
    }

print(donations_analysis(donations))


