class Product:
    def __init__(self, name="", price=0.0, discount_percent=0):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent

    def get_discount_amount(self):
        return self.price * self.discount_percent / 100

    def get_discount_price(self):
        return self.price - self.get_discount_amount()

    def get_description(self):
        return self.name


class Book(Product):
    def __init__(self, name="", price=0.0, discount_percent=0, author=""):
        Product.__init__(self, name, price, discount_percent)
        self.author = author

    def get_description(self):
        return Product.get_description(self) + " by " + self.author


class Movie(Product):
    def __init__(self, name="", price=0.0, discount_percent=0, year=0):
        Product.__init__(self, name, price, discount_percent)
        self.year = year

    def get_description(self):
        return Product.get_description(self) + " (" + str(self.year) + ")"
