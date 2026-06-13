from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
from typing import Optional

book_db = {
     1:{"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "price": 14.99},
     2:{"id": 2, "title": "1984", "author": "George Orwell", "price": 9.99},
}



class Book_create(BaseModel):
    title:str
    author:str
    price:float

class Book_update(BaseModel):
    title:Optional[str]=None
    author:Optional[str]=None
    price:Optional[float]=None

app=FastAPI()
@app.post("/",status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Book_create):
    new_id=max(book_db.keys(),default=0)+1
    new_book=book_data.model_dump()
    new_book["id"]=new_id
    book_db[new_id]=new_book
    return new_book
@app.get("/")
async def get_all_books(author:Optional[str]=None):
    if author:
        filtered_books=[
            book for book in book_db.values()
            if author.lower() in book["author"].lower()   
        ]
        return filtered_books
    return list(book_db.values())
@app.get("/books/{book_id}")
async def get_books(book_id: int):
    if book_id not in book_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
    return book_db[book_id]
@app.put("/books/{book_id}")
async def update_books(book_id:int,book_data:Book_update):
    if book_id not in book_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
    stored_book =book_db[book_id]
    updeted_dict=book_data.model_dump(exclude_unset=True)
    for key,value in updeted_dict.items():
        stored_book[key]=value

    book_db[book_id]=stored_book
    return stored_book
@app.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_books(book_id:int):
    if book_id not in book_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"book with id {book_id} not found")
    del book_db[book_id]
    return None


