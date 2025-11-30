from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated 
from django_filters.rest_framework import DjangoFilterBackend  # ADD THIS IMPORT
from rest_framework import filters  # ADD THIS IMPORT
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from .permissions import IsOwnerOrReadOnly, IsStaffUser

# List all books - accessible to everyone WITH FILTERING, SEARCHING, ORDERING
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
    # Add filtering, searching, and ordering backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtering: Allow filtering by specific fields
    filterset_fields = ['title', 'publication_year', 'author__name']
    
    # Searching: Allow text search on these fields
    search_fields = ['title', 'author__name']
    
    # Ordering: Allow ordering by these fields
    ordering_fields = ['title', 'publication_year', 'id']
    ordering = ['title']  # Default ordering

# Retrieve a single book by ID - accessible to everyone
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create a new book - only for authenticated users
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Changed from IsAuthenticated
    
    # Customize the response for successful creation
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'message': 'Book created successfully',
                'book': serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )

# Update an existing book - only for authenticated users
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]  # Enhanced permissions
    
    # Customize the response for successful update
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response(
            {
                'message': 'Book updated successfully',
                'book': serializer.data
            }
        )

# Delete a book - only for staff users
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsStaffUser]  # Only staff users can delete
    
    # Customize the response for successful deletion
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        book_title = instance.title
        self.perform_destroy(instance)
        return Response(
            {'message': f'Book "{book_title}" deleted successfully'},
            status=status.HTTP_200_OK
        )