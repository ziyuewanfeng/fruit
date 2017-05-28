# _*_coding:utf-8
from django.shortcuts import render, render_to_response
from django.template import loader, RequestContext
from django.http import HttpResponse
import models,views
from django.views.decorators import csrf


# Create your views here.

def index(request):
    # Tem=loader.get_template("main/index.html")
    # return HttpResponse(Tem)
    return render_to_response("main/index.html")

def checkout(request):
    return render_to_response("main/checkout.html")

def register(request):
    com_pass=models.com_pass.objects.all()
    context={"com_pass":com_pass}
    if request.POST:
        if request.POST['chose_buy_or_sell']=='sell':
            user=models.sell_user()
            user.name=request.POST['name']
            user.sex=request.POST['radio']
            user.user_name=request.POST['username']
            password=request.POST['password']
            password_1=request.POST['again_password']
            if password!=password_1:
                result={}
                result['res']="两次密码不同"
                return render(request,"main/register.html",result)
            else:
                user.password=password
            user.address=request.POST['address']
            user.identity_num=request.POST['identity']
            user.com_pass=models.com_pass.objects.get(pk=request.POST['chose_com_pass'])
            user.save()
            result={}
            result['rlt']=request.POST['username']
            return render(request, "main/index.html", result)
        elif request.POST['chose_buy_or_sell']=='buy':
            user_buy=models.buy_user()
            user_buy.name=request.POST['name']
            user_buy.sex=request.POST['radio']
            user_buy.user_name=request.POST['username']
            password=request.POST['password']
            password_1=request.POST['again_password']
            if password!=password_1:
                result={}
                result['res']="两次密码不同"
                return render(request,"main/register.html",result)
            else:
                user_buy.password=password
            user_buy.address=request.POST['address']
            user_buy.save()
            result={}
            result['rlt']=request.POST['username']
            return render(request, "main/index.html", result)
    return render(request,"main/register.html",context)#注册

def login(request):
    ret = {}
    if request.POST:
        username = request.POST['Username']
        password=request.POST['Password']
        if models.sell_user.objects.filter(user_name=username,password=password):
            ret['rlt']=username
            return render(request, "main/index.html", ret)
        elif models.buy_user.objects.filter(user_name=username,password=password):
            ret['rlt']=username
            return render(request, "main/index.html", ret)
        else:
            ret['rlt']="登录失败，请检查用户名和密码"

    return render(request, "main/account.html", ret)







