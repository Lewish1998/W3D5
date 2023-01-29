from app import app
from flask import render_template, request
from models.book_class import Book
from models.books import book_list, add_book, remove_book



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view-all')
def index():
    return render_template('view.html', book_list=book_list)

@app.route('/add-book')
def add():
    return render_template('add.html', book_list=book_list)

@app.route('/add-book', methods=['POST'])
def add_function():
    title = request.form['title']
    description = request.form['description']
    author = request.form['author']
    genre = request.form['genre']
    new_book = Book(title, description, author, genre)
    add_book(new_book)
    return render_template('add.html', book_list=book_list)

@app.route('/view-book/<int:index>')
def single_book(index):
    return render_template('single.html', book_list=book_list[index])

@app.route('/delete-book/<int:index>')
def delete(index):
    remove_book(book_list[index])
    return render_template('view.html', book_list=book_list)


# @app.route('/error')

