# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 14:54:59 2025

@author: Sai Manogna
"""

import datetime

class Book:
    def __init__(self, book_id, title, author):
        self.book_id, self.title, self.author = book_id, title, author
        self.available = True
class Borrower:
    def __init__(self, borrower_id, name):
        self.borrower_id, self.name = borrower_id, name
        self.borrowed_books = {}
class Library:
    def __init__(self):
        self.books, self.borrowers = {}, {}
    def add_book(self, book_id, title, author):
        self.books[book_id] = Book(book_id, title, author)
        print(f"Book '{title}' added.")
    def register_borrower(self, borrower_id, name):
        self.borrowers[borrower_id] = Borrower(borrower_id, name)
        print(f"Borrower '{name}' registered.")
    def borrow_book(self, borrower_id, book_id):
        b, bk = self.borrowers.get(borrower_id), self.books.get(book_id)
        if not b or not bk: return print("Borrower or Book not found.")
        if not bk.available: return print("Book is already borrowed.")
        due = datetime.date.today() + datetime.timedelta(days=14)
        b.borrowed_books[book_id], bk.available = due, False
        print(f"Book '{bk.title}' borrowed by '{b.name}'. Due on {due}.")
    def return_book(self, borrower_id, book_id):
        b = self.borrowers.get(borrower_id)
        if not b or book_id not in b.borrowed_books: return print("Invalid return.")
        due = b.borrowed_books.pop(book_id)
        bk, today = self.books[book_id], datetime.date.today()
        bk.available = True
        if today > due:
            print(f"Book returned late. Fine: ₹{(today - due).days * 5}")
        else:
            print(f"Book '{bk.title}' returned on time.")
    def show_books(self):
        for bk in self.books.values():
            print(f"{bk.book_id}: {bk.title} by {bk.author} [{'Available' if bk.available else 'Borrowed'}]")
    def show_borrowers(self):
        for b in self.borrowers.values():
            print(f"{b.borrower_id}: {b.name} - Borrowed Books: {list(b.borrowed_books.keys())}")

lib = Library()
lib.add_book(1, "Python Basics", "PROF.MITESH")
lib.add_book(2, "Data Structures", "PROF.CHIRAG")
lib.register_borrower(163, "sai Manogna")
lib.borrow_book(163, 1)
lib.show_books()
lib.return_book(163, 1)