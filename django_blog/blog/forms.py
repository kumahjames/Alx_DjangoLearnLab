from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

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

# Form for creating and updating blog posts WITH TAGS
class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text='Enter tags separated by commas (e.g., django, python, web)',
        widget=forms.TextInput(attrs={'placeholder': 'django, python, web'})
    )
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Enter post title'})
        self.fields['content'].widget.attrs.update({'placeholder': 'Write your post content here...'})
        
        # Set initial tags value if editing existing post
        if self.instance and self.instance.pk:
            self.initial['tags'] = ', '.join(tag.name for tag in self.instance.tags.all())

# Form for creating and updating comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Write your comment here...',
            'rows': 3
        })