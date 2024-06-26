# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

# Models
from apps.news.models import Author

# Form
from apps.news.forms import AuthorForm


class AuthorList(LoginRequiredMixin, ListView):
	context_object_name = 'authors'
	queryset = Author.objects.all()
	template_name = 'author/list.html'


class AuthorCreate(LoginRequiredMixin, CreateView):
	form_class = AuthorForm
	success_url = reverse_lazy('news:list_authors')
	template_name = 'author/create_update.html'


class AuthorUpdate(LoginRequiredMixin, UpdateView):
	form_class = AuthorForm
	model = Author
	success_url = reverse_lazy('news:list_authors')
	template_name = 'author/create_update.html'


class AuthorDelete(LoginRequiredMixin, DeleteView):
	model = Author
	template_name = 'author/delete.html'
	success_url = reverse_lazy('news:list_authors')
