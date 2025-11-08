# Update Operation

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Output the updated title
print(book.title)  # Output: Nineteen Eighty-Four


