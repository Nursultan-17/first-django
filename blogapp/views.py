from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'  # Под каким именем данные будут отзыватся в html
    template_name = 'post_list_template.html'

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail_template.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create_template.html'
    fields = ['title', 'body', 'author']
    success_url = reverse_lazy('post_list_url')

class StoryListView(ListView):
    model = Story
    context_object_name = "stories"
    template_name = 'story_list_template.html'

class StoryDetailView(DetailView):
    model = Story
    context_object_name = 'story'
    template_name = 'story_detail_template.html'

class StoryCreateView(CreateView):
    model = Story
    template_name = 'story_create_template.html'
    fields = ['expired_at', 'body', 'author']
    success_url = reverse_lazy('story_list_url')

class FlowerListView(ListView):
    model = Flower
    context_object_name = "flowers"
    template_name = 'Flower_list_template.html'

class FlowerDetailView(DetailView):
    model = Flower
    context_object_name = 'flower'
    template_name = 'flower_detail_template.html'

class FlowerCreateView(CreateView):
    model = Flower
    template_name = 'flower_create_template.html'
    fields = ['name', 'color']
    success_url = reverse_lazy('flower_list_url')


def CarsView(request):
    cars = Car.objects.all()
    context = {
            'cars': cars,
        }
    return render(request=request, template_name='cars_template.html', context=context)


def CarDetailView(request, car_id):
    car = Car.objects.get(id=car_id)
    context = {
        'car': car
    }
    return render(request=request, template_name='car_detail_template.html', context=context)

def CarFView(request, car_brand):
    car = Car.objects.filter(brand=car_brand)
    context = {
        'car': car
    }
    return render(request=request, template_name='carf_template.html', context=context)


def BouquetsView(request):
    bouquets = Bouquet.objects.all()
    context = {
        'bouquets': bouquets
    }
    return render(request=request, template_name='bouquets_template.html', context=context)


def BouquetsDetailView(request, bouquet_id):
    bouquet = Bouquet.objects.get(id=bouquet_id)
    context = {
        'bouquet': bouquet
    }
    return render(request=request, template_name='bouquet_detail_template.html', context=context)


def BouquetsCreateView(request):
    if request.method == 'GET':
        flowers = Flower.objects.all()
        context = {
            'flowers': flowers
        }
        return render(request=request, template_name='bouquet_create_template.html', context=context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        flowers = request.POST.getlist('flowers')
        bouquet = Bouquet(name=name)
        bouquet.save()
        for flower in flowers:
            bouquet.flowers.add(Flower.objects.get(id=flower))
        bouquet.save()
        return redirect('bouquets_url')

def BouquetUpdateView(request, bouquet_id):
    bouquet = Bouquet.objects.get(id=bouquet_id)
    if request.method == 'GET':
        flowers = Flower.objects.all()
        context = {
            'bouquet': bouquet,
            'flowers': flowers
        }
        return render(request=request, template_name='bouquet_update_template.html', context=context)
    elif request.method == 'POST':
        bouquet.name = request.POST.get('name')
        flowers = request.POST.getlist('flowers')
        bouquet.flowers.clear()
        for flower in flowers:
            bouquet.flowers.add(Flower.objects.get(id=flower))
        bouquet.save()
        return redirect('bouquets_detail_url', bouquet_id)