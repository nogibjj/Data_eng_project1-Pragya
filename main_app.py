from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from hello_dask_books import get_book
from hello_dask_books import get_author_rating

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Let's find the author of the book by using  the url/authors/{book_name} and the average rating of all authors by using the url/rating/{author_name}"}


#@app.get("/add/{num1}/{num2}")
#async def add(num1: int, num2: int):
    #"""Add two numbers together"""

   # total = num1 + num2
    #return {"total": total}


#@app.get("/charts/{title}")
#async def read_item(title):
 #   return {"title": title}


# @app.get("/artist/{a}")
# async def q_artist(a:str):
  #  answer = get_artist(a) 
   # return {"artist": answer}

@app.get("/authors/{book_name}")
async def q_authors(book_name:str):
    answer = get_book(book_name) 
    return {"authors": answer}

@app.get("/rating/{author_name}")
async def query(author_name:str):
    result = get_author_rating(author_name)
    return {"answer": result}

#@app.get("/region/{c_name}")
#async def query(c_name:str):
  #  result = get_country(c_name)
  #  return {"answer": result}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
