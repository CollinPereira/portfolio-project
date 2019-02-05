from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.

def allblogs(request):
    blogs=Blog.objects
    return render(request,'blogs/allblogs.html',{'blogs':blogs})

def description(request,blog_id):
        blog_des=get_object_or_404(Blog,pk=blog_id)
        return render(request,'blogs/description.html',{'blog':blog_des})