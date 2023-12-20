from exercise18 import EBook
my_book = EBook("Python Programming", "Guido van Rossum", 300)
my_book.open_book()
my_book.display_status()
my_book.read_pages(5)
my_book.display_status()
my_book.close_book()
my_book.read_pages(3)
