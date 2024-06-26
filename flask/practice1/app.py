from flask import Flask, jsonify, abort, request


# data
books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]



app = Flask(__name__)


# get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})



# read single book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id']==book_id),None)
    if book is None:
        abort(404)
    return jsonify(book)


# create a new book
@app.route('/books', methods=['POST'])
def create_book():
    if not request.json or not request.json['title']:
        abort(400)
    new_book = {
        "id": books[-1]['id']+1 if books else 1,
        "title" : request.json['title'],
        "author": request.json.get("author","")
    }
    books.append(new_book)
    return jsonify(new_book), 201


# Update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = ((book for book in books if book['id']==book_id), None)
    if book is None:
        abort(404)
    if not request.json:
        abort(400)
    book['title'] = request.json.get("title", book["title"])
    book['author'] = request.json.get("author", book['author'])
    return jsonify(book)


# Delete a book
@app.route("/books/<int:book_id>", methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book['id']==book_id), None)
    if book is None:
        abort(404)
    books.remove(book)
    return jsonify({"result": True})



if __name__ == "__main__":
    app.run(debug=True)