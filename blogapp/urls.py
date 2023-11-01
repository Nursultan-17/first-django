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

    path('flower', FlowerListView.as_view(), name='flower_list_url'),
    path('flower/<int:pk>', FlowerDetailView.as_view(), name='flower_detail_url'),
    path('flower/create', FlowerCreateView.as_view(), name='flower_create_url'),

    path('cars', CarsView, name='cars_url'),
    path('car/<int:car_id>', CarDetailView, name='car_detail_url'),
    path('cars/<str:car_brand>', CarFView, name='carf_url'),

    path('bouquets', BouquetsView, name='bouquets_url'),
    path('bouquet/<int:bouquet_id>', BouquetsDetailView, name='bouquets_detail_url'),
    path('create_bouquet', BouquetsCreateView, name='bouquets_create_url'),
    path('update_bouquet/<int:bouquet_id>', BouquetUpdateView, name='bouquets_update_url'),
]