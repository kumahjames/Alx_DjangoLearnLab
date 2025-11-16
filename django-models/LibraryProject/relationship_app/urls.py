from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryListView, LibraryDetailView, register_view

app_name = 'relationship_app'

urlpatterns = [
    # Authentication URLs using Django's built-in class-based views
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Function-based view URL
    path('books/', list_books, name='list_books'),
    
    # Class-based view URLs
    path('libraries/', LibraryListView.as_view(), name='library_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]