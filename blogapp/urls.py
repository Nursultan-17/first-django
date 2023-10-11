from django.urls import path
from .views import *

# path('<Роут маршрут>', <Имя вашей вьюшки>.as_view(), name='<Внутреннее имя для маршрута>'),
urlpatterns = [
    path('posts', PostListView.as_view(), name='post_list_url'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail_url'),
    path('post/create', PostCreateView.as_view(), name='post_create_url'),
    path('stories', StoryListView.as_view(), name= 'story_list_url'),
    path('story/<int:pk>', StoryDetailView.as_view(), name='story_detail_url'),
    path('story/create', StoryCreateView.as_view(), name='story_create_url'),
]