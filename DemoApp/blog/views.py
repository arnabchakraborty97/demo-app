from django.shortcuts import render
from .forms import PostForm
from .models import Post


def index(request):
	posts = Post.objects.all()
	return render(request, 'blog/index.html', {'posts': posts})


def details(request, post_id):
	post = Post.objects.get(pk=post_id)
	return render(request, 'blog/details.html', {'post': post})


def create(request):
	form = PostForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		post = form.save(commit=False)
		post.user = request.user
		post.save()
		return render(request, 'blog/details.html', {'post': post})
	return render(request, 'blog/post_form.html', {'form': form})


def edit(request, post_id):
	post = Post.objects.get(pk=post_id)

	if request.method == "POST":
		form = PostForm(request.POST, instance=post)

		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return render(request, 'blog/details.html', {'post': post})
	else:
		form = PostForm(instance=post)
		return render(request, 'blog/post_form.html', {'form': form})


def delete(request, post_id):
	post = Post.objects.get(pk=post_id)
	post.delete()

	posts = Post.objects.all()
	return render(request, 'blog/index.html', {'posts': posts, 'success': 'Successfully deleted the post'})