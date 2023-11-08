import datetime

# Django
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

# Models
from apps.news.models import News

# Form
from apps.news.forms import NewsForm


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
		# if self.object.is_task:
		# 	self.object.published = False
		# if self.object.video:
		# 	self.object.embed = self.object.video.split('?v=')[1]
		self.object.save()
		# for each in form.cleaned_data['images']:
		# 	Gallery.objects.create(image=each, news=self.object)
		# set_wm_image(self.object)
		# if self.object.published:
		# 	#elay(self.object), #post_object
		# 	post_twitter.delay(self.object)
		# 	post_instagram.delay(self.object)
		return super(NewsCreate, self).form_valid(form)


class NewsDelete(DeleteView):
	model = News
	template_name = 'news/delete.html'
	success_url = reverse_lazy('news:admin_news_list')
