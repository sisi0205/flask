from flask import Flask, render_template

app = Flask(__name__)

posts = [{
    'author': 'Lisi Wang',
    'title': "blog 2"
}]

### the two routes are beening handler by the same function
@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

if __name__ == "__main__":
    app.run(debug = True)