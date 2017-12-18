from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import os

DBURI = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DBURI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    document = db.Column(db.Text(length=None), nullable=False)

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

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)