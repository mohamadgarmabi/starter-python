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