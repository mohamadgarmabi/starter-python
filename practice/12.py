def say_hello_world():
    print("Hello World")

say_hello_world()

def divider():
    print("--------------------------------")

divider()

def say_hello_with_name(name: str)-> None:
    print("Hello", name)

say_hello_with_name("John")

divider()

def is_positive(number: int)-> bool:
    print(f"The number {number} is positive: {number >= 0}")
    return number >= 0

for number in [10, -10, 0, 2,3,-6,-9]:
    is_positive(number)

divider()

def sum_of_squares(fistNumber: int, secondNumber: int)-> int:
    return fistNumber ** 2 + secondNumber ** 2

print(sum_of_squares(5, 12))

divider()


def is_even(number: int)-> bool:
    return number % 2 == 0

for number in range(10, 21):
    print(f"The number {number} is even: {is_even(number)}")

divider()


def is_greater(firstNumber: int, secondNumber: int)-> bool:
    return firstNumber > secondNumber

print(is_greater(10, 5))
print(is_greater(3, 7))

divider()
