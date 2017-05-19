from django.forms import forms, TextInput, Textarea, DateTimeInput
from django.forms import ModelForm
from django import forms

from .models import Article,Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'comment')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name'})
        self.fields['comment'].widget = Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Comment'})






