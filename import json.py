import json

class Books:
    def __init__(self):
        self.books = {}

    def load(self) -> None:
        try:
            with open("library.json", 'r') as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = {}

    def add_book(self, author: str, title: str) -> str:
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
    
    def add_read_status(self, answer: str) -> str:
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

    def show_unread_book(self) -> str:
        for book in self.books['Unread']:
            print(f"{book['author']}: {book['title']}")

    def save(self) -> None:
        with open("library.json", 'w') as file:
            json.dump(self.books, file)


my_books = Books()
my_books.load()

while True:
    question = input("Please choose what you want to do: " \
    "1: ADD/ 2: TURN READ STATUS /3: SHOW UNREAD BOOKS").upper()
    print("PRESS Q for exit")
    
    if question == '1':
        author = str(input("Please enter name of author: "))
        title = float(input("Please enter the title: "))
        my_books.add_book(author, title)
        my_books.save()

    if question == '2':
        clarification = str(input("Do you want change status of your book? Y/N: ")).upper()
        if clarification == 'Y':
            my_books.add_read_status(clarification)
            my_books.save()
        else:
            print("ok, Bye")

    if question == '3':
        my_books.show_unread_book()

    if question == 'Q':
        print('Bye!')
        break