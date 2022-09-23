from dblib.books import dask_query_books

ddf = dask_query_books()
#print("One record from the enron dataset without compute:")
#print(ddf["title"][0])
#print("One record from the enron dataset with compute:")
#print(ddf["title"][0].compute())

#print(ddf["title"][0:10].compute())  

#print(len(ddf['region'].unique()))
#print(ddf[(ddf.title == 'Safari') & (ddf.region == 'Chile')].compute())

#x =ddf[ddf["title"] == "Safari"]["artist"].compute()
#print(x.head(n=1))

#def get_book(title:str):
    #x =ddf[ddf["title"] == title]["artist"].compute()
   # return x.head(n=1)

def get_book(title:str):
    x =ddf[ddf["title"] == title]["authors"].compute()
    return x.head(n=1)
#print(get_artist("Safari"))

#def get_artist(name):
   # x = ddf[["title" == name]].compute()
   # artist_name = x["artist"]
  #  return x.head(n=1)

#print(get_artist("Safari"))

#x =ddf[ddf["title"] == title]["artist"].compute()
#return x.head(n=1)


#print(ddf[ddf.chart == top200])
# streams = ddf.groupby('region')['streams'].sum().reset_index()
# streams['percent_streams'] = streams['streams']/streams['streams'].sum()
#streams['region'] = streams.apply(lambda x: x['region'] if x['percent_streams'] >= .01 else 'Other', axis=1, meta=(None, 'object'))
#streams = streams.groupby('region')['percent_streams'].sum().reset_index().round(3).sort_values(by='percent_streams')
#print(streams.compute())

def get_author_rating(author_n:str):
    author_r = ddf.groupby('authors')['average_rating'].mean().reset_index()
    author_rating= author_r[author_r['authors'] == author_n].compute()
    return author_rating.head(n=1)


#def get_country(country:str):
 #   country_name = streams[streams['region'] == country].compute()
  #  return country_name.head(n=1)

