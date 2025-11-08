# relationship_app/query_samples.py
import os
import django

# set Django settings module and initialize
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# helper to create data safely using get_or_create
author, _ = Author.objects.get_or_create(name="Asmaa")

book1, _ = Book.objects.get_or_create(title="Django Basics", author=author)
book2, _ = Book.objects.get_or_create(title="Advanced Python", author=author)

library, _ = Library.objects.get_or_create(name="City Library")
library.books.add(book1, book2)

librarian, _ = Librarian.objects.get_or_create(name="Khalid", library=library)

# Queries:
print("Books by Asmaa:", list(Author.objects.filter(name="Asmaa").first().book_set.all()))
print("Books in library:", list(library.books.all()))
print("Librarian for library:", Librarian.objects.get(library=library).name)
