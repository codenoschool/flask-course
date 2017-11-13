from flask import Flask

app = Flask(__name__)


request_status = ""

@app.before_request
def before_request():
    global request_status

    request_status += "Before request"
    print("Before request.")

@app.after_request
def after_request(response):
    global request_status

    request_status = request_status + " After request"
    print("After request")

    return response

@app.teardown_request
def teardown_request(response):
    global request_status

    request_status = request_status + " Teardown request"
    print("Teardown request.")

    return response

@app.route("/")
def index():

    return "Request status: " + request_status

if __name__ == "__main__":
    app.run(debug=True)
