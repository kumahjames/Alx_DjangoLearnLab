from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Book
from .serializers import BookSerializer

# Keep the existing view for backward compatibility - make it public
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Anyone can view the book list

# New ViewSet for full CRUD operations with proper permissions
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Set permissions: Anyone can view, but only authenticated users can modify
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]  # Anyone can view books
        else:
            permission_classes = [IsAuthenticated]  # Only authenticated users can create, update, delete
        return [permission() for permission in permission_classes]