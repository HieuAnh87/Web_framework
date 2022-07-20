from RestFul_API.library.extension import db
from RestFul_API.library.libraryma import BookSchema
from RestFul_API.library.models import Author, Books, Borrows, Category, Students
from flask import request, jsonify
from sqlalchemy.sql import func
import json


def get_borrow_author_cat_service(student_name):
    # Not in specific table, so use db.session
    borrows = db.session.query(Borrows.id, Books.name, Category.name, Author.name).join(Students, Borrows.student_id == Students.id).join(Books, Borrows.book_id == Books.id).join(
        Category, Books.category_id == Category.id).join(Author, Books.author_id == Author.id).filter(func.lower(Students.name) == student_name.lower()).all()
    if borrows:
        return jsonify({f"{student_name} borrowed": borrows}), 200
    else:
        return jsonify({"message": "Not found borrow!"}), 404
