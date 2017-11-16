from objects import Product, Book, Movie


def show_products(products):
    print("PRODUCTS")
    for i in range(len(products)):
        product = products[i]
        print(str(i + 1) + ".", product.get_description())
    print()


def show_product(product):
    print("PRODUCT DATA")
    print("Name:            ", product.name)
    if isinstance(product, Book):
        print("Author:          ", product.author)
    if isinstance(product, Movie):
        print("Year:            ", product.year)
    print("Discount percent: {:d}%".format(product.discount_percent))
    print("Discount amount:  {:.2f}".format(product.get_discount_amount()))
    print("Discount price:   {:.2f}".format(product.get_discount_price()))
    print()


def main():
    print("The Product Viewer program")
    print()

    # a tuple of Product objects
    products = (Product("Swingline Stapler, 747, Business, Desktop, Rio Red (74736)", 11.40, 30),
                Book("Originals: How Non-Conformists Move the World", 11.55, 20, "Adam Grant"),
                Movie("Guardians of the Galaxy Vol. 2 Blu-Ray", 24.95, 25, 2017))
    show_products(products)

    while True:
        number = int(input("Enter product number: "))
        print()

        product = products[number - 1]
        show_product(product)

        choice = input("Continue? (y/n): ")
        print()
        if choice != "y":
            print("Bye!")
            break


if __name__ == "__main__":
    main()
