from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('introduction', views.introduction, name='introduction'),
    path('daily', views.daily, name='daily'),
    path('daily/<str:album_name>/<int:pk>/', views.daily_detail, name='daily_detail'),
    path('daily/<int:pk>/',views.photo, name='photo'),
    path('posts', views.posts, name='posts'),
    path('post_list', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]