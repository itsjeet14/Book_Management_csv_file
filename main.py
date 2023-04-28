from operation import Book_Management
import sys

class Main:
    def execution(self, choice):
        if choice == 1:
            print("-----Add Book-----")
            obj_book_management.addBook(obj_fetchBook)
        
        if choice == 2:
            print("-----View Book-----")
            obj_book_management.viewBook()
        
        if choice == 3:
            print("-----Delete Book-----")
            obj_book_management.deleteBookByID(obj_fetchBook)
        
        if choice == 4:
            print("-----Update Book List-----")
            obj_book_management.updateByBookID(obj_fetchBook)
        
        if choice == 5:
            print("-----Search Book-----")
            obj_book_management.searchBookByID()
        
        if choice == 6:
            print("-----Search Book By Name-----")
            obj_book_management.searchBookByName()
        
        
        if choice == 0:
            print("Thank your!!")
            sys.exit()

if __name__=="__main__":
    obj_main = Main()
    obj_book_management = Book_Management()
    obj_fetchBook = obj_book_management.fetchBook()
    while True:
        try:
            choice = int(input("Enter \n1. Add Book \n2. View Book List \n3. Delete Book Using BookID \n4. Updata Book by BookID \n5. Search Book by BookID \n6. Search Book by Book Name \n0. Exit \n"))
            obj_main.execution(choice)
        except ValueError:
            print("Invalid Choice!!")