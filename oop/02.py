def divider():
  print("--------------------------------")


class Book:
  def __init__(self, name: str, pages: int):
    self.name = name
    self.pages = pages
  def open(self):
    return f"The book {self.name} is opened and has {self.pages} pages"
  

book = Book("Python", 100)
print(book.open())

divider()


class SportBook(Book):
  def __init__(self, name: str, pages: int, sport: str = "Football"):
    super().__init__(name, pages)
    self.sport = sport
  def open(self):
    return f"The sport book {self.name} is opened and has {self.pages} pages and is about {self.sport}"
  
sport_book = SportBook("Python", 100)
print(sport_book.open())

divider()

class Mohammad:
  def __init__(self, name: str, learning_name: str, period_time: int):
    self.name = name
    self.learning_name = learning_name
    self.period_time = period_time
  def learn(self):
    return f"My name is {self.name} and I am learning {self.learning_name} for {self.period_time} hours"
  
mohammad = Mohammad("Mohammad", "Python", 12)
print(mohammad.learn())

divider()

class Reyhane(Mohammad):
  def __init__(self, name: str, learning_name: str, period_time: int):
    self.name = name
    super().__init__(name ,learning_name, period_time)

  def learn(self):
    return f"My name is {self.name} and I am learning {self.learning_name} for {self.period_time} hours"

reyhane = Reyhane("Reyhaneh", "Product management", 4)
print(reyhane.learn())
print(reyhane.learn())

divider()

for learn in [mohammad, reyhane]:
  print(learn.learn())