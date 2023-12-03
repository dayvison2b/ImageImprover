from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_extension(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')
    
        file = request.files['file']
        
        if file.filename == '':
            return render_template('index.html', error='No selected file')

        if file and allowed_extension(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            return render_template('index.html', success='File uploaded successfully', filename=filename)
        
        else:
            return render_template('index.html', error='Invalid file type')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)