from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def display(self):
        print "Title: %s" % (self.title)
        print "Author: %s" % (self.author)
        print "Price: %d" % (self.price)
