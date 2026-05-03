import json
import copy

class Books:
    def __init__(self):
        self.books = {}

    def load(self) -> None:
        try:
            with open("library.json", 'r') as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = {}

    def add_book(self, author, title):
        if title not in self.books.values('title'):
            self.books['Unread'] = []
        self.books['Unread'].append({
            'author': author,
            'title' : title 
            })
        if title in self.books.values('title'):
            print(f"The {title} book is exist in your library")
    
    def add_read_status(self, answer):
        if answer == "Y":
            for id, book in self.books['Unread']:
                print(f"{id+1}. {book['author']}: {book['title']}")
            



    def show_unread_book(self):
        for book in self.books['Unread']:
            print(f"{book['author']}: {book['title']}")

    def save(self):
        with open("library.json", 'w') as file:
            json.dump(self.books, file)