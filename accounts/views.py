from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST['username']
            password = request.POST['password1']
            user = User.objects.create_user(username=username, password=password)
            auth.login(request, user)
            return redirect('home')
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(request, username=username, password=password) #DB에 있는 회원이 맞는지 확인
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:       #없는 회원이라면 에러메시지(임의) 띄워라
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)    #접속해 있는 회원 로그아웃 시켜라
        return redirect('home')
    return render(request, 'login.html')
