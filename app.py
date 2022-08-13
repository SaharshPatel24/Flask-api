from flask import Flask, render_template

UPLOAD_FOLDER = 'C:/Users/ashar/OneDrive/Desktop/Sketch-Flask-App/static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"


@app.route('/')
def home():
    return render_template('index.html')
