from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request): #new.html을 띄워주는 함수
    return render(request, "new.html")

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog=Blog()      #Blog라는 클래스에서 blog라는 객체 형성
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()   #작성한 시점을 넣어주는..꿀팁!
    blog.save()     #객체를 데이터베이스에 저장하라는 메소드!!
    return redirect('/blog/'+str(blog.id))
    #redirect함수는 프로그램 밖에 있는 URL도 연결 할 수 있음

def portfolio(request):
    return render(request, "portfolio.html")