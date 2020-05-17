import re
from datetime import date
from os import name

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import *
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.contrib.auth.views import auth_login
from . import models
from .models import Login, billdetails, customer
from django.contrib.auth.models import User


def login(request):
    print('sucess')
    return TemplateResponse(request, 'login.html')


def home(request):
    print('success')
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            post = models.data()
            post.username = request.POST.get('username')
            post.password = request.POST.get('password')
            post.save()
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            if name == "admin" and pwd == "admin123":
                b = customer.objects.filter(Joiningdate=date.today()).count()
                print(b)
                a = billdetails.objects.filter(billdate=date.today()).count()
                print(a)
                return render(request, 'admin.html', {"alldata": a, "cou": b})
            if Login.objects.filter(username=name).exists():
                lev = Login.objects.get(username=name)
                print(lev)
                if lev.level == "m":
                    b = customer.objects.filter(Joiningdate=date.today()).count()
                    print(b)
                    a = billdetails.objects.filter(billdate=date.today()).count()
                    print(a)
                    return render(request, 'manager.html', {"alldata": a, "cou": b})
                elif lev.level == "c":
                    cc = customer.objects.all()
                    return render(request, 'crehome.html', {"alldata": cc})
                elif lev.level == "cus":
                    return render(request, 'cushome.html')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return render(request, 'login.html')


def pswrd(request):
    return render(request, 'resetpwd.html')


def shop(request):
    if request.method == 'POST':
        print("sdfgth")
        if request.POST.get('sub'):
            post = models.sub()
            post.sub = t
            post.save()
        return render(request, 'shops.html', {"alldata": t})
    else:
        return render(request, 'shops.html')


def sel(request):
    return render(request, 'selshop.html')


def zera(request):
    if request.method == 'POST':
        if request.POST.get('billamt') and request.POST.get('billnum') and request.POST.get('billdate'):
            post = models.billdetails()
            post.billamt = request.POST.get('billamt')
            post.billnum = request.POST.get('billnum')
            post.billdate = request.POST.get('billdate')
            post.save()
            return render(request, 'zera.html')
    else:
        return render(request, 'zera.html')


def credit(request):
    if request.method == 'POST':
        if request.POST.get('amount') and request.POST.get('creditpoint'):
            post = models.credit()
            post.amount = request.POST.get('amount')
            post.creditpoint = request.POST.get('creditpoint')
            post.save()
            global a
            a = models.credit.objects.all()
        return render(request, 'credit.html', {"alldata": a, "message": "Credit set successfully"})

    return cred(request)


def cred(request):
    return render(request, 'credit.html', {"alldata": a})


def confirm(request):
    return render(request, 'confirmpwd.html')


def cre(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('mobile') and request.POST.get('email'):
            post = models.Login()
            post.name = request.POST.get('name')

            post.mobile = request.POST.get('mobile')

            post.email = request.POST.get('email')

            post.level = 'c'
            post.save()

            return render(request, 'cre.html',{ "message": "Successfully added CRE"})
    global a
    a = Login.objects.filter(level="c")
    print(a)

    return cr(request)


def cr(request):
    return render(request, 'cre.html', {"alldata": a})


def bill(request):
    if request.method == 'POST':
        if request.POST.get('mobile') and request.POST.get('billnum') and request.POST.get(
                'billamt') and request.POST.get('name'):
            post = models.customer()
            post.mobile = request.POST.get('mobile')
            post.name = request.POST.get('name')
            post.save()
            post = models.billdetails()
            post.billnum = request.POST.get('billnum')
            post.billamt = request.POST.get('billamt')
            post.save()
            post = models.Login()
            post.name = request.POST.get('name')
            post.mobile = request.POST.get('mobile')
            post.level = 'cus'
            post.save()
        return render(request, 'addcust.html', {"message": "Successfully added"})
    else:
        return TemplateResponse(request, 'addcust.html')


def cus(request):
    if request.method == 'POST':
        if request.POST.get('billnum') and request.POST.get('billamt'):
            post = models.billdetails()
            post.billnum = request.POST.get('billnum')
            post.billamt = request.POST.get('billamt')
            post.save()
        return render(request, 'morecust.html')
    else:
        return render(request, 'morecust.html')


def admin(request):
    return render(request, 'admin.html')


def crehome(request):
    return render(request, 'crehome.html')


def cushome(request):
    return render(request, 'cushome.html')


def type(request):
    if request.method == 'POST':
        if request.POST.get('type'):
            post = models.type()
            post.type = request.POST.get('type')
            post.save()
        return render(request, 'type.html')
    else:
        return render(request, 'type.html')


def cree(request):
    if request.method == 'POST':
        if request.POST.get('mobile'):
            mob = request.POST.get('mobile')
            print(mob)
            if customer.objects.filter(mobile=mob).exists():
                k = customer.objects.get(mobile=mob)
                print(k)
                return render(request, 'morecust.html', {"alldata": k})
            else:
                return render(request, 'crepage.html', {"message": "New customer.. Please add"})
        post = models.billdetails()
        post.billnum = request.POST.get('billnum')
        post.billamt = request.POST.get('billamt')
        post.save()
        return render(request, 'crepage.html')
    global c
    c = customer.objects.all()
    return cc(request)


def cc(request):
    return render(request, 'crepage.html', {"alldata": c})


def cust(request):
    if request.method == 'POST':
        if request.POST.get('Name'):
            n = request.POST.get('Name')
            print(n)
            if models.Shop.objects.filter(Name=n).exists():
                global t
                t = models.Shop.objects.get(Name=n)
                print(t)
                return shop(request)
        d = models.data.objects.all()
        s = d[len(d) - 1]
        post = models.sub()
        post.user = s
        post.sub = request.POST.get('sub')
        post.save()
        return render(request, 'cust.html')
    else:
        return render(request, 'cust.html')


def report(request):
    if request.method == 'POST':
        print('fgvbhnj')
        if request.POST.get('report'):
            a = request.POST.get('report')
            print(a)
        return render(request, 'report.html')
    else:
        return render(request, 'report.html')


def sub(request):
    d = models.data.objects.all()
    s = d[len(d) - 1]
    l = models.sub.objects.filter(user=s)
    print(l)
    global n
    n = request.POST.get('name')
    if n == 'ZERA':
        return render(request, 'zera.html')
    post = models.billdetails()
    post.billamt = request.POST.get('billamt')
    post.billnum = request.POST.get('billnum')
    post.billdate = request.POST.get('billdate')
    post.save()
    print(n)
    if n == "KFC":
        return redirect("selshop.html")
    return render(request, 'subshops.html', {"alldata": l})


def viewcus(request):
    a = Login.objects.filter(level="cus")
    print(a)
    return render(request, 'viewcus.html', {"alldata": a})


def adcredit(request):
    return render(request, 'admincredit.html')


def mm(request):
    return render(request, 'manager.html')


def add(request):
    return render(request, 'addshop.html', {"alldata": m, "shop": s})


def adreport(request):
    return render(request, 'adminreport.html')


def mngr(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('mobile') and request.POST.get('email'):
            post = models.Login()
            post.name = request.POST.get('name')
            post.mobile = request.POST.get('mobile')
            post.email = request.POST.get('email')
            post.level = 'm'
            post.save()
            return render(request, 'addmanager.html', {"message": "Successfully added"})
    else:
        return TemplateResponse(request, 'addmanager.html')


def adshop(request):
    if request.method == 'POST':
        if request.POST.get('Name') and request.POST.get('Phone') and request.POST.get('Email') and request.POST.get(
                'logo') and request.POST.get('type') and request.POST.get('managerid') and request.POST.get('category'):
            print('cc')
            post = models.Shop()
            post.Name = request.POST.get('Name')
            post.Phone = request.POST.get('Phone')
            post.Email = request.POST.get('Email')
            post.logo = request.POST.get('logo')
            post.type = request.POST.get('type')
            post.managerid = request.POST.get('managerid')
            post.category = request.POST.get('category')
            post.save()
        return add(request)
    global m
    global s
    m = models.type.objects.all()
    print(m)
    s = models.Shop.objects.all()
    return add(request)


def viewshop(request):
    b = models.Shop.objects.all()
    print(b)
    return render(request, 'viewshop.html', {"alldata": b})


def viewmgr(request):
    c = Login.objects.filter(level="m")
    print(c)
    return render(request, 'viewmngr.html', {"alldata": c})


def feed(request):
    d = models.data.objects.all()
    s = d[len(d) - 1]
    if customer.objects.filter(mobile=s).exists():
        t = customer.objects.get(mobile=s)
        t.feedback = request.POST.get('feedback')
        t.save()
        return render(request, 'feedback.html', {"message": "Successfully added"})
    else:
        return render(request, 'feedback.html')


def viewfb(request):
    f = customer.objects.all()
    print(f)
    return render(request, 'viewfeed.html', {"alldata": f})


def viewcre(request):
    g = Login.objects.filter(level="c")
    print(g)
    return render(request, 'viewcre.html', {'alldata': g})


def offers(request):
    return render(request, 'offers.html')
