class LibraryBook:
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("year:", self.year)
        print("Copies:", self.copies)
        
        

    def issue(self):
        if self.copies > 0:
            self.copies -= 1
            print("Book Issued")
        else:
            print("Not Available")

    def return_book(self):
        self.copies += 1
        print("Book Returned")


b = LibraryBook("Python", "ABC", 2023, 1)
b.display()
b.issue()
b.display()
b.return_book()
b.display()
