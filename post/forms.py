from django import forms
from post.models import Post

class CreatePostForm(forms.ModelForm):
    photo = forms.ImageField(required=True)
    caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'edit-profile__input'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'edit-profile__input'}))

    class Meta:
        model = Post
        fields = ('photo', 'caption', 'location')
