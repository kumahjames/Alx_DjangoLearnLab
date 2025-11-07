from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Library

# Task 1: List all books (function-based)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

# Task 2: Library detail with books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'