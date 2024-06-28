from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional


app = FastAPI()

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    
    
books = []

# Example data for illustration
books.extend([
    Book(id=1, title="Book 1", author="Author 1"),
    Book(id=2, title="Book 2", author="Author 2")
])


# custom exception class for book not found
class BookNotFoundException(HTTPException):
    def __init__(self, book_id=None):
        detail = f"book with id: {book_id} not found!"
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)



# retrieve all books
@app.get('/books', response_model=List[Book])
def get_books():
    return books


# get specific book
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise BookNotFoundException(book_id)


# post book
@app.post("/books", response_model=Book)
def create_book(book: Book):
    book.id = len(books)+1
    books.append(book)
    return book


# update book
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: Book):
    for b in books:
        if b.id == book_id:
            b.title = book.title
            b.author = book.author
            return b
        
    raise BookNotFoundException(book_id)

# delete book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    global books
    initial_length = len(books)
    books = [book for book in books if book.id != book_id]
    if initial_length > len(books):
        return {"message": "deleted successfully!"}
    return BookNotFoundException(book_id)