# How would you sort the following list of dictionaries based on the year of publication of each book, from the earliest to the most recent?

books = [
    {
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel Garcia Marquez",
        "published": "1967",
    },
    {
        "title": "The Book of Kells",
        "author": "Multiple Authors",
        "published": "800",
    },
    {
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "published": "1869",
    },
]


def get_year(book):
    return int(book["published"])


print(sorted(books, key=get_year))
