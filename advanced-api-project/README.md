\# Advanced API Project - Custom Views \& Generic Views



\## Project Overview

This Django REST Framework project demonstrates the implementation of custom views and generic views for handling CRUD operations on Book resources.



\## API Endpoints



\### Book Operations



| Endpoint | Method | Description | Permissions |

|----------|--------|-------------|-------------|

| `/api/books/` | GET | List all books | Public (AllowAny) |

| `/api/books/<id>/` | GET | Get single book details | Public (AllowAny) |

| `/api/books/create/` | POST | Create a new book | Authenticated users only |

| `/api/books/update/<id>/` | PUT/PATCH | Update existing book | Authenticated users + Object permissions |

| `/api/books/delete/<id>/` | DELETE | Delete a book | Staff users only |



\## View Configuration Details



\### BookListView (`generics.ListAPIView`)

\- \*\*Purpose\*\*: Retrieve all book instances

\- \*\*Permissions\*\*: `AllowAny` - Public read access

\- \*\*Customization\*\*: Uses default list behavior with BookSerializer



\### BookDetailView (`generics.RetrieveAPIView`)

\- \*\*Purpose\*\*: Retrieve single book instance by ID

\- \*\*Permissions\*\*: `AllowAny` - Public read access

\- \*\*Customization\*\*: Standard retrieve operation



\### BookCreateView (`generics.CreateAPIView`)

\- \*\*Purpose\*\*: Create new book instances

\- \*\*Permissions\*\*: `IsAuthenticated` - Requires user authentication

\- \*\*Customization\*\*: Enhanced response with success message and book data



\### BookUpdateView (`generics.UpdateAPIView`)

\- \*\*Purpose\*\*: Update existing book instances

\- \*\*Permissions\*\*: `IsAuthenticated` + `IsOwnerOrReadOnly` - Authenticated users with object permissions

\- \*\*Customization\*\*: Enhanced response with success message and updated book data



\### BookDeleteView (`generics.DestroyAPIView`)

\- \*\*Purpose\*\*: Delete book instances

\- \*\*Permissions\*\*: `IsStaffUser` - Restricted to staff users only

\- \*\*Customization\*\*: Enhanced response with book title in success message



\## Custom Permission Classes



\### IsOwnerOrReadOnly

\- Allows read access to all users

\- Restricts write operations to object owners

\- Currently allows any authenticated user (can be extended for ownership)



\### IsStaffUser

\- Restricts access to staff users only

\- Used for sensitive operations like deletion



\## Testing

The API can be tested using:

1\. Django REST Framework's browsable API

2\. Tools like Postman or curl

3\. Django admin interface for data management



\## Setup Requirements

\- Django 3.2+

\- Django REST Framework

\- SQLite database (default)


## Advanced Query Features

### Filtering, Searching, and Ordering

The BookListView now supports advanced query capabilities:

#### Filtering
Filter books by specific fields using query parameters:
- `?title=Harry Potter` - Filter by exact title
- `?publication_year=1997` - Filter by publication year
- `?author__name=J.K. Rowling` - Filter by author name

#### Searching
Perform text searches across multiple fields:
- `?search=harry` - Search in title and author name fields
- `?search=rowling` - Search for author names

#### Ordering
Sort results by various fields:
- `?ordering=title` - Sort by title (ascending)
- `?ordering=-publication_year` - Sort by publication year (descending)
- `?ordering=title,-publication_year` - Multiple field sorting

### Example API Requests

```http
# Get all books published in 1997
GET /api/books/?publication_year=1997

# Search for books with "Harry" in title or author name
GET /api/books/?search=harry

# Get books sorted by publication year (newest first)
GET /api/books/?ordering=-publication_year

# Combined: Search and filter
GET /api/books/?search=potter&publication_year=1997&ordering=title

## Testing Strategy

### Test Coverage
The test suite comprehensively covers:
- **CRUD Operations**: Create, Read, Update, Delete functionality
- **Authentication & Permissions**: User access control testing
- **Filtering, Searching, Ordering**: Query parameter functionality
- **Validation**: Data integrity and business rule validation

### Running Tests
```bash
# Run all tests for the api app
python manage.py test api

# Run with verbose output
python manage.py test api -v 2

# Run specific test case
python manage.py test api.tests.BookAPITestCase

# Run specific test method
python manage.py test api.tests.BookAPITestCase.test_list_books