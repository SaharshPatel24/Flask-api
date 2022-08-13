from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World From Flask Server!"

@app.route("/admin")
def admin():    
    return " Hello from Admin Server! "     