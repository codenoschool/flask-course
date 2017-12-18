from app import app, db
from app.schemas.post import Post
from flask import render_template, request, redirect, url_for

@app.route("/")
def index():

    return "Hello World!"

@app.route("/add/document", methods=["GET", "POST"])
def document():
    if request.method == "POST":
        new_post = Post(document=request.form["document"])
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for("get_document", id=new_post.id))

    return render_template("add_document.html")

@app.route("/document/<int:id>")
def get_document(id):

    post = Post.query.get(id)
    bodytoHTML = post.document.replace("\n", "<br>")

    return render_template("document.html", post=post, body=bodytoHTML)