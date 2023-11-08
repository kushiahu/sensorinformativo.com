# -*- coding: utf-8 -*-
from django import forms
from froala_editor.widgets import FroalaEditor
# from multiupload.fields import MultiFileField

from apps.news.models import News


class NewsForm(forms.ModelForm):
	body = forms.CharField(widget=FroalaEditor)
	# images = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)
	class Meta:
		model = News
		exclude = ['views', 'date_published', 'published', 'name_img']
		widgets = {
			'date_task': forms.TextInput(attrs={'type': 'date'}),
			'hour_task': forms.TimeInput(attrs={'type': 'time'}),
		}

	def __init__(self, *args, **kwargs):
		super(NewsForm, self).__init__(*args, **kwargs)
		# self.fields['images'].widget.attrs.update({'accept': 'image/*'})