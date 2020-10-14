from django import forms
from django.contrib.auth.models import User
from user_profile.models import Profile

GENDER_CHOICE = (
    ('Male','Male'),
    ('Female','Female'),
    ("Don't want to specify","Don't want to specify"),
)

class EditProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'edit-profile__input'}), max_length=50, required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'edit-profile__input'}), max_length=50, required=False)
    nickname = forms.CharField(widget=forms.TextInput(attrs={'class': 'edit-profile__input'}), max_length=50, required=False)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'edit-profile__input'}), max_length=15, required=False)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'edit-profile__input'}), max_length=50, required=False)
    website = forms.URLField(widget=forms.TextInput(attrs={'class': 'edit-profile__input'}), max_length=50, required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'edit-profile__textarea'}), max_length=250, required=False)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'id':'gender'}), choices=GENDER_CHOICE, required=False)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone', 'website', 'bio', 'gender', 'picture')
