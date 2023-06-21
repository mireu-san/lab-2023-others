from django.urls import path
from . import views

# from blog.views import Index

app_name = "blog"

urlpatterns = [
    # path(패턴, 매핑)
    # path("", views.index) # FBV
    # 글 조회
    path("", views.Index.as_view(), name="list"),
    # 글 작성
    path("write/", views.write, name="write"),
    # 글 수정
    # 글 삭제
    # 코멘트 작성
    # 코멘트 삭제
]
