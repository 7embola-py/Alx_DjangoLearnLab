# Update Operation

```python
from bookshelf.models import Book

# Retrieve the Book instance
b = Book.objects.get(title="1984")

# Update the title
b.title = "Nineteen Eighty-Four"
b.save()

# Verify the update
print(b.title, b.author, b.publication_year)
# Output: Nineteen Eighty-Four George Orwell 1949


