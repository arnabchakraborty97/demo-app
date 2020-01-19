from django.shortcuts import render
from .models import Post


def index(request):
	posts = Post.objects.all()
	return render(request, 'blog/index.html', {'posts': posts})


def details(request, post_id):
	post = Post.objects.get(pk=post_id)
	return render(request, 'blog/details.html', {'post': post})


def create(request):
	pass


def edit(request):
	pass


def delete(request):
	pass