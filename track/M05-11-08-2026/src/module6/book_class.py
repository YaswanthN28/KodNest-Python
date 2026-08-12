class Book:
    def __init__(self, title, author, price):
        # Store the received values inside the object
        self.title=title
        self.author=author
        self.price=price

title = input("Enter the title: ").strip()
author = input("Enter the author: ").strip()
price = int(input("Enter the price: "))

book = Book(title, author, price)

print("BOOK DETAILS")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Price: {book.price}")