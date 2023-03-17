from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    """
    Form class to add a comment
    """

    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': SummernoteWidget
        }


class PostForm(forms.ModelForm):
    """
    Form class to add a post
    """

    class Meta:
        model = Post
        fields = ('featured_image', 'author', 'title', 'slug', 'content')
        widgets = {
            'content': SummernoteWidget
        }
