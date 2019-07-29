from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .models import NewBlog
from .form import BlogPost
from .form import BlogPostForm

def home(request):
    blogs = NewBlog.objects #쿼리셋
    #블로그 모든 글들을 대상으로
    blog_list = NewBlog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해준다
    posts = paginator.get_page(page)
    return render(request,'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(NewBlog, pk=blog_id)
    return render(request, 'detail.html',{'blog':details})

def new(request):   #new.html 띄워주는 함수
    return render(request,'new.html')

def create(request):       #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()         #위에서 blog 객체에 넣은 정보를 데이터베이스에 저장해라
    return redirect('/blog/'+str(blog.id))

def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        # is_valid() 란?
        # form의 내용이 형식에 맞게 잘 입력됬을 시 true 반환
        # 만약 아무 내용도 입력하지 않고 제출하려하면 예외 처리해줌
        if form.is_valid():
            # 모델 객체를 반환하되 저장하지 않고 가져온다
            # 여기서 post는 블로그형 객체
            post = form.save(commit=False)
            # 현재 시간 넣어주기
            post.pub_date = timezone.now()
            # save()를 이용하여 저장
            post.save()
            return redirect('home')
    else:
        # 비어있는 객체를 반환해줌
        form = BlogPostForm()
        return render(request, 'new.html', {'form':form})
