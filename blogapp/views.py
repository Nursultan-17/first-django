from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'  # Под каким именем данные будут отзыватся в html
    template_name = 'post_list_template.html'
# Create your views here.
