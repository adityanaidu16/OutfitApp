from flask import Flask, render_template, request
import requests
import time
import os
import sqlite3

from bs4 import BeautifulSoup
import requests

# Configure flask application
app = Flask(__name__)

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
        color = request.form.get("color_response")
        category = request.form.get("category_response")
        connection.execute("INSERT INTO CLOSET(name, color, category) \
                    VALUES (?, ?, ?)", (name, color, category))
        connection.commit()

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