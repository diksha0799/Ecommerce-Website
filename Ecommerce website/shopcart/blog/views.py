from django.shortcuts import render
from .models import BlogPost
# Create your views here.
from django.http import HttpResponse

def index(request):
	myposts = BlogPost.objects.all()
	print(myposts)
	return render(request, 'blog/index.html', {'myposts': myposts})



def blogPost(request, id):
	post = BlogPost.objects.filter(post_id = id)[0]
	print(post)
	return render(request, 'blog/blogPost.html', {'post':post})