class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
 
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Price: ${self.price:.2f}")
 
    def apply_discount(self, percentage):
        discount = self.price * percentage
        self.price -= discount
        print(f"Discount applied. New price: ${self.price:.2f}")
my_book = Book("To Kill a twisted games", "anna huang", 2023, 17.99)
my_book.display_info()
my_book.apply_discount(0.1)
my_book.display_info()