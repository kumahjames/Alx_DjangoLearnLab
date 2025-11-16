import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Alx_DjangoLearnLab.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    """Query all books by a specific author"""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return Book.objects.none()

def list_all_books_in_library(library_name):
    """List all books in a library"""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return Book.objects.none()

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage and testing
if __name__ == "__main__":
    # Create sample data for testing
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")
    
    book1 = Book.objects.create(title="Harry Potter", author=author1)
    book2 = Book.objects.create(title="1984", author=author2)
    book3 = Book.objects.create(title="Animal Farm", author=author2)
    
    library = Library.objects.create(name="City Library")
    library.books.add(book1, book2, book3)
    
    librarian = Librarian.objects.create(name="John Smith", library=library)
    
    # Test the queries
    print("=== Testing Queries ===")
    print("Books by J.K. Rowling:", list(query_all_books_by_author("J.K. Rowling")))
    print("Books by George Orwell:", list(query_all_books_by_author("George Orwell")))
    print("Books in City Library:", list(list_all_books_in_library("City Library")))
    print("Librarian for City Library:", get_librarian_for_library("City Library"))