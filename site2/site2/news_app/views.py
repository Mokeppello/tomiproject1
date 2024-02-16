from django.shortcuts import render,get_object_or_404

from .models import Post

def home_page(request):
    latest_news = Post.objects.order_by('-created_at')[:4]
    return render(request,'./index.html',{'latest_news':latest_news})

def news_detail_page(request,pk):
    news = get_object_or_404(Post, pk=pk)
    return render(request,'./news-detail.html',{'news':news})

def news_page(request):
    latest_news = Post.objects.order_by('-created_at')
    return render(request,'./news.html',{'latest_news':latest_news})

