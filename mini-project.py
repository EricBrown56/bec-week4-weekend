# Your mission is to create a robust system that allows users to browse, borrow, return, and explore a collection of books while demonstrating your proficiency in OOP principles and the use of modules.

import re
import os
books = []
genres = []
authors = []
users = []

def clear():
    '''Method to clear the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

class Book:
    
    def __init__(self, title, author, genre, borrowed = False):
        '''Constructor method to initialize the attributes of the Book class'''
        self.author = author
        self.borrowed = borrowed
        self.title = title
        self.genre = genre

    def get_info(self):
        '''Method to display the book information'''
        print(f"Title: {self.title} Author: {self.author} Genre: {self.genre}")

   
    def borrow_book(self):
        '''Method to borrow a book from the library'''

        if self.borrowed == False:
            self.borrowed = True
            print(f"{self.title} has been borrowed")
        else:
            print(f"{self.title} is already borrowed")

    def return_book(self):
        '''Method to return a book to the library'''
        
        if self.borrowed == True:
            self.borrowed = False
            print(f"{self.title} has been returned")
        else:
            print(f"{self.title} is already returned")

   

books.append(Book("animal_farm", "George Orwell", "Fiction", borrowed=False))
books.append(Book("don_quixote", "Miguel de Cervantes", "Fiction", borrowed=False))
books.append(Book("the_great_gatsby", "F. Scott Fitzgerald", "Fiction", borrowed=False))
books.append(Book("pride_and_prejudice", "Jane Austen", "Fiction", borrowed=False))
books.append(Book("to_kill_a_mockingbird", "Harper Lee", "Fiction", borrowed=False))
books.append(Book("the_catcher_in_the_rye", "J.D. Salinger", "Fiction", borrowed=False))
books.append(Book("nineteen_eighty_four", "George Orwell", "Fiction", borrowed=False))
books.append(Book("the_odyssey", "Homer", "Fiction", borrowed=False))

# Book helper functions

def add_book():
        '''Method to add a book to the library'''
        
        title = input("Enter the title of the book you would like to add: ").capitalize()
        author = input("Enter the author of the book you would like to add: ")
        genre = input("Enter the genre of the book you would like to add: ")
        
        
        new_book = Book(title, author, genre)
        books.append(new_book)
        print(books)
    

def show_books():
        '''Method to display all the books in the library'''
        for b in books:
            print(b.title)
            
        if len(books) <= 0:
                print("There are no books in the library")
        
def search_books():
        '''Method to search for a book in the library'''
        title = input("Enter the title of the book you would like to search for: ")
        for book in books:
            if title == book.title:
                print(f"{book.title} is in the library")
        else:
            print(f"{book.title} is not in the library")
        

  

class User:
    def __init__(self, username, email, password):
        '''Constructor method to initialize the attributes of the User class'''
        self.username = username
        self.email = email
        self.__password = password
        

    def get_password(self):
        '''Method to get the password'''
        return self.__password
    
    def set_password(self, new_password):
        '''Method to set a new password'''
        new_password = input("Enter your new password: ")
        self.__password = new_password
        print("Password changed successfully")
    
    def get_user_info(self):
        '''Method to display the user information'''
        print(f"Name: {self.username} Email: {self.email}")

    
 

def view_users():
    '''Method to view all the users'''
    for u in users:
        print(u.username)

def register():
        '''Method to register a user'''
        try:  
            username = input("Enter your username: ")
            while True:
                email = input("Enter your email: ")
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    print("Please enter a valid email address.")
                    continue
                password = input("Enter your password: ")
                
                print(f"{username} has been registered")
                new_user = User(username, email, password)
                users.append(new_user)
                break
        except ValueError:
            print("value error")
        #except AttributeError:
            #print("attribute error")

def quit():
    '''Method to quit the program'''
    print("Goodbye")
    exit()

def main():
    print(''' Welcome to the Library Management System!

    Main Menu:
    1. Book Operations
    2. User Operations
    3. Quit
    ''')
    while True:    
        try:
            choice = int(input("Please enter the number of what you would like to do from the Main Menu: "))
            if choice == 1:
                print('''Book Operations Menu:
                1. Add a Book
                2. Borrow a Book
                3. Return a Book
                4. Search for a Book
                5. Show all Books
                6. Main Menu
                ''')
                book_choice = int(input("Please enter the number of what you would like to do from Book choices: "))
                if book_choice == 1:
                    #self = input("Enter the title of the book you would like to add: ")
                    add_book()
                    main()
                elif book_choice == 2:
                    show_books()
                    title = input("Enter the title of the book you would like to borrow: ")
                    for book in books:
                        if title == book.title:
                            book.borrow_book()
                        else:
                            print(f"{book.title} is already borrowed")
                    main()
                elif book_choice == 3:
                    show_books()
                    title = input("Enter the title of the book you would like to return: ")
                    for book in books:
                        if title == book.title:
                            book.return_book()
                        else:
                            print(f"{book.title} is already returned")
                    main()
                elif book_choice == 4:
                    search_books()
                    main()
                elif book_choice == 5:
                    show_books()
                    main()
                elif book_choice == 6:
                    main()
            elif choice == 2:
                print('''User Operations Menu:
                1. Register
                2. View Users
                3. Get User Info
                4. Main Menu
                ''')
                user_choice = int(input("Please enter the number of what you would like to do: "))
                if user_choice == 1:
                    register()
                    main()
                elif user_choice == 2:
                    view_users()
                    main()
                elif user_choice == 3:
                    view_users()
                    name = input("Enter the username of the user you would like to get info for: ")
                    for u in users:
                        if name == u.username:
                            u.get_user_info()
                        else:
                            print(f"{u.username} is not a registered user")
                    main()
                elif user_choice == 4:
                    main()
            elif choice == 3:
                quit()
                break
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        except AttributeError:
            print("Attribute error")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

if __name__ == "__main__":
    main()
