from flask import Flask, render_template

app = Flask('app')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/secondlpp')
def secondlpp():
    return render_template("secondlpp.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")


app.run(host='0.0.0.0', port=8080)