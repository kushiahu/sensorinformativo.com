# Django
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Models
from apps.news.models import News
from apps.news.tasks import publish_news


def index(request):
	news_list = News.objects.filter(published=True)
	# print('antes del delay')
	# publish_news.delay_on_commit()

	# Paginación
	paginator = Paginator(news_list, 1)  # 10 noticias por página
	page = request.GET.get('page')
	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		# Si la página no es un número, mostrar la primera página
		news = paginator.page(1)
	except EmptyPage:
		# Si la página está fuera de rango, mostrar la última página
		news = paginator.page(paginator.num_pages)

	return render(request, 'index.html', {'news': news})
