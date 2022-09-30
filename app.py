from re import template
from flask import Flask, render_template
app = Flask("__name__")

@app.route("/")
@app.route("/home")
def home ():
    return render_template("home.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

if __name__=='__name__':
    app.run(debug=True)