from RestFul_API.library.extension import db
from RestFul_API.library.libraryma import ma, BookSchema
from RestFul_API.library.models import Books
import json
from flask import request, jsonify

book_schema = BookSchema()
books_schema = BookSchema(many=True)


# Add book
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
            return jsonify({"message": "Add success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add book!"}), 400
    else:
        return jsonify({"message": "Request error"}), 400

# Get book by ID
def get_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        return book_schema.jsonify(book)
    else:
        return jsonify({"message": "Not found book!"}), 404


# Get all books
def get_all_books_service():
    books = Books.query.all()
    if books:
        return books_schema.jsonify(books)
    else:
        return jsonify({"message": "Not found books!"}), 404


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
                return jsonify({"message": "Book updated!"}), 200
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not update book!"}), 400
    else:
        return jsonify({"message": "Not found books!"}), 404


# Delete book by id
def delete_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            return jsonify({"message": "Book deleted!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete book!"}), 400

    else:
        return jsonify({"message": "Not found books!"}), 404
