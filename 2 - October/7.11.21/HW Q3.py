# HW Q3 - *etgar
# *etgar: create a list of 3 three books.
# now create a dictionary which contains these 3 books where the key is the book-title
# and the value is the book instance. now input a string from the user (the title)
# and try to pop the book out of the dictionary using the title as the key
# (and print the book.__dict__ you just poped)

# didn't manage to solve


class Book:
    pass

def book_func(title, author,genre, year_of_publish, no_of_pages):
    book_func = Book()
    book_func.title = title
    book_func.author = author
    book_func.genre = genre
    book_func.year_of_publish = year_of_publish
    book_func.no_of_pages = no_of_pages
    return book_func
book1 = book_func('the first book', 'the first author', 'action', 2010, 250)
book2 = book_func('the second book', 'the second author', 'drama', 2020, 300)
book3 = book_func('the third book', 'the first author', 'comedy', 2015, 400)

list1 = [book1, book2, book3]

dict1 = {book1: 1, book2: 2, book3: 3}

string1 = input('enter a book title: ')
print(list1.pop(string1))
