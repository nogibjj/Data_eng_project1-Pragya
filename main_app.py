from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from hello_dask_books import get_book
from hello_dask_books import get_author_rating

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Let's find the author of the book by using  the url/authors/{book_name} and the average rating of all authors by using the url/rating/{author_name}"}
    
@app.get("/authors/{book_name}")
async def q_authors(book_name:str):
    answer = get_book(book_name) 
    return {"authors": answer}

@app.get("/rating/{author_name}")
async def query(author_name:str):
    result = get_author_rating(author_name)
    return {"answer": result}



if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
