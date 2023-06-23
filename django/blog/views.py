from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Post, Comment, HashTag
from .forms import PostForm, CommentForm, HashTagForm
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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     post = self.get_object()
    #     comments = Comment.objects.filter(post=post)
    #     context["comments"] = comments
    #     return context


class Update(UpdateView):
    model = Post
    template_name = "blog/post_edit.html"
    fields = ["title", "content"]

    def get_initial(self):
        initial = super().get_initial()
        post = self.get_object()
        initial["title"] = post.title
        initial["content"] = post.content
        return initial

    def get_success_url(self):
        post = self.get_object()
        return reverse("blog:detail", kwargs={"pk": post.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()  # make sure the form is in the context
        return context


class Delete(DeleteView):  # 지우는 화면 따로 구성할 필요는 없음.
    model = Post  # Post 에 있는 값을 지울예정
    success_url = reverse_lazy("blog:list")
    # 어디서 실행 시킬까? 상세페이지 내부에서.


class DetailView(View):
    def get(self, request, pk):
        # Get the post
        post = Post.objects.get(pk=pk)

        # Get the comments for the post
        comments = Comment.objects.filter(post=post)

        # hashtag
        # 이 post 는 hashtag 에 해당되는 것만 가져올 예정.
        hashtags = HashTag.objects.filter(post=post)

        # Create an instance of the form (in this example, I am assuming CommentForm)
        comment_form = CommentForm()

        hashtag_form = HashTagForm()

        # Include the form in the context
        # context = {"post": post, "comments": comments, "form": form}
        context = {
            "post": post,
            "comments": comments,
            "hashtags": hashtags,
            "comment_form": comment_form,
            "hashtag_form": hashtag_form,
        }

        # Render the template
        return render(request, "blog/post_detail.html", context)


### Comment
class CommentWrite(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            # Valid form input
            content = form.cleaned_data["content"]
            post = Post.objects.get(pk=pk)
            comment = Comment.objects.create(
                post=post,
                content=content,
            )
            return redirect("blog:detail", pk=pk)
        else:
            # Invalid form input
            # add a return statement to render an error page
            # or redirect back to the detail page
            return redirect("blog:detail", pk=pk)  # Redirecting back as an example


# class CommentDelete(DeleteView):
#     model = Comment

#     def get_success_url(self):
#         return reverse_lazy("blog:detail", kwargs={"pk": self.object.post.pk})


class CommentDelete(View):
    def post(self, request, pk):
        # 지울 객체를 찾아야 함 -> 댓글 객체
        comment = Comment.objects.get(pk=pk)
        # 상세페이지로 돌아가기
        post_id = comment.post.id
        # 삭제
        comment.delete()

        return redirect("blog:detail", pk=post_id)


### HashTag
class HashTagWrite(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = HashTagForm(request.POST)

        if form.is_valid():
            hashtag = form.save(commit=False)
            hashtag.post = post
            hashtag.save()
            return redirect("blog:detail", pk=post.pk)
        else:
            # 폼에 문제가 있다면, 오류 메시지를 출력합니다.
            pass


class HashTagDelete(View):
    def post(self, request, pk):
        hashtag = HashTag.objects.get(pk=pk)
        hashtag.delete()
        return redirect("blog:detail", pk=hashtag.post.pk)
