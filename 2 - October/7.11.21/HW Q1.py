# HW Q1
# create a Book class. now, create an instance of your favorite book with the following data fields:
# title, author, genre, year_of_publish, no_of_pages (1) create the instance data using dictionary
# [for example: myBook.__dict__[‘year_of_publish’] = 1961] (2) create the instance data using dot
# [for example: myBook.title = ‘catch 22’] (3) create a method which creates a new books instance and data
# (see the create_Person method we did in lesson)

class Book:
    pass

# The Hundred and One Dalmatians is a book I read long time ago during childhood
# created the instance data using dictionary:
hundred_and_one_d = Book()
hundred_and_one_d.__dict__['title'] = 'The Hundred and One Dalmatians'
hundred_and_one_d.__dict__['author'] = 'Dorothy Gladys "Dodie" Smith'
hundred_and_one_d.__dict__['genre'] = 'adventure'
hundred_and_one_d.__dict__['year_of_publish'] = 1956
hundred_and_one_d.__dict__['no_of_pages'] = 199
# created the instance data using dot:
hundred_and_one_d = Book()
hundred_and_one_d.title = 'The Hundred and One Dalmatians'
hundred_and_one_d.author = 'Dorothy Gladys "Dodie" Smith'
hundred_and_one_d.genre = 'adventure'
hundred_and_one_d.year_of_publish = 1956
hundred_and_one_d.no_of_pages = 199
# created a method which creates a new books instance and data (like person example in class)
def create_hunderd_and_one_d(title, author,genre, year_of_publish, no_of_pages):
    hundred_and_one_d = Book()
    hundred_and_one_d.title = title
    hundred_and_one_d.author = author
    hundred_and_one_d.genre = genre
    hundred_and_one_d.year_of_publish = year_of_publish
    hundred_and_one_d.no_of_pages = no_of_pages
    return hundred_and_one_d
hunderd_and_one_d = create_hunderd_and_one_d('The Hundred and One Dalmatians'\
, 'Dorothy Gladys "Dodie" Smith', 'adventure', 1956, 199)
