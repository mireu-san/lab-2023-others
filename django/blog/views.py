from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse

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
    return render(request, "blog/post_form.html", {"form": form})


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


class Update(UpdateView):
    model = Post
    template_name = "blog/post_edit.html"
    fields = ["title", "content"]
    # success_url = reverse_lazy("blog:list")

    # initial 기능 사용 -> form 에 값을 미리 넣어주기 위해서 # reset 아님. initial.
    def get_initial(self):
        # super = approaching parent class to inherit it
        initial = super().get_initial()  # updateView(generic view)에서 제공하는 initial 딕셔너리.
        post = self.get_object()  # pk 기반으로.
        initial["title"] = post.title
        initial["content"] = post.content
        return initial

    def get_success_url(self):
        post = self.get_object()  # pk 기반으로 현재 객체 가져오기 # self 는 class 로 만든, 현재 찍어준 객체
        # return reverse_lazy("blog:detail", kwargs={"pk: post.pk"})
        return reverse("blog:detail", kwargs={"pk": post.pk})


class Delete(DeleteView):  # 지우는 화면 따로 구성할 필요는 없음.
    model = Post  # Post 에 있는 값을 지울예정
    success_url = reverse_lazy("blog:list")
    # 어디서 실행 시킬까? 상세페이지 내부에서.
