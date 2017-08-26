# -------------------------------------
# Book List Program
# -------------------------------------


def display_menu():
    print("MENU")
    print("list - List all books")
    print("add  - Add a book")
    print("del  - Delete a book")
    print("exit - Exit program")
    print()


def list(book_list):
    i = 1
    for book in book_list:
        print(str(i) + ". " + book)
        i += 1
    print()


def add(book_list):
    book = input("Name: ")
    book_list.append(book)
    print(book + " was added.\n")


def delete(book_list):
    number = int(input("Number: "))
    if number < 1 or number > len(book_list):
        print("Invalid book number.\n")
    else:
        book = book_list.pop(number-1)
        print(book + " was deleted.\n")


def main():
    book_list = [
        "HTML5 and CSS3 Web Development",
        "Programming Java",
        "Programming Python",
        "MySQL Database Programming",
        "JavaScript Frameworks"
    ]

    display_menu()

    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list(book_list)
        elif command.lower() == "add":
            add(book_list)
        elif command.lower() == "del":
            delete(book_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")

    print("Exit.")


if __name__ == "__main__":
    main()
