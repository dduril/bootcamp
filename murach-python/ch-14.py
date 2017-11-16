# -------------------------------------
# Chapter 14 Code Examples
#   OOP - Classes
# -------------------------------------


class Product:
    def __init__(self, name, published, pages, price, discount_percent):
        self.name = name
        self.published = published
        self.pages = pages
        self.price = price
        self.discount_percent = discount_percent

    def get_discount_amount(self):
        return self.price * self.discount_percent / 100

    def get_discount_price(self):
        return self.price - self.get_discount_amount()


def show_products(products):
    print("PRODUCTS")
    for i in range(len(products)):
        product = products[i]
        print(str(i + 1) + ". " + product.name)
    print()


def show_product(product):
    print("PRODUCT DATA")
    print("Name:             {:s}".format(product.name))
    print("Published date:   {:d}".format(product.published))
    print("Number of pages:  {:d}".format(product.pages))
    print("Price:            {:.2f}".format(product.price))
    print("Discount percent: {:d}%".format(product.discount_percent))
    print("Discount amount:  {:.2f}".format(product.get_discount_amount()))
    print("Discount price:   {:.2f}".format(product.get_discount_price()))
    print()


def main():
    print("The Product Viewer program")
    print()

    # a tuple of Product objects
    products = (Product("AngularJS Development", 2015, 392, 25.00, 25),
                Product("HTML5/CSS3 Cookbook", 2017, 498, 22.50, 15),
                Product("JavaScript and jQuery Frameworks", 2018, 684, 18.45, 20))
    show_products(products)

    while True:
        number = int(input("Enter product number: "))
        print()

        product = products[number - 1]
        show_product(product)

        choice = input("View another product? (y/n): ")
        print()
        if choice != "y":
            print("Bye!")
            break

if __name__ == "__main__":
    main()