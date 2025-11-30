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

