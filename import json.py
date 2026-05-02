import json

class Books:
    def __init__(self):
        self.books = {}
        self.status = {}

    def load(self) -> None:
        try:
            with open("data.json", 'r') as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = {}

    def add_book(self, author, title):
        if title not in self.books.values():
            self.books[author] = title
        else:
            print(f"The {title} book is exist in your library")
    
    def add_read_status(self, request):
        pass

    def show_unread_book(self):
        pass

    def save(self):
        with open("data.json", 'w') as file:
            json.dump(self.books, file)