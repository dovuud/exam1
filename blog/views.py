from django.shortcuts import render
from .models import Category,Tag,Post,Author
# Create your views here.

def home_page(request):
    posts = Post.obj.all().order_by('-id')[:5]
    context ={'posts':posts}
    return render(request,'index.html',context)
    
