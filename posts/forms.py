# forms.py
from django import forms
from .models import PostPost, PostComment

class postform(forms.ModelForm):
    class Meta:
        model = PostPost
        fields = ['title','text_content', 'file_content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['content']
