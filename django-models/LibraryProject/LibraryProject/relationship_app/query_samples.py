"""
Sample queries for relationship_app models
"""

# Query all books by a specific author
def books_by_author(author_name):
    """
    Returns all books written by a specific author
    """
    from .models import Book, Author
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return Book.objects.none()

# List all books in a library
def books_in_library(library_name):
    """
    Returns all books available in a specific library
    """
    from .models import Library
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return Library.books.model.objects.none()

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    """
    Returns the librarian for a specific library
    """
    from .models import Library, Librarian
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage (commented out):
# if __name__ == "__main__":
#     # Query books by author
#     author_books = books_by_author("George Orwell")
#     print("Books by George Orwell:", list(author_books))
#     
#     # Query books in library
#     library_books = books_in_library("Main Library")
#     print("Books in Main Library:", list(library_books))
#     
#     # Query librarian for library
#     librarian = librarian_for_library("Main Library")
#     print("Librarian for Main Library:", librarian)