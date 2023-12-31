# Python
from datetime import date

# Django
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager,
	PermissionsMixin,
)
from django.db import models
from django.template.defaultfilters import slugify


class UserManager(BaseUserManager, models.Manager):

	def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
		email = self.normalize_email(email)
		if not email:
			raise ValueError('El email debe ser obligatorio')
		user = self.model(username = username, email = email, is_active = True,
			is_staff = is_staff, is_superuser = is_superuser, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, False, False, **extra_fields)

	def create_superuser(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(unique=True, editable=False)
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	avatar = models.URLField(blank=True, null=True, default='')
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	id_facebook = models.CharField(max_length=64, blank=True, null=True)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def save(self, *args, **kwargs):
		self.slug = slugify(self.username)
		super(User, self).save(*args, **kwargs)

	def get_short_name(self):
		return self.username

	def full_name(self):
		return '%s %s' % (self.first_name, self.last_name)
