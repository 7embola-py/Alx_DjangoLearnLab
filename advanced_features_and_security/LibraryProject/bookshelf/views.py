# Using Django ORM ensures queries are parameterized and prevents SQL injection

from .models import Book
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect



def form_example(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        author = request.POST.get("author", "").strip()
        year = request.POST.get("year", "").strip()

        # Basic validation
        if title and author and year.isdigit():
            Book.objects.create(
                title=title,
                author=author,
                publication_year=int(year)
            )
            return redirect("book_list")  # go back to book list
        else:
            error = "Please provide valid input for all fields."
            return render(request, "bookshelf/form_example.html", {"error": error})

    return render(request, "bookshelf/form_example.html")


@login_required
def book_list(request):
    # Safe query
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return HttpResponse("Create book page (only users with can_create).")


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return HttpResponse(f"Edit page for {book.title} (requires can_edit).")


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return HttpResponse(f"Delete page for {book.title} (requires can_delete).")
