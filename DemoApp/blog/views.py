from django.shortcuts import render
from .models import Post


def index(request):
	posts = Post.objects.all()
	return render(request, 'blog/index.html', {'posts': posts})


def details(request):
	pass


def create(request):
	pass


def edit(request):
	pass


def delete(request):
	pass