print("let's cook")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
    def __str__(self):
        return (f"book name: {self.title}, written by: {self.author}")
    
    def check_out(self):
        if self.is_checked_out == False:
            self.is_checked_out = True
            print(f"Enjoy your book!")
        else: print(f'Sorry, this book is already taken.')
    
    def return_book(self):
        if self.is_checked_out == True:
            self.is_checked_out = False
            print(f"Thanks for returning")


class digitalBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title,author)
        self.file_size = file_size
    
    def __str__(self):
        super().__str__()
        return (f"book name: {self.title}, written by: {self.author}, size: {self.file_size} ")

The_great_gatsby = digitalBook("The Great Gatsby","F. Scott Fitzgerald", 2)
print(The_great_gatsby)
(The_great_gatsby.check_out())


The_great_gatsby = Book("The Great Gatsby","F. Scott Fitzgerald")
print(The_great_gatsby)
(The_great_gatsby.check_out())