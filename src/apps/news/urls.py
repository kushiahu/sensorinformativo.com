# Django
from django.urls import path

# Views
from apps.news import views


app_name = 'news'

urlpatterns = [
    path(
        'panel/categorias/',
        views.CategoryList.as_view(),
        name='list_categories'
    ),
    path(
        'panel/categoria/nueva/',
        views.CategoryCreate.as_view(),
        name='create_category'
    ),
    path(
        'panel/categoria/editar/<slug:slug>/',
        views.CategoryUpdate.as_view(),
        name='update_category'
    ),
    path(
        'panel/categoria/eliminar/<slug:slug>/',
        views.CategoryDelete.as_view(),
        name='delete_category'
    ),
]
