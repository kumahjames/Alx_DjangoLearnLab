from django.db import models

# Create your models here.
from django.db import models

# Author model to store author information
class Author(models.Model):
    # Name field to store the author's name
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Book model to store book information with relationship to Author
class Book(models.Model):
    # Title field for the book's title
    title = models.CharField(max_length=200)
    # Publication year field
    publication_year = models.IntegerField()
    # Foreign key relationship to Author (one author can have many books)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.title