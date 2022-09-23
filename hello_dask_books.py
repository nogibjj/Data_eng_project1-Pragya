from dblib.books import dask_query_books

ddf = dask_query_books()
#print("One record from the enron dataset without compute:")
#print(ddf["title"][0])
#print("One record from the enron dataset with compute:")
#print(ddf["title"][0].compute())

)  




def get_book(title:str):
    x =ddf[ddf["title"] == title]["authors"].compute()
    return x.head(n=1)




def get_author_rating(author_n:str):
    author_r = ddf.groupby('authors')['average_rating'].mean().reset_index()
    author_rating= author_r[author_r['authors'] == author_n].compute()
    return author_rating.head(n=1)

