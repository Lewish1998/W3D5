class Book():
    
    def __init__(self, title, description, author, genre, book_num):
        self.title = title
        self.description = description
        self.author = author
        self.genre = genre
        self.checked_out = False
        self.book_num = book_num