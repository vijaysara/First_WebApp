

from django.urls import path
from django.urls import include, path
from .import views

urlpatterns = [
    path('panel/categories/list/', views.cat_list, name='cat_list'),
    path('panel/categories/add/', views.cat_add, name='cat_add'),
    path('panel/categories/del/<int:id>', views.cat_del, name='cat_del'),

]