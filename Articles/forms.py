from django.forms import forms
from django.forms import ModelForm
from django import forms

from .models import Article,Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'content')
