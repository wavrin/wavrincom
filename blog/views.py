from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):
	latest_post_list = Post.objects.all().order_by('-pub_date')[:4]
	context = {'latest_post_list': latest_post_list}
	return render(request, 'blog/index.html', context)

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'blog/detail.html', {'post': post})