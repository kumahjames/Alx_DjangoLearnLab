from django import forms
from django.core.exceptions import ValidationError
import re

class ExampleForm(forms.Form):
    """
    Secure form example with built-in Django validation and custom security measures.
    Demonstrates proper input validation to prevent common vulnerabilities.
    """
    
    title = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter book title'
        }),
        error_messages={
            'required': 'Book title is required',
            'max_length': 'Title cannot exceed 200 characters'
        }
    )
    
    author = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter author name'
        })
    )
    
    publication_year = forms.IntegerField(
        min_value=1000,
        max_value=2024,
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Publication year'
        }),
        error_messages={
            'min_value': 'Publication year must be after 1000',
            'max_value': 'Publication year cannot be in the future'
        }
    )

    def clean_title(self):
        """Custom validation for title field to prevent XSS and injection attacks"""
        title = self.cleaned_data.get('title', '').strip()
        
        # Validate title contains only safe characters
        if not re.match(r'^[a-zA-Z0-9\s\-\'\.!,?]+$', title):
            raise ValidationError('Title contains invalid characters')
            
        return title

    def clean_author(self):
        """Custom validation for author field"""
        author = self.cleaned_data.get('author', '').strip()
        
        # Validate author name format
        if not re.match(r'^[a-zA-Z\s\-\'\.]+$', author):
            raise ValidationError('Author name contains invalid characters')
            
        return author

    def clean(self):
        """Overall form validation"""
        cleaned_data = super().clean()
        
        # Additional cross-field validation can be added here
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')
        
        if title and author:
            # Example: Prevent duplicate entries (in real app, check database)
            if title.lower() == 'test' and author.lower() == 'test':
                raise ValidationError('Test entries are not allowed')
                
        return cleaned_data