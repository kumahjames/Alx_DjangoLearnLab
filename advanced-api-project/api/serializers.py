from rest_framework import serializers
from .models import Author, Book

# BookSerializer to handle Book model serialization
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
    
    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer to handle Author model serialization with nested books
class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to include related books dynamically
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']