class Book():
    
    def __init__(self, title, description, author, genre):
        self.title = title
        self.description = description
        self.author = author
        self.genre = genre
        self.checked_out = False
