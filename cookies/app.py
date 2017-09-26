from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/")
def index():

    return "Hello World!"

@app.route("/cookie/set")
def set_cookie():
    resp = make_response(render_template("index.html"))
    resp.set_cookie("username", "CodeNoSchool")

    return resp

@app.route("/cookie/read")
def read_cookie():
    username = request.cookies.get("username", None)

    if username == None:
        return "The cookie doesn't exist."

    return username

if __name__ == "__main__":
    app.run(debug=True)
