
from flask import Flask, render_template, request, url_for
from flask_googlemaps import GoogleMaps, Map
import pandas as pd


app = Flask(__name__)
GoogleMaps(app, key="AIzaSyDhLViwByDYVOICDO_CJb--YexgYHjNLrw")
app.config['GOOGLEMAPS_KEY'] = "AIzaSyDhLViwByDYVOICDO_CJb--YexgYHjNLrw"

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/user')
def user():

    return render_template('user.html')

@app.route('/userrecorded')
def userrecorded():
    return render_template('userrecorded.html')

@app.route('/rescueops')
def rescueops():

    return render_template('rescueops.html')

@app.route('/rescueopsrecorded')
def rescueopsrecorded():
    return render_template('rescueopsrecorded.html')