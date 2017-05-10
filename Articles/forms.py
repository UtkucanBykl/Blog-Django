from django.forms import forms
from django.forms import ModelForm
from django import forms

from .models import Article,Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'comment')

        def __init__(self, *args, **kwargs):
            super(CommentForm, self).__init__(*args, **kwargs)
            self.fields['name'].widget.attrs.update({'class': 'form-control','id':"name"})
            self.fields['comment'].widget.attrs.update({'class': 'form-control','id':"message"})




