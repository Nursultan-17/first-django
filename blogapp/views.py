from django.shortcuts import render
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

