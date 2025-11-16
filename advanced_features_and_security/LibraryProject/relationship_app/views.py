from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Library

# Function-based view to list all books - requires can_view permission
@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    from .models import Book
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(PermissionRequiredMixin, DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    permission_required = 'bookshelf.can_view'

# Class-based view to list all libraries
class LibraryListView(PermissionRequiredMixin, ListView):
    model = Library
    template_name = 'relationship_app/library_list.html'
    context_object_name = 'libraries'
    permission_required = 'bookshelf.can_view'