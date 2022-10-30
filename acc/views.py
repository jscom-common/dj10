from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib import messages

# Create your views here.
def index(request) :
    return render(request, 'acc/index.html')

def ulogin(request) :
    if request.method == 'POST' :
        un = request.POST.get('uname')
        up = request.POST.get('upass')
        u = authenticate(username=un, password=up)
        if u :
            login(request, u)
            messages.success(request, f"{un}님 환영합니다!")
            return redirect('acc:index')
        else :
            messages.info(request, '계정 정보가 일치하지 않습니다.')
    return render(request, 'acc/login.html')

def ulogout(request) :
    logout(request)
    messages.info(request, '로그아웃 되었습니다.')
    return redirect('acc:index')

def profile(request) :
    return render(request, 'acc/profile.html')

def delete(request) :
    u = request.user
    up = request.POST.get('upass')
    if check_password(up, u.password) :
        u.pic.delete()
        u.delete()
        messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
        return redirect('acc:index')
    else :
        messages.warning(request, '비밀번호가 일치하지 않습니다.')
    return redirect('acc:profile')

def signup(request) :
    if request.method == 'POST' :
        un = request.POST.get('uname')
        um = request.POST.get('umail')
        uc = request.POST.get('ucom')
        pi = request.FILES.get('upic')
        up = request.POST.get('upass')
        try :
            User.objects.create_user(username=un, email=um, comment=uc, pic=pi, password=up)
            messages.success(request, '회원가입에 성공하였습니다.')
            return redirect('acc:login')
        except :
            messages.warning(request, '회원가입에 실패하였습니다.')
    return render(request, 'acc/signup.html')

def update(request) :
    if request.method == 'POST' :
        u = request.user
        uc = request.POST.get('ucom')
        ue = request.POST.get('umail')
        up = request.FILES.get('upic')
        u.comment, u.email = uc, ue
        if up :
            u.pic = up
        u.save()
        messages.success(request, '성공적으로 업데이트 되었습니다.')
        return redirect('acc:profile')
    return render(request, 'acc/update.html')

def chpass(request) :
    u = request.user
    cp = request.POST.get('cpass')
    if check_password(cp, u.password) :
        np = request.POST.get('npass')
        u.set_password(np)
        u.save()
        messages.success(request, '성공적으로 비밀번호가 바뀌었습니다.')
        return redirect('acc:logout')
    else :
        messages.warning(request, '비밀번호가 맞지 않습니다.')
        return redirect('acc:update')
