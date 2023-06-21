from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('Index page GET')
#     # 나머지 요청
#     # 에러, 예외처리
#     return HttpResponse('invalid request')


class Index(View):
    def get(self, request):
        # return HttpResponse('Index page GET class')

        # 데이터베이스 접근해서 값 가져오기.
        # 게시판에 글 보여줘야 하므로 DB에서 '값 조회'
        # all()
        # context = DB 에서 가져온 값.
        post_objs = Post.objects.all()

        context = {"posts": post_objs}
        return render(request, "blog/board.html", context)


# write
# post - form
# 글 작성 화면
def write(request):
    if request.method == "POST":
        # form
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("blog:list")
    # & beware of indentation
    form = PostForm()
    return render(request, "blog/write.html", {"form": form})


# Django 자체의 클래스 뷰 기능도 강력, 편리
# model, template_name, context_object_name,
# paginate_by, form_class, form_valid(), get_queryset()
# django.views.generic -> ListView
class List(ListView):
    model = Post  # model
    template_name = "blog/post_list.html"  # template
    context_object_name = "posts"  # name of variable value


class Write(CreateView):
    model = Post  # model
    form_class = PostForm  # form
    success_url = reverse_lazy("blog:list")  # url to send when succeed


class Detail(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"  # name of variable = "post"
