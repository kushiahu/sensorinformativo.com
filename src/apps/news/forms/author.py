# Django
from django import forms

# Models
from apps.news.models import Author


class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = '__all__'