from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Book Serializer with custom validation
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
    
    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future!")
        return value

# Author Serializer with nested Book relationships
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to include related books
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']  # Includes author name and their books