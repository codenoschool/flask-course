from flask import Flask, render_template, abort

app = Flask(__name__)

admin_user = ""

@app.route("/")
def index():

    return "Hello World!"

@app.route("/admin")
def admin():
    if not admin_user:
        abort(403)

    return "Welcome {}!".format(admin_user)

@app.errorhandler(404)
def page_not_found(err):

    return render_template("page_not_found.html"), 404

@app.errorhandler(403)
def forbidden(err):

    return render_template("forbidden.html"), 403

if __name__ == "__main__":
    app.run(debug=True)
