# Django
from django import forms

# Models
from apps.news.models import Category


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = '__all__'