from flask import Blueprint, render_template, request, redirect, url_for, abort, current_app, json, flash, send_from_directory, send_file
from model import db
from model import Upload
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import os

upload = Blueprint("upload", __name__, template_folder="routes")

@upload.route('/')
def index():
    files = os.listdir(current_app.config['UPLOAD_DIRECTORY'])
    images = []

    for file in files:
        extension = os.path.splitext(file)[1].lower() 
        if extension in current_app.config['ALLOWED_EXTENSIONS']:
            images.append(file)

    print(files)

    return render_template('index.html', images=images)

#upload file
@upload.route('/upload', methods=['POST'])
def upload_file():
    try:
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1].lower() 
        print(extension)

        if file:

            if extension not in current_app.config['ALLOWED_EXTENSIONS']:
                return 'File is not an image.'

            file.save(os.path.join(current_app.config['UPLOAD_DIRECTORY'], 
                file.filename))
            upload = Upload(filename=(os.path.join(
                current_app.config['UPLOAD_DIRECTORY'], 
                file.filename)), 
                fp=os.path.abspath(current_app.config['UPLOAD_DIRECTORY']))
            db.session.add(upload)
            db.session.commit()
    except RequestEntityTooLarge:
        return 'File is larger than the 16MB limit.'

    return redirect('/')

#display files
@upload.route('/serve-image/<filename>', methods=['GET'])
def serve_image(filename):
    return send_from_directory(current_app.config['UPLOAD_DIRECTORY'], filename)

#download file
@upload.route('/download-image/<filename>', methods=['GET'])
def download_image(filename):
    try:
        return send_from_directory(current_app.config['UPLOAD_DIRECTORY'], filename, as_attachment=True)
    except FileNotFoundError:
        abort (404)

@upload.route('/single-image/<filename>', methods=['GET'])
def single_image(filename):
    return render_template('target.html', user_img=filename)





