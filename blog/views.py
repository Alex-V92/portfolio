from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    blog = Blog.objects.order_by('-date')
    return render(request, 'blog/blog_home.html', {'blog':blog})
