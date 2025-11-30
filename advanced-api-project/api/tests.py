from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author

class BookAPITestCase(TestCase):
    """
    Test case for Book API endpoints including CRUD operations,
    filtering, searching, ordering, and permissions.
    """
    
    def setUp(self):
        """
        Set up test data and client for each test method.
        """
        # Create test client
        self.client = APIClient()
        
        # Create test users
        self.regular_user = User.objects.create_user(
            username='testuser', 
            password='testpass123'
        )
        self.staff_user = User.objects.create_user(
            username='staffuser', 
            password='staffpass123',
            is_staff=True
        )
        
        # Create test authors
        self.author1 = Author.objects.create(name='J.K. Rowling')
        self.author2 = Author.objects.create(name='George Orwell')
        
        # Create test books
        self.book1 = Book.objects.create(
            title='Harry Potter and the Philosopher\'s Stone',
            publication_year=1997,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title='1984',
            publication_year=1949,
            author=self.author2
        )
        self.book3 = Book.objects.create(
            title='Harry Potter and the Chamber of Secrets',
            publication_year=1998,
            author=self.author1
        )
    
    # Test CRUD Operations
    
    def test_list_books(self):
        """
        Test retrieving list of all books.
        """
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
    
    def test_retrieve_single_book(self):
        """
        Test retrieving a single book by ID.
        """
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)
    
    def test_create_book_authenticated(self):
        """
        Test creating a book as authenticated user.
        """
        self.client.force_authenticate(user=self.regular_user)
        data = {
            'title': 'New Test Book',
            'publication_year': 2020,
            'author': self.author1.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['book']['title'], 'New Test Book')
    
    def test_create_book_unauthenticated(self):
        """
        Test that unauthenticated users cannot create books.
        """
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2020,
            'author': self.author1.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_update_book_authenticated(self):
        """
        Test updating a book as authenticated user.
        """
        self.client.force_authenticate(user=self.regular_user)
        data = {
            'title': 'Updated Title',
            'publication_year': 1997,
            'author': self.author1.id
        }
        response = self.client.put(f'/api/books/update/{self.book1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['book']['title'], 'Updated Title')
    
    def test_delete_book_staff_only(self):
        """
        Test that only staff users can delete books.
        """
        # Try as regular user (should fail)
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.delete(f'/api/books/delete/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Try as staff user (should succeed)
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.delete(f'/api/books/delete/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # Test Filtering, Searching, and Ordering
    
    def test_filter_by_publication_year(self):
        """
        Test filtering books by publication year.
        """
        response = self.client.get('/api/books/?publication_year=1997')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book1.title)
    
    def test_filter_by_author_name(self):
        """
        Test filtering books by author name.
        """
        response = self.client.get('/api/books/?author__name=George Orwell')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book2.title)
    
    def test_search_books(self):
        """
        Test searching books by title or author name.
        """
        response = self.client.get('/api/books/?search=Harry')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_ordering_books(self):
        """
        Test ordering books by different fields.
        """
        # Order by title ascending
        response = self.client.get('/api/books/?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], '1984')
        
        # Order by publication year descending
        response = self.client.get('/api/books/?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1998)
    
    # Test Validation
    
    def test_publication_year_validation(self):
        """
        Test that publication year cannot be in the future.
        """
        self.client.force_authenticate(user=self.regular_user)
        data = {
            'title': 'Future Book',
            'publication_year': 2030,  # Future year
            'author': self.author1.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)
    
    def test_required_fields_validation(self):
        """
        Test that required fields are validated.
        """
        self.client.force_authenticate(user=self.regular_user)
        data = {
            'title': '',  # Empty title
            'publication_year': 2020,
            'author': self.author1.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)