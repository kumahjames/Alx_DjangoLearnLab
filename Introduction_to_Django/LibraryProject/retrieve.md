\# Retrieve Operation



\*\*Command:\*\*

```python

book = Book.objects.get(title="1984")

print(f"Title: {book.title}")

print(f"Author: {book.author}")

print(f"Publication Year: {book.publication\_year}")

