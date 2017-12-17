from flask import Flask, abort, render_template

app = Flask(__name__)

admin = ""

@app.route("/")
def index():

    return "Hello World!"

@app.route("/admin")
def protected_page():
    if not admin:
        abort(403)

    return "Welcome " + admin

@app.errorhandler(404)
def page_not_found(error):

    return render_template("page_not_found.html"), 404

@app.errorhandler(403)
def forbidden(error):

    return render_template("forbidden.html"), 403

if __name__ == "__main__":
    app.run(debug=True)
