from django.db import models

# Create your models here.
from django.db import models

# Author model representing book authors
class Author(models.Model):
    # Author's name field
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Book model representing books with author relationship
class Book(models.Model):
    # Book title field
    title = models.CharField(max_length=200)
    # Year the book was published
    publication_year = models.IntegerField()
    # Foreign key relationship to Author (one author can have many books)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.title