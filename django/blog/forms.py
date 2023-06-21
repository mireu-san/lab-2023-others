# blog/forms.py
from django import forms
from .models import Post


class PostForm(forms.Modelform):
    class Meta:
        model = Post
        field = (
            "title",
            "writer",
        )
        widget = {"content": forms.widgets.Textarea}
