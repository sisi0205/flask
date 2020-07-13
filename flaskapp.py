from flask import Flask

app = Flask(__name__)

### the two routes are beening handler by the same function
@app.route("/")
@app.route("/home")
def hello():
    return "<h1> Home Page </h1>"

@app.route("/about")
def about():
    return "<h1> About Page </h1>"

if __name__ == "__main__":
    app.run(debug = True)