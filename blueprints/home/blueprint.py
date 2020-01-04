from flask import Blueprint, render_template, request
import psycopg2

import tensorflow as tf
import os
import random


home = Blueprint('home', __name__)

IMAGE_WIDTH, IMAGE_HEIGHT = 192, 192


def load_resize_save_image(path, filename):
    image = tf.io.read_file(path + "/" + filename)
    try:
        image = tf.image.decode_jpeg(image, channels=3)
        image = tf.image.resize(image, [IMAGE_WIDTH, IMAGE_HEIGHT])
        tf.keras.preprocessing.image.save_img(
            path + "/" + filename, image, data_format='channels_last')
    except:
        os.remove(path + "/" + filename)


@home.route('/',  methods=['POST', 'GET'])
def route_name():
    if request.method == 'GET':
        return render_template('home.html', feedback=False)
    else:
        name_of_image, category = request.form['text'].split(", ")
        print(name_of_image, category)

        src = "./uploads/" + name_of_image
        dst = "./new_classified_fruits/" + category + "/" + name_of_image
        # rename() function will rename all the files
        load_resize_save_image("./uploads", name_of_image)
        os.rename(src, dst)
        return render_template('home.html', feedback=True)
