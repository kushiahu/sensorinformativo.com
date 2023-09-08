import os
from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Category(models.Model):

	name = models.CharField('Nombre', max_length=120, unique=True)
	slug = models.SlugField(max_length=120, unique=True, editable=False)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)


class Author(models.Model):

	first_name = models.CharField('Nombre(s)', max_length=120)
	last_name = models.CharField('Apellido(s)', max_length=120, null=True, blank=True)
	email = models.EmailField('Email', blank=True, null=True)
	slug = models.SlugField(max_length=120, unique=True, editable=False)

	def __str__(self):
		return f'{self.first_name} {self.larst_name}'

	def save(self, *args, **kwargs):
		self.slug = slugify(f'{self.first_name} {self.last_name}')
		super(Author, self).save(*args, **kwargs)


class News(models.Model):

	title = models.CharField('Título de la noticia *', max_length=120, unique=True)
	slug = models.SlugField(max_length=120, unique=True, editable=False)
	body = models.TextField('Contenido de la noticia *')
	video = models.URLField('URL video youtube', blank=True, null=True)	
	category = models.ForeignKey(
		Category,
		on_delete=models.CASCADE,
		related_name='news',
		verbose_name='Categoría *'
	)
	author = models.ForeignKey(
		Author,
		on_delete=models.CASCADE,
		related_name='news',
		verbose_name='Autor *'
	)
	views = models.IntegerField(default=0)
	published = models.BooleanField(default=True)
	date_published = models.DateTimeField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(News, self).save(*args, **kwargs)

	class Meta:
		ordering = ["-date_published"]
