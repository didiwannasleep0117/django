
from .models import Event, Guest
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# crate your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        id = request.POST.get('id','')
        password = request.POST.get('password','')
        user = auth.authenticate(username = id,password = password)
        if user is not None:
            auth.login(request,user) #登錄要求
            request.session['user'] = id #新增session，並對應user值為id
            response = HttpResponseRedirect('login_ok/')  #新增
            #response.set_cookie('user',id,3600)  #新增cookie
            return response
        else:
            return render(request,"login.html",{'error':'帳號或密碼輸入錯誤'})
    elif request.method == 'GET':
        return render(request,"index.html")
    else:
        print("request.method:", request.method)
@login_required

def login_ok(request):  
    #id = request.COOKIES.get('user','') 
    id = request.session.get('user','') 
    return render(request,'login_ok.html',{'user':id})

def table(request):
    events = Event.objects.all()
    guests = Guest.objects.all()
    return render(request,'table.html',{'event':events}, {'guest':guests})
