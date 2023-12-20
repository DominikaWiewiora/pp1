class EBook:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.current_page = 1
        self.is_open = False

    def open_book(self):
        self.is_open = True

    def display_status(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of Pages: {self.num_pages}")
        print(f"Current Page: {self.current_page}")

    def read_pages(self, pages_to_read):
        if self.is_open:
            self.current_page += pages_to_read
            if self.current_page > self.num_pages:
                self.current_page = self.num_pages
        else:
            print("The book is closed. Please open the book to read.")

    def close_book(self):
        self.is_open = False
