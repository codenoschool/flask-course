from flask import Flask, jsonify

app = Flask(__name__)

cns = [
        {
            "id": 1,
            "title": "1.- Hello World - Curso Flask"
            },
        {
            "id": 2,
            "title": "2.- Metodo Run - Curso Flask"
            }
        ]

isc = [
        {
            "id": 1,
            "title": "1.- Hello World - Curso Flask"
            },
        {
            "id": 2,
            "title": "2.- Metodo Run - Curso Flask"
            }
        ]

@app.route("/")
def index():

    return "Hello World!"

@app.route("/api/v1/videos/")
def get_all_videos():

    return jsonify({"videos": {"cns": cns, "isc": isc}})

if __name__ == "__main__":
    app.run(debug=True)
