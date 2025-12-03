from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
# Custom registration form that extends Django's UserCreationForm
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# Form for updating user profile
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email']

# Form for creating and updating blog posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Enter post title'})
        self.fields['content'].widget.attrs.update({'placeholder': 'Write your post content here...'})