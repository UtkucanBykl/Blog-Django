from django import forms

from comment.models import Comment


class CommentForm(forms.ModelForm):

    username = forms.CharField(max_length=30, label="Adınız", widget=forms.TextInput)

    class Meta:
        model = Comment
        fields = ["username", "comment"]