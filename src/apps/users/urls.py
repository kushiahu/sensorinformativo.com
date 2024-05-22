# Django
from django.urls import path

# Views
from apps.users import views

app_name = 'user'


urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
