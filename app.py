from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_extension(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Process the file as needed
            success_message = "File uploaded successfully!"
            return render_template('index.html', success=success_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)