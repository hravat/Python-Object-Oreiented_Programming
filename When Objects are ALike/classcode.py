##Class demonstrating basic inheritance

class BookListSearch(list):
    '''
    This class is used to search books
    It demonstrates built ins
    '''

    def search(self, name):
        '''Return all contacts that contain the search value
        in their name.
        '''

        matching_books = []
        for book in self:
            if name in book.bookname:
                matching_books.append(book)
        return matching_books

class Booklist():
    '''
    Keeps a list og all the books
    '''

    # This is a global variable shared bby all object of this class
    all_books = BookListSearch()

    def __init__(self,bookname,author):
        self.bookname = bookname
        self.author=author
        Booklist.all_books.append(self)

class Audiobook(Booklist):
    '''
    This stores the format of the audiobook
    '''
    

    def format(self,audio_format):
        '''
        Prints the audio book of the format
        '''
        print('The format of this audio book is '+audio_format)


class BookPublisher(Booklist):
    '''
    This class is to show method overiding
    We override the method rom Booklist Super Class
    and add publisher also if an object is creates on this class
    '''

    def __init__(self,bookname,author,publisher):
        super().__init__(bookname,author)
        self.publisher = publisher

    def disp_publisher(self):
        print(self.publisher)








