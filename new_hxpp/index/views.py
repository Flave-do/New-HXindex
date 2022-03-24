from django.shortcuts import render,reverse,redirect
from django.views.generic import View
# 登录出错给出提示
from django.http import HttpResponse
# django自带用户模型下的表
from django.contrib.auth.models import User
# 登录和登出功能
from django.contrib.auth import logout,login,authenticate
# Create your views here.

# 注册
class Regist(View):
    def get(self,request):
        # 判断用户当前是否登录，如果登录就跳转到首页
        if request.user.is_authenticated:
            # 跳转
            return redirect(reverse('index'))
        return render(request,'register.html')

    def post(self,request):
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        check_password = request.POST.get('check_password','')

        if password != check_password:
            return HttpResponse('密码输入不一致')

        # 判断当前注册帐号是否已经被注册，如果已经被注册，则提示用户重新注册
        exists = User.objects.filter(username=username).exists()
        if exists:
            return HttpResponse('该帐号已被注册')
        User.objects.create_user(username=username,password=password)
        return redirect(reverse('login'))


# 登录
class Login(View):
    def get(self, request):
        return render(request,'login.html')

    def post(self, request):
        pass


# 网站首页
class Index(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


# 用户注销
class LogoutUser(View):
    def get(self, request):
        pass

    def post(self, request):
        pass