# LibraryProject/relationship_app/query_samples.py

from .models import Author, Book, Library, Librarian

# -------------------------------
# 1. Query all books by a specific author
# -------------------------------
author_name = "Asmaa"
author = Author.objects.get(name=author_name)
books_by_author = author.book_set.all()
print(f"Books by {author_name}: {list(books_by_author)}")

# -------------------------------
# 2. List all books in a library
# -------------------------------
library_name = "City Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}: {list(books_in_library)}")

# -------------------------------
# 3. Retrieve the librarian for a library
# -------------------------------
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library_name}: {librarian.name}")
