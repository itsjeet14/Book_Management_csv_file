import csv

class Book_Management:
    def saveBook(self, Books):
        with open("SaveBook.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id','name','price'])
            for book in Books:
                writer.writerow([book['id'],book['name'],book['price']])
        
    def fetchBook(self):
        try:
            with open("SaveBook.csv", 'r') as file:
                reader = csv.DictReader(file)
                book = []
                for row in reader:
                    book.append(row)
                return book

        except FileNotFoundError:
            return []
    
    def book_id_generator(self, data):
        book_ids = set()
        for book in data:
            book_ids.add(int(book['id']))
        if book_ids:
            book_id = max(book_ids) + 1
        else:
            book_id = 1
        return book_id
    
    def addBook(self, books):
        try:
            bookID = self.book_id_generator(books)
            name = input("Enter Name: ")
            price = float(input("Enter Price: "))

            book = {'id':bookID, 'name': name, 'price': price}
            books.append(book)
            self.saveBook(books)

            print(f"Book Detaiils Saved Successfully with BookID: {bookID}")
        except ValueError:
            print("Invalid Price!!")

    def viewBook(self):
        books = self.fetchBook()
        if len(books) < 1:
            print("Library is empty!!")
        else: 
            for book in books:
                print(book)
    
    def deleteBookByID(self, books):
        try:
            book_id = (input("Enter BookID: "))
            assumed = False
            for book in books:
                if book['id'] == book_id:
                    books.remove(book)
                    self.saveBook(books)
                    print("Book Deleted Successfully with BookID: ",book_id)
                    assumed = True    
            if not assumed:        
                print("Book Not Found!!")            
                    
        except ValueError:
            print("Invalid BookID")
    
    def updateByBookID(self, books):
        try:
            bookID = int(input("Enter BookID: "))
            for book in books:
                if book['id'] == bookID:
                    name = input("Enter New Name: ")
                    price = float(input("Entre New Price: "))

                    book['name'] = name
                    book['price'] = price

                    
                    self.saveBook(books)
                    print("Book Updated Successfully!!")
                    return
                print("BookID Not Found!!")
        except ValueError:
            print("Invalid input!!")

    def searchBookByID(self):
        try:
            books = self.fetchBook()
            book_id = (input("Enter BookID: "))
            assumed = False
            for book in books:
                if book['id'] == book_id:
                    print(book)
                    assumed = True
            if not assumed:
                print("Book Not Found!!")
            
        except ValueError:
            print("Invalid Input!!")
    
    def searchBookByName(self):
        naam = input("Enter Name: ")
        books = self.fetchBook()
        assumed = False
        for book in books:
            if book['name'] == naam:
                print(book)
                assumed = True
        if not assumed:
            print("No Book Available by this name")
        