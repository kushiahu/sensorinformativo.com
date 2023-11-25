# -*- coding: utf-8 -*-
from django import forms
from froala_editor.widgets import FroalaEditor

from apps.news.models import News


class NewsForm(forms.ModelForm):
	body = forms.CharField(widget=FroalaEditor)
	images = forms.ImageField(
		label='Imagenes *',
		widget=forms.ClearableFileInput(
			attrs={'allow_multiple_selected': True}
		)
	)
	class Meta:
		model = News
		fields = [
			'title', 'body', 'author', 'category',
			'video', 'is_task', 'date_task', 'hour_task'
		]
		widgets = {
			'date_task': forms.TextInput(attrs={'type': 'date'}),
			'hour_task': forms.TimeInput(attrs={'type': 'time'}),
		}

	def __init__(self, *args, **kwargs):
		super(NewsForm, self).__init__(*args, **kwargs)
		self.fields['images'].widget.attrs.update({'accept': 'image/*', 'multiple': 'multiple'})


class NewsUpdateForm(NewsForm):
	images = forms.ImageField(
		label='Imagenes',
		required=False, 
		widget=forms.ClearableFileInput(
			attrs={'allow_multiple_selected': True}
		)
	)
