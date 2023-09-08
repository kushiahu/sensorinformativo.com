# Django
from django.urls import path

# Views
from apps.www import views


urlpatterns = [
    path('', views.index, name='index'),
]
