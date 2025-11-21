from typing import Literal

def divider():
  print("--------------------------------")


class SayHello:
  def __init__(self, name):
    self.name = name
  def say_hello(self):
    print(f"Hello, {self.name}!")

class SayGoodbye:
  def __init__(self, full_name: str, age: int):
    self.full_name = full_name
    self.age = age
  def say_goodbye(self):
    print(f"Goodbye, {self.full_name}! You are {self.age} years old.")


say_hello = SayHello("Mohammad")
say_hello.say_hello()

divider()

say_goodbye = SayGoodbye("Mohammad Garmabi", 31)
print(say_goodbye.full_name)
print(say_goodbye.age)
say_goodbye.say_goodbye()

divider()

class Employee:
  def __init__(self, **kwargs: dict[Literal['name', 'position', 'salary', 'period'], str | int]):
    self.name = kwargs["name"]
    self.position = kwargs["position"]
    self.salary = kwargs["salary"]
    self.period = kwargs["period"]
  def get_info(self) -> str:
    return f"My name is {self.name}, I am a {self.position} and I am working for {self.period} years."
  def pay_salary(self)-> str:
    salary = self.salary * self.period
    return f"I am getting {salary} dollars per month."
  def say_congratulations(self)-> str:
    return f"Congratulations, {self.name}! You are a {self.position} and you are working for {self.period} years."


employee_info = {
  "name": "Mohammad",
  "position": "Software Engineer",
  "salary": 100000,
  "period": 5
}

kwargs = employee_info

employee = Employee(**kwargs)
print(employee.get_info())
print(employee.pay_salary())
print(employee.say_congratulations())

divider()

class BookApi:
  books = {}

  def __init__(self, title: str, author: str, price: int):
    self.title = title
    self.author = author
    self.price = price
    BookApi.books[self.title] = {"author": self.author, "price": self.price}

  def get_books(self) -> dict:
    return BookApi.books

  @staticmethod
  def add_book(title: str, author: str, price: int) -> dict:
    new_book = BookApi(title, author, price)
    return new_book.get_books()

book_api = BookApi("Python", "Mohammad", 20000)
print(book_api.get_books())
print(book_api.add_book("Python2", "Mohammad2", 20000))

divider()

