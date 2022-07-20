from RestFul_API.library.extension import db
from RestFul_API.library.libraryma import ma, BookSchema
from RestFul_API.library.models import Books
import json
from flask import request, jsonify

book_schema = BookSchema()
books_schema = BookSchema(many=True)


def add_book_service():
    data = request.json
    if data and ('name' in data) and ('page_count' in data) and ('author_id' in data) and ('category_id' in data):
        name = data['name']
        page_count = data['page_count']
        author_id = data['author_id']
        category_id = data['category_id']
        try:
            new_book = Books(name, page_count, author_id, category_id)
            db.session.add(new_book)
            db.session.commit()
            return "Add success"
        except IndentationError:
            db.session.rollback()
            return "Can not add book!"


# Get book by ID
def get_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        return book_schema.jsonify(book)
    else:
        return "Not found book!"


# Get all books
def get_all_books_service():
    books = Books.query.all()
    if books:
        return books_schema.jsonify(books)
    else:
        return "Not found book!"


# Update book by id
def update_book_by_id_service(id):
    book = Books.query.get(id)
    data = request.json
    if book:
        if data and ('name' in data) and ('page_count' in data) and ('author_id' in data) and ('category_id' in data):
            try:
                book.page_count = data["page_count"]
                book.name = data["name"]
                book.author_id = data["author_id"]
                book.category_id = data["category_id"]
                db.session.commit()
                return "Updated Success!"
            except IndentationError:
                db.session.rollback()
                return "Can not update book!"
    else:
        return "Not found book!"


# Delete book by id
def delete_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            return "Book deleted!"
        except IndentationError:
            db.session.rollback()
            return "Can not delete book!"

    else:
        return "Not found book!"
