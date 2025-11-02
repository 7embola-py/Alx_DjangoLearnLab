# Delete Operation

```python
from bookshelf.models import Book

# Retrieve the Book instance
b = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
b.delete()

# Confirm deletion
print(Book.objects.all())
# Output: <QuerySet []>

