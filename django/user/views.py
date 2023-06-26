from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.urls import reverse
from django.views import View
from .models import User
from .forms import RegisterForm, LoginForm


# Create your views here.

# User 관련된 기능
# 회원가입
# 로그인
# 탈퇴


### Registration
class Registration(View):
    def get(self, request):
        # 회원가입 페이지
        # 정보를 입력할 폼을 보여주어야 한다.
        form = RegisterForm()
        context = {"form": form}
        return render(request, "user/user_register.html", context)

    # views.py in Registration class post method

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save ModelForm directly
            password = form.cleaned_data.get("password")
            user.set_password(password)  # Set hashed version of password
            user.save()  # Save the user object
            return redirect("blog:list")


class Login(View):
    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, "user/user_login.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("blog:list")

            form.add_error(None, "아이디가 없습니다")

        context = {"form": form}

        return render(request, "user/user_login.html", context)


### Logout
class Logout(View):
    def get(self, request):
        logout(request)
        # request.user.email
        return redirect("blog:list")
