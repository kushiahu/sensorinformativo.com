# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

# Models
from apps.news.models import Category

# Form
from apps.news.forms import CategoryForm


class CategoryList(LoginRequiredMixin, ListView):
	context_object_name = 'categories'
	queryset = Category.objects.all()
	template_name = 'category/list.html'


class CategoryCreate(LoginRequiredMixin, CreateView):
	form_class = CategoryForm
	success_url = reverse_lazy('news:list_categories')
	template_name = 'category/create_update.html'


class CategoryUpdate(LoginRequiredMixin, UpdateView):
	form_class = CategoryForm
	model = Category
	success_url = reverse_lazy('news:list_categories')
	template_name = 'category/create_update.html'


class CategoryDelete(LoginRequiredMixin, DeleteView):
	model = Category
	template_name = 'category/delete.html'
	success_url = reverse_lazy('news:list_categories')
