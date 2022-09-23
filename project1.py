# importing the required libraries.
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
import dask.dataframe as dd
from dask.distributed import Client


# importing the data.
books = pd.read_csv("books.csv", error_bad_lines=False)
books.head(5)

# set "bookID" as index
books.set_index("bookID", inplace=True)

## parse "publication_date"
books["publication_date"] = pd.to_datetime(
    books["publication_date"], format="%m/%d/%Y", errors="coerce"
)

print("The dataset has {} rows and {} columns".format(books.shape[0], books.shape[1]))
books_rated_5 = books[books["average_rating"] == 5.0].loc[
    :, ["title", "authors", "average_rating", "language_code"]
]
print("{} books have 5 as their average ratings".format(books_rated_5.shape[0]))


books_rated_1 = books[books["average_rating"] == 1.0].loc[
    :, ["title", "authors", "average_rating", "language_code"]
]
print("{} books have 1 as their average ratings".format(books_rated_1.shape[0]))
books_rated_1
books_most_rated = books.sort_values("ratings_count", ascending=False)[:10].loc[
    :, ["title", "ratings_count"]
]


plt.figure(figsize=(15, 6))
sns.set_theme(style="darkgrid")
a = sns.barplot(
    x=books_most_rated["ratings_count"], y=books_most_rated["title"], palette="husl"
)
plt.title("Top 10 Books with Highest Rating Count")
plt.xlabel("Rating Count")
plt.ylabel("Title")
plt.show()


# Top 10 Books with Highest Reviews Count

books_most_reviewed = books.sort_values("text_reviews_count", ascending=False)[:10]
books_most_reviewed

plt.figure(figsize=(15, 6))
sns.set_theme(style="dark")
sns.barplot(
    x=books_most_reviewed["text_reviews_count"],
    y=books_most_reviewed["title"],
    palette="pastel",
)
plt.title("Top 10 Books with Highest Reviews Count")
plt.xlabel("Reviews Count")
plt.ylabel("Title")
plt.show()


# Top 10 Authors with Most Books Published

authors_with_most_books = (
    books.groupby("authors").size().sort_values(ascending=False)[:10]
)

plt.figure(figsize=(15, 6))
authors_with_most_books.plot.barh(label="books count", legend=True)
