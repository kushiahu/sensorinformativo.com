import datetime

# Django
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import DeletionMixin

# Models
from apps.news.models import News, Gallery

# Form
from apps.news.forms import NewsForm, NewsUpdateForm


class NewsDetail(DetailView):
	model = News
	template_name = 'news/detail.html'


class NewsPnlList(ListView):
	context_object_name = 'news'
	queryset = News.objects.filter(published=True).order_by('-date_published')
	template_name = 'news/admin_list.html'
	# login_url = reverse_lazy('user:login')
	# permission_required = "news.add_news"
	# paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super(NewsPnlList, self).get_context_data(**kwargs)
		context['news_inactive'] = News.objects.filter(published=False, is_task=False).order_by('-date_published')
		context['news_tasks'] = News.objects.filter(published=False, is_task=True).order_by('-date_published')
		context['total'] = News.objects.filter(published=True).order_by('-date_published').count()
		return context


class NewsCreate(CreateView):
	form_class = NewsForm
	success_url = reverse_lazy('news:admin_news_list')
	template_name = 'news/create.html'
	# login_url = reverse_lazy('user:login')
	# permission_required = "news.add_news"

	def form_valid(self, form):
		self.object = form.save()
		self.object.date_published = datetime.datetime.now()
		images = self.request.FILES.getlist('images')
		for image in images:
			Gallery.objects.create(image=image, news=self.object)
		cover = self.object.gallery.first()
		self.object.cover = cover.image
		return super(NewsCreate, self).form_valid(form)


class NewsUpdate(UpdateView):
	form_class = NewsUpdateForm
	model = News
	success_url = reverse_lazy('news:admin_news_list')
	template_name = 'news/update.html'
	# login_url = reverse_lazy('user:login')
	# permission_required = "news.change_news"

	def form_valid(self, form):
		self.object = form.save()
		images = self.request.FILES.getlist('images')
		for image in images:
			Gallery.objects.create(image=image, news=self.object)
		return super(NewsUpdate, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(NewsUpdate, self).get_context_data(**kwargs)
		images = Gallery.objects.filter(news=self.object)
		cover = images.first()
		self.object.cover = cover.image
		self.object.save()
		context['is_published'] = self.object.published
		context['gallery'] = images
		context['slug_news'] = self.object.slug
		return context


class NewsDelete(DeleteView):
	model = News
	template_name = 'news/delete.html'
	success_url = reverse_lazy('news:admin_news_list')


class ImageDelete(DeletionMixin, SingleObjectMixin, View):
	# login_url = reverse_lazy('user:login')
	model = Gallery
	# permission_required = "news.delete_news"
	pk_url_kwarg = "pk"

	def get(self, *args, **kwargs):
		return self.delete(*args, **kwargs)

	def get_success_url(self):
		return reverse_lazy('news:update_news', kwargs={'slug':self.kwargs.get('slug')})

