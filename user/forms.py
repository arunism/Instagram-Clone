from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class ChangePasswordForm(forms.ModelForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'edit-profile__input'}), required=True)
	new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'edit-profile__input'}), required=True)
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'edit-profile__input'}), required=True)

	class Meta:
		model = User
		fields = ('id', 'old_password', 'new_password', 'confirm_password')
