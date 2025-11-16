\# Django Permissions and Groups Setup Guide



\## Overview

This application implements a custom permissions system to control access to book-related functionality using Django's built-in authentication and authorization system.



\## Custom Permissions Defined



The following custom permissions are defined in the `Book` model:



\- \*\*can\_view\*\*: Permission to view books

\- \*\*can\_create\*\*: Permission to create new books  

\- \*\*can\_edit\*\*: Permission to edit existing books

\- \*\*can\_delete\*\*: Permission to delete books



\## Recommended Groups Setup



\### 1. Viewers Group

\- \*\*Permissions\*\*: `can\_view`

\- \*\*Description\*\*: Users in this group can only view books but cannot create, edit, or delete them.



\### 2. Editors Group  

\- \*\*Permissions\*\*: `can\_view`, `can\_create`, `can\_edit`

\- \*\*Description\*\*: Users in this group can view, create, and edit books but cannot delete them.



\### 3. Admins Group

\- \*\*Permissions\*\*: `can\_view`, `can\_create`, `can\_edit`, `can\_delete`

\- \*\*Description\*\*: Users in this group have full access to all book operations.



\## Views Protection



\### Function-based Views

\- `list\_books()`: Protected with `@permission\_required('bookshelf.can\_view')`

\- Users must have `can\_view` permission to access the book listing



\### Class-based Views  

\- `LibraryListView`: Protected with `PermissionRequiredMixin` and `permission\_required = 'bookshelf.can\_view'`

\- `LibraryDetailView`: Protected with `PermissionRequiredMixin` and `permission\_required = 'bookshelf.can\_view'`



\## Setup Instructions



1\. \*\*Create Groups\*\*: 

&nbsp;  - Go to Django Admin → Authentication and Authorization → Groups

&nbsp;  - Create the three groups (Viewers, Editors, Admins)

&nbsp;  - Assign appropriate permissions to each group



2\. \*\*Assign Users\*\*:

&nbsp;  - Assign users to appropriate groups based on their roles

&nbsp;  - Users inherit permissions from their group memberships



3\. \*\*Testing\*\*:

&nbsp;  - Create test users and assign them to different groups

&nbsp;  - Verify that permissions are enforced by accessing protected views



\## URL Patterns

\- `/relationship/books/` - Requires `can\_view` permission

\- `/relationship/libraries/` - Requires `can\_view` permission  

\- `/relationship/library/<id>/` - Requires `can\_view` permission

