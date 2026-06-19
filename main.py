from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel
from typing import Optional
<<<<<<< HEAD
import psycopg2
from psycopg2.extras import RealDictCursor
import time

# book_db = {
#      1:{"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "price": 14.99},
#      2:{"id": 2, "title": "1984", "author": "George Orwell", "price": 9.99},
# }
=======

book_db = {
     1:{"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "price": 14.99},
     2:{"id": 2, "title": "1984", "author": "George Orwell", "price": 9.99},
}
>>>>>>> 1ac655cc4595c3a1d5e81fd2a354272dc22cd59c



class Book_create(BaseModel):
    title:str
    author:str
<<<<<<< HEAD
    price:int
class Book_update(BaseModel):
    title:Optional[str]=None
    author:Optional[str]=None
    price:Optional[int]=None

app=FastAPI()
while True:
    try:
        conn=psycopg2.connect(host='localhost',database='book store',user='postgres',password='23001616',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database connected successful")
        break
    except Exception as error:
        print("Connecting failed")
        print("Error",error)
        time.sleep(2)

@app.post("/books",status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Book_create):
    cursor.execute("""INSERT INTO public."book-store" (title,author,price) VALUES(%s, %s ,%s) RETURNING * """,(book_data.title,book_data.author,book_data.price))
    new_book=cursor.fetchone()
    conn.commit()
    # new_id=max(book_db.keys(),default=0)+1
    # new_book=book_data.model_dump()
    # new_book["id"]=new_id
    # book_db[new_id]=new_book
    return new_book
@app.get("/books")
async def get_all_books(author:Optional[str]=None):
    cursor.execute("""SELECT * FROM public."book-store" """)
    books=cursor.fetchall()
    # if author:
    #     filtered_books=[
    #         book for book in book_db.values()
    #         if author.lower() in book["author"].lower()   
    #     ]
    #     return filtered_books
    return {"Data":books}
@app.get("/books/{book_id}")
async def get_books(book_id: int):
    cursor.execute("""SELECT * FROM public."book-store" WHERE id=%s""",(book_id,))
    book_id=cursor.fetchone()

    if not book_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
    return book_id
@app.put("/books/{book_id}")
async def update_books(book_id:int,book_data:Book_update):
    cursor.execute("""update public."book-store" set title=%s, author=%s,price=%s where id=%s RETURNING * """,(book_data.title,book_data.author,book_data.price,book_id))
    book=cursor.fetchone()
    conn.commit()
    if book ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
    # # stored_book =book_db[book_id]
    # updeted_dict=book_data.model_dump(exclude_unset=True)
    # for key,value in updeted_dict.items():
    #     stored_book[key]=value
    # book_db[book_id]=stored_book
    return book
@app.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_books(book_id:int):
    cursor.execute("""DELETE FROM public."book-store" WHERE id=%s RETURNING * """,str(book_id))
    deleted_book=cursor.fetchone()
    conn.commit()

    if deleted_book ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"book with id {book_id} not found")
    
    return deleted_book
=======
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
>>>>>>> 1ac655cc4595c3a1d5e81fd2a354272dc22cd59c


