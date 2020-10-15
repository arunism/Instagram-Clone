from django import forms
from reaction.models import Comment

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={'class':'photo__add-comment', 'placeholder':'Add a comment...'}), required=True)

    class Meta:
        model = Comment
        fields = ('body',)
