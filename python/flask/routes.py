from flask import render_template, request, redirect, url_for
from app import app, db
from models import Post


@app.route("/")
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


@app.route("/post/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("create.html")


@app.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == "POST":
        post.title = request.form["title"]
        post.content = request.form["content"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", post=post)


@app.route("/post/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("index"))
