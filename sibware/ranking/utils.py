import os
from flask import Flask,current_app
from werkzeug.utils import secure_filename
import sys


def save_downloadable(form_pic,uniqu):
    file= form_pic
    filename= secure_filename(file.filename)
    g=uniqu+filename
    upload_path=os.path.join(current_app.root_path, 'static',g)
    file.save(upload_path)
    return g
  

def savep(form_pic,uniqu):
    file= form_pic
    filename= secure_filename(file.filename)
    if checker(filename):
        g=uniqu+filename
        upload_path=os.path.join(current_app.root_path, 'static',g)
        file.save(upload_path)
        return g
    else:
        return 'fail'


def checker(file_nam):
    x= file_nam
    if x.endswith('.pdf'):
        return True
    elif x.endswith('.jpeg'):
        return True
    elif x.endswith('.mp4'):
        return True
    elif x.endswith('.mp3'):
        return True
    elif x.endswith('.jpg'):
        return True
    elif x.endswith('.jpx'):
        return True
    elif x.endswith('.gif'):
        return True
    elif x.endswith('.webp'):
        return True
    elif x.endswith('.x-canon-cr2'):
        return True
    elif x.endswith('.tiff'):
        return True
    elif x.endswith('.bmp'):
        return True
    elif x.endswith('.vnd.adobe.photoshop'):
        return True
    elif x.endswith('.x-icon'):
        return True
    elif x.endswith('.heic'):
        return True
    elif x.endswith('.PNG'):
        return True
    elif x.endswith('.png'):
        return True
    else:
        return False

