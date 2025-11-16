from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from django.core.exceptions import ValidationError
import re
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Secure book listing view with input validation and safe search functionality.
    Uses Django ORM to prevent SQL injection and validates user input.
    """
    books = Book.objects.all()
    
    # Safe search functionality - uses Django ORM to prevent SQL injection
    search_query = request.GET.get('search', '').strip()
    
    if search_query:
        # Input validation: only allow alphanumeric characters and spaces
        if not re.match(r'^[a-zA-Z0-9\s\-\.]+$', search_query):
            # Log suspicious input (in production, you'd use proper logging)
            print(f"Potential malicious input detected: {search_query}")
            search_query = ''  # Reset to safe value
        else:
            # Safe ORM query using parameterized queries (no string formatting)
            books = books.filter(
                Q(title__icontains=search_query) | 
                Q(author__icontains=search_query)
            )
    
    return render(request, 'bookshelf/book_list.html', {
        'books': books,
        'search_query': search_query
    })

def safe_book_detail(request, book_id):
    """
    Secure book detail view using get_object_or_404 to prevent information leakage.
    """
    # Safe object retrieval - prevents exposing existence of objects
    book = get_object_or_404(Book, id=book_id)
    
    return render(request, 'bookshelf/book_detail.html', {'book': book})

def validate_book_data(title, author, publication_year):
    """
    Custom validation function to ensure data integrity and security.
    """
    errors = []
    
    # Validate title
    if not title or len(title.strip()) == 0:
        errors.append("Title is required")
    elif len(title) > 200:
        errors.append("Title too long")
    
    # Validate author - only allow letters, spaces, and common punctuation
    if not re.match(r'^[a-zA-Z\s\-\'\.]+$', author):
        errors.append("Invalid author name")
    
    # Validate publication year
    try:
        year = int(publication_year)
        if year < 1000 or year > 2024:
            errors.append("Invalid publication year")
    except (ValueError, TypeError):
        errors.append("Publication year must be a valid number")
    
    return errors