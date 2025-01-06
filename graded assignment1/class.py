class book:

    def __init__(self,name,author):
        self.name = name
        self.author = author
        self.available = True


    def borrow(self):
        if self.available:
            self.available = False
            print(f"you borrowed {self.name} by {self.author}")
        else:
            print(f""
                  f"not available {self.name}")

    def reeturn_book(self):
        self.available = True
        print(f"you returned {self.name}")


my_book = book("python","doe")
my_book.borrow()
my_book.reeturn_book()
print(isinstance(my_book,book))
print(hasattr(my_book,"python"))
print(hasattr(my_book,"name"))

