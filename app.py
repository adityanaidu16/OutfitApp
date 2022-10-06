from flask import Flask, render_template, request, redirect, flash, url_for, session
from flask_session import Session
import requests
import time
import os
import sqlite3
import cv2
import numpy as np

import tensorflow as tf

from bs4 import BeautifulSoup
import requests

UPLOAD_FOLDER = '/fitfixer/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Configure flask application
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
sess = Session()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

connection = sqlite3.connect("fitfixer.db", check_same_thread=False)

cursor = connection.execute("SELECT name, color, category from CLOSET")

for row in cursor:
   print("NAME = ", row[0])
   print("COLOR = ", row[1])
   print("CATEGORY = ", row[2], "\n")

def weather(city):
    try:
        soup = BeautifulSoup(requests.get("https://www.google.com/search?q=weather+{}".format(city)).content, "html.parser")
        weather = soup.find('div', class_="BNeawe iBp4i AP7Wnd")
        return weather.getText()[0:-2]
    except:
        return "Error"
    

# render index.html by default 
@app.route('/')
def index():
    return render_template('index.html')

# function for adding closet
@app.route("/", methods=["GET", "POST"])
def outfits():
    # User reach route via filter section POST (as by submitting a form via POST)
    if request.method == "POST":
        name = request.form.get("name_response")
        category = request.form.get("category_response")

        print(name, category)

        uploaded_file = request.files['file']
        print(uploaded_file.filename)
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)

        try:
            img = cv2.imread(uploaded_file.filename)
            img = np.asarray(bytearray(img))
            print(img)
            im = cv2.resize(img, (64, 64))
            im = im/255
            print(im)
        except:
            print("error")


        # connection.execute("INSERT INTO CLOSET(name, color, category) \
                    # VALUES (?, ?, ?)", (name, name, category))
        # connection.commit()



        return render_template('index.html') 
    else:
        return render_template('index.html')

# function for suggesting outfits
@app.route("/generate", methods=["GET", "POST"])
def suggest():
    # User reach route via filter section POST (as by submitting a form via POST)
    if request.method == "POST":
        location = request.form.get("location_response")
        duration = request.form.get("duration_response")
        print(weather(location))
        print(duration)

        return render_template('generate.html') 
    else:
        return render_template('generate.html')