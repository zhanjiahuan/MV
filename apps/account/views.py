from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template import loader
from apps.account.models import User
from movies import settings


def login_view(request):
    if request.method == 'GET':
        next = request.GET.get('next')
        return render(request, 'login.html', context={'next': next})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    if next:
                        ind = '/'
                    else:
                        ind = next
                    return redirect(ind)
                else:
                    return render(request, 'login.html', {'msg': '您的账号已经被禁用!!!!请与管理员联系'})
            else:
                return render(request, 'login.html', {'msg': '账号密码输入有误!!!'})
        else:
            return render(request, 'login.html', {'msg': '账号密码为空!!!!'})
    else:
        return render(request, '404.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            if username and password and phone:
                user = User.objects.filter(Q(username=username) | Q(phone=phone))
                if user.exists():
                    return render(request, 'register.html', {'msg': '该用户名或者电话已经注册过!!!!'})
                else:
                    user = User.objects.create_user(username=username, password=password,
                                                    phone=phone, email=email, is_active=0)
                    if user:
                        active_url = f'http://127.0.0.1:8000/account/active/?uid={user.id}'
                        content = loader.render_to_string('mail.html',
                                                          request=request,
                                                          context={
                                                              'username': username,
                                                              'active_url': active_url,
                                                          })
                        send_active_mail(subject='123456789', content=content, to=[email])
                        return redirect('/')
                    else:
                        return render(request, 'register.html', {'msg': '注册失败,请核对您的输入!!!'})
        except Exception as e:
            print(e)
            return render(request, '404.html')


def send_active_mail(subject='', content=None, to=None):
    send_mail(subject=subject,
              message='',
              html_message=content,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=to
              )


def active_account(request):
    uid = request.POST.get('uid')
    User.objects.filter(id=uid).update(is_active=1)
    return render('/')


@login_required
def logout_view(request):
    # 退出登录
    logout(request)
    return redirect('/')


@login_required
def update(request):
    user = request.user
    user.save()
    return redirect('/')


def index(request):
    return render(request, 'index.html')
