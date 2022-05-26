## CLASSES
## LIBRARY MANAGEMENT SYSTEM
#1_ CLASSES
#2_ FUNCTIONS
#3_ LISTS
#4_ LOOPS
##class mericlass:
##    def __init__(self,firstnme,lastnme,paisa):
##        self.firstnme = firstnme
##        self.lastnme = lastnme
##        self.paisa = paisa
##    def display(self):
##        print(f"first name: {self.firstnme} \n last name: {self.lastnme} \n paisa milta hai: {self.paisa}")
##main1 = mericlass("huzaifa","Ghori",10000)
##main1.display()
##print(main1.firstnme)
##  


## LIBRARY MANAGEMENT SYSTEM

class library:
    def __init__(self,list_of_books):
        self.available_books = list_of_books
        self.lended_books = []

    def display(self):
        print("Available books in library are: ")
        for book in self.available_books:
            print(book)
        print("Lended Books Are:")
        for book in self.lended_books:
            print(book)
    def lend_book(self,requested_book):
        if requested_book in self.available_books:
            print(f"You have now borrowed the book {requested_book}")
            self.lended_books.append(self.available_books.pop(self.available_books.index(requested_book)))
            print(self.lended_books)
            
        else:
            print("We dont have that book")


    def add_book(self,book):
        if book in self.available_books:
            print("We already have this book")
        elif book in self.lended_books:
            print("Thank you for the book")
            self.available_books.append(self.lended_books.pop(self.lended_books.index(book)))
        else:
            userAgree = input(f"We dont have this book in lended records.. Are you a contributor?: \n 'Y' for YES \n 'N' for NO \n Enter: ")
            if userAgree == "Y":
                print("Thank you for the book")
                self.available_books.append(book)             
            else:
                Print("Ok Bye!")
class customer:
    def requested_book(self):
        self.book = input("Enter the name of the book you want:")
        return self.book
    def return_book(self):
        self.book = input("Enter the name of the book you want to return:")
        return self.book

library = library(["Harry Potter","Star Wars","Avengers","Biology"])

customer = customer()

while True:
    print("---------------------------------------")    
    print("Enter 1 to display books")
    print("Enter 2 to lend a book")
    print("Enter 3 to return a book")
    print("Enter 4 to quit")
    print("---------------------------------------")
    user_choice = int(input("Enter: "))
    if user_choice == 1:
        library.display()
    elif user_choice == 2:
        requested_book = customer.requested_book()
        library.lend_book(requested_book)
    elif user_choice == 3:
        returned_book = customer.return_book()
        library.add_book(returned_book)
    elif user_choice == 4:
        break
