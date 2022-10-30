from django.shortcuts import render, redirect
from .models import Board
from acc.models import User
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def index(request) :
    pg = request.GET.get('page', 1)
    cate = request.GET.get('cate', '')
    kw = request.GET.get('kw', '')
    if kw :
        if cate == 'sub' :
            b = Board.objects.filter(subject__startswith=kw)
        elif cate == 'wri' :
            try :
                u = User.objects.get(username=kw)
                b = Board.objects.filter(writer=u)
            except :
                b = Board.objects.none()
        elif cate == 'con' :
            b = Board.objects.filter(content__contains=kw)
    else :
        b = Board.objects.all()
    pag = Paginator(b,5)
    obj = pag.get_page(pg)
    context = {
        'bset' : obj,
        'cate' : cate,
        'kw' : kw
    }
    return render(request, 'board/index.html', context)

def detail(request, bpk) :
    b = Board.objects.get(id=bpk)
    context = {
        'b' : b
    }
    return render(request, 'board/detail.html', context)

def delete(request, bpk) :
    b = Board.objects.get(id=bpk)
    if (b.writer == request.user) :
        b.delete()
        return redirect('board:index')
    else :
        pass # 마지막날
    return redirect('board:detail', bpk)

def create(request) :
    if request.method == 'POST' :
        s = request.POST.get('subject')
        c = request.POST.get('content')
        try :
            Board(subject=s, content=c, writer=request.user, pubdate = timezone.now()).save()
            return redirect('board:index')
        except :
            pass
    return render(request, 'board/create.html')

def modify(request, bpk) :
    b = Board.objects.get(id=bpk)
    if b.writer != request.user :
        return redirect('board:index')
        pass # 메세지~
    context = {
        'b': b
    }
    if request.method == 'POST' :
        s = request.POST.get('subject')
        c = request.POST.get('content')
        try :
            b.subject, b.content = s, c
            b.save()
            return redirect('board:detail', bpk)
        except :
            pass # 마지막에 혼자서!
    return render(request, 'board/modify.html', context)

def likey(request, bpk) :
    b = Board.objects.get(id=bpk)
    b.likey.add(request.user)
    return redirect('board:detail', bpk)

def cancel(request, bpk) :
    b = Board.objects.get(id=bpk)
    b.likey.remove(request.user)
    return redirect('board:detail', bpk)
