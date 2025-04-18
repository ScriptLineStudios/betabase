from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    response = make_response(render_template("test.html"))
    print(response)
    return response


if __name__ == "__main__":
    app.run(debug=True)