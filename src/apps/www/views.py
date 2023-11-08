# Django
from django.shortcuts import render

# Models
from apps.news.models import News


def index(request):
	news = News.objects.filter(published=True)
	return render(request, 'index.html', {'news': news})
