

from django.urls import path
from django.urls import include, path
from .import views

urlpatterns = [
    path('news/<str:name>',views.detail, name='detail'),
    path('panel/news/list/', views.news_list, name='news_list'),
    path('panel/news/add/', views.news_add, name='news_add'),
    path('panel/news/del/<int:id>',views.news_delete, name='news_delete'),
    path('panel/news/edit/<int:id>',views.news_edit, name='news_edit'),

]