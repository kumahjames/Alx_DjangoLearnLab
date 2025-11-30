from django.urls import path
from . import views

# URL patterns for Book views
urlpatterns = [
    # List all books - GET /books/
    path('books/', views.BookListView.as_view(), name='book-list'),
    
    # Get single book by ID - GET /books/1/
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    
    # Create new book - POST /books/create/
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    
    # Update existing book - PUT/PATCH /books/update/1/
    path('books/update/<int:pk>/', views.BookUpdateView.as_view(), name='book-update'),
    
    # Delete book - DELETE /books/delete/1/
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),
]