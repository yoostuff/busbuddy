from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signin")
def login():
    return render_template('signin.html')
    
@app.route("/signup")
def register():
    return render_template('signup.html')

@app.route("/profile")
def dashboard():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run(debug=True)
