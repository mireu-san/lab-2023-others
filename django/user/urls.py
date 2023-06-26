from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    # user/
    path("", views.Registration.as_view(), name="register"),
    path("register/", views.Registration.as_view(), name="register"),
    # 로그인
    path("login/", views.Login.as_view(), name="login"),
]
