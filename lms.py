# LIBRARY MANAGEMENT SYSTEM 

class Library:

    # condition-1 : Creating constructor and destructor methods
    def __init__(self): # cunstructor
        self.db = open("books.txt", "a+", encoding="utf-8") # "a+": It performs both read and write operations

    def __del__(self): # destructor
        self.db.close()


    # condition-2 : Add the "List Books", "Add book" and "Remove Book" methods
    def List_Books(self):
        self.db.seek(0)  # Move the cursor to the beginning of the books.txt
        books = self.db.read().splitlines()
        space = " " * 25
        stars = "*" * 60 
        print(f"\n{space} \033[1m BOOK  LIST{space} \033[0m") # to center the title
        print(f"\033[1m {stars} \033[0m")
        if len(books) != 0:
            for i, book in enumerate(books):  # We get index and elements with enumerate
                book = book.split(",")  # separates items after a comma
                print(f" *Book-{i+1}: {book[0].upper()}, Author: {book[1].upper()}")
            print(f"\033[1m {stars} \033[0m")
            print(f" There are a total of \033[1m'{len(books)}'\033[0m books in the library.\n")
        else:
            print("\n There are no registered books in the library yet.\n")

    def Add_Book(self):
        space = " " * 26
        stars = "*" * 60 
        print(f"\n{space}\033[1m ADD BOOK \033[0m{space}") # to center the title
        print(f"\033[1m {stars} \033[0m")
        
        while True:
            book_title = input("\033[1m *Enter book title: \033[0m")
            if book_title.strip() == "b" or book_title == "4":
                print(" \n Returning to the menu...")
                return
            elif not book_title.strip():  # Check if book_title is empty or contains only whitespace
                print(" Invalid input! Please enter a valid book title.")
            else:
                break

        while True:
            author = input("\033[1m *Enter book author: \033[0m")
            if author.strip() == "b" or author == "4":
                print(" \n Returning to the menu...")
                return
            elif not author.strip():  # Check if author is empty or contains only whitespace
                print(" Invalid input! Please enter a valid author.")
            elif any(char.isdigit() for char in author):  # Check if author contains any digits
                print(" Invalid input! Author name must not contain digits.")
            else:
                break

        while True:
            release_year = input("\033[1m *Enter release year (between 1-9999 in YYYY): \033[0m")
            if release_year.strip() == "b" or release_year == "4":
                print(" \n Returning to the menu...")
                return
            elif not release_year.strip():  # Check if release_year is empty or contains only whitespace
                print(" Invalid input! Please enter a valid release year.")
            elif not (release_year.isdigit() and len(release_year) == 4 and 1 <= int(release_year) <= 9999):
                print(" Invalid input! Release year must be a numeric value between 1-9999 in 'YYYY' format.")
            else:
                break

        while True:
            num_pages = input("\033[1m *Enter number of pages: \033[0m")
            if num_pages.strip() == "b" or num_pages == "4":
                print(" \n Returning to the menu...")
                return
            elif not num_pages.strip():  # Check if num_pages is empty or contains only whitespace
                print(" Invalid input! Please enter a valid number of pages.")
            elif not num_pages.isdigit():
                print(" Invalid input! Please enter a numeric value for the number of pages.")
            else:
                break

        book = f"{book_title},{author},{release_year},{num_pages}\n"
        self.db.write(book)
        self.db.seek(0)
        print(f"\033[1m {stars} \033[0m")
        print(f" Book \033[1m'{book_title.upper()}'\033[0m added successfully.")



    def Remove_Book(self):
        space = " " * 24
        stars = "*" * 60  
        print(f"\n{space} \033[1m REMOVE  BOOK \033[0m {space}")  # to center the title
        print(f"\033[1m {stars} \033[0m")

        while True:
            title_to_remove = input("\033[1m *Enter the title of the book to remove:\033[0m ").strip()
            if title_to_remove.strip() == "b" or title_to_remove == "4":
                print(" \n Returning to the menu...")
                return
            elif not title_to_remove:  # Check if title_to_remove is empty or contains only whitespace
                print(" Invalid input! Please enter a valid title to remove.")
                continue
            found = False
            with open("books.txt", "r+", encoding="utf-8") as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    if title_to_remove.lower() not in line.lower():  # for case sensitivity
                        file.write(line)
                    else:
                        found = True
                file.truncate()
            if not found:
                print(" The specified book does not exist. Please enter a valid title to remove.")
            else:
                print(f"\033[1m {stars} \033[0m")
                print(f" Book \033[1m'{title_to_remove.upper()}'\033[0m removed successfully. \033[0m")
                break


# # condition-3 : Creating an object named "lib" with "Library" class
lib = Library()


# condition-4 : Create a menu to interact with the “lib” object 
while True:
    space = " " * 28
    stars = "*" * 60  # len(space*2) + len("MENU")
    print(f"""{space} \033[1m MENU \033[0m {space}
    \n\033[1m {stars} \033[0m
    \n \033[1m(1)\033[0m List Books
    \n \033[1m(2)\033[0m Add Book
    \n \033[1m(3)\033[0m Remove Book
    \n \033[1m(4)\033[0m Back to Menu (or b)
    \n \033[1m(5)\033[0m Exit (or q)
    """)
    choice = input(" \033[1mEnter your choice (1/2/3/4/5):\033[0m ")

    if choice == "1":
        lib.List_Books()
    elif choice == "2":
        lib.Add_Book()
    elif choice == "3":
        lib.Remove_Book()
    elif choice.lower() == "b" or choice == "4":
        print(" \n Returning to the menu...")
        continue
    elif choice.lower() == "q" or choice == "5":
        print(" \n Exiting...\n")
        del lib
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")