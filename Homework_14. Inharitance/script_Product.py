class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self,name, price,quantity, author):
        super().__init__(name, price, quantity)
        self.author = author


    def read(self):
        print(f"The author of the book is '{self.name}' is {self.author}. It costs 
              {self.price}. Currently, we have {self.quantity} copies of it.")