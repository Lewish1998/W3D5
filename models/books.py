from models.book_class import *

dune = Book(
    title='Dune',
    description='Dune is a 1965 epic science fiction novel by American author Frank Herbert, originally published as two separate serials in Analog magazine.',
    author='Frank Herbert',
    genre='Fantasy',
    book_num=0)

the_hobbit = Book(
    title='The Hobbit',
    description='The Hobbit is the unforgettable story of Bilbo, a peace-loving hobbit, who embarks on a strange and magical adventure. A timeless classic.',
    author='J.R.R. Tolkien',
    genre='Fantasy',
    book_num=1
)


book_list = [dune, the_hobbit]

def add_book(book):
    book_list.append(book)

def remove_book(index):
    book_list.remove(index)

def check_out(book):
    book.checked_out = True
    
def check_in(book):
    book.checked_out = False

def delete_me(book):
    book.delete = True
    if book.delete:
        book_list.remove(book)
