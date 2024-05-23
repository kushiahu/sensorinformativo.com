# Django
from django.urls import path

# Views
from apps.www import views


app_name = 'site'

urlpatterns = [
    path('', views.index, name='index'),
    path('celery/', views.testing_celery, name='testing'),
]
