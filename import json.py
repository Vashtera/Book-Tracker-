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
        self.author = author
        self.title = title
        if title not in self.books.values('title'):
            self.books['Unread'] = []
        self.books['Unread'].append({
            'author': author,
            'title' : title 
            })
        if self.title in self.books.values('title'):
            print(f"The {self.title} book is exist in your library")
    
    def add_read_status(self, answer):
        if answer == "Y":
            for id, book in enumerate(self.books['Unread']):
                print(f"{id+1}. {book['author']}: {book['title']}")
            try: 
                id_answer = int(input("Enter number of your book: "))
                id_book = self.books['Unread'][id_answer - 1]
            except ValueError:
                print("You need to enter number!")
            for author, title in self.books.items():
                if self.title in title:
                    title.remove(self.title)
                    self.books['Read'].append(id_book)
                    return print("The books succesfully move in Read section")
            return print("The book with this id not founded")



    def show_unread_book(self):
        for book in self.books['Unread']:
            print(f"{book['author']}: {book['title']}")

    def save(self):
        with open("library.json", 'w') as file:
            json.dump(self.books, file)