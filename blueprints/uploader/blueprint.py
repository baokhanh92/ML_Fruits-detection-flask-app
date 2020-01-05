from flask import Blueprint, render_template, request, redirect, send_from_directory
from keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input
from werkzeug import secure_filename
import tensorflow as tf
import numpy as np
import os

UPLOAD_FOLDER = 'uploads'

model = tf.keras.models.load_model('models/model.h5')

uploader = Blueprint('uploader', __name__)

# IMAGE_SIZE = 100
IMAGE_SIZE = 192


@uploader.route('/uploader', methods=['GET', 'POST'])
def upload():
    # get file
    uploaded_file = request.files['file']

    # check if file is an image
    if uploaded_file.content_type != "image/jpeg":
        return redirect("/")

    # create path of image
    upload_image_path = os.path.join("uploads", uploaded_file.filename)

    # save image
    uploaded_file.save(upload_image_path)
    # classify image
    probability = classify(upload_image_path)
    return render_template('home.html', probability=probability, filename=uploaded_file.filename)


def classify(upload_image_path):

    # img = tf.io.read_file(upload_image_path)
    # img = tf.image.decode_jpeg(image, channels=3)
    img = image.load_img(
        upload_image_path, target_size=(IMAGE_SIZE, IMAGE_SIZE))
    img_array = image.img_to_array(img)
    expanded_image_array = np.expand_dims(img_array, axis=0)
    preprocessed_image = preprocess_input(
        expanded_image_array)  # Preprocess the image
    # image = tf.image.resize(image, [IMAGE_SIZE, IMAGE_SIZE])
    # image /= 255.0  # normalize to [0,1] range
    # image = tf.reshape(image, (1, IMAGE_SIZE, IMAGE_SIZE, 3))
    probability = model.predict(preprocessed_image)

    if probability[0][0] > probability[0][1] and probability[0][0] > probability[0][2]:
        return {"apple": round((probability[0][0] * 100), 2)}
    elif probability[0][1] > probability[0][0] and probability[0][1] > probability[0][2]:
        return {"banana": round((probability[0][1] * 100), 2)}
    else:
        return {"cherry": round((probability[0][2] * 100), 2)}


@uploader.route('/uploader/<filename>')
def send_file(filename):
    return send_from_directory("uploads", filename)
