from app import app
from flask import request, render_template, redirect, url_for, send_file,send_from_directory,flash
import os
from PIL import Image
from .Neural_network_meta import *

@app.route('/')
@app.route('/start_page')
def start_page():
    user = {'username': 'Romal'}
    return render_template('start_page.html', title='Home', user=user)

@app.route("/image_classifier")
def show_template(file=None,image_name=None,image_labels=None):
    return render_template('upload_data.html', 
                            file=file,
                            image_name=image_name,
                            image_labels=image_labels)

@app.route("/image_classifier",methods=["POST"])
def image_upload():

    uploaded_file=request.files['file']
    if uploaded_file.filename!='':
        file_ext = path.splitext(uploaded_file.filename)[1]
        if file_ext in app.config['UPLOAD_EXTENSIONS']:
            uploaded_file.save(path.join(app.config['UPLOAD_FOLDER'],uploaded_file.filename))
            path_to_file=path.join(app.config['UPLOAD_FOLDER'],uploaded_file.filename)

    img=Image.open(uploaded_file)
    image_labels=get_label(img)
    print(image_labels,flush=True)

    return render_template('upload_data.html', 
                           file=uploaded_file.filename,
                           image_name=uploaded_file.filename,
                           image_labels=image_labels)
    #redirect(url_for('show_template',file=uploaded_file.filename,image_name=uploaded_file.filename))

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)