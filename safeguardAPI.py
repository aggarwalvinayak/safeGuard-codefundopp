
from flask import Flask, render_template, request, url_for
from flask_googlemaps import GoogleMaps, Map
import pandas as pd
from Utils import cluster

def fn():
    global MasterMap
    MasterMap = Map(
        identifier="view-side",
        lat=latCenter,
        lng=longCenter,
        markers=cluster(df),
        style="height:480px;width:850px;margin:0;",
        fit_markers_to_bounds = True
    )
    return MasterMap
global df, Notif
df = pd.read_csv("./database/final.csv")
df.columns=['ID','Latitude','Longitude','isSOS','isCamp','isUnsafe']
latCenter = df.Latitude.mean()
longCenter = df.Longitude.mean()
print(df)
Notif = "Currently None"


app = Flask(__name__)
GoogleMaps(app, key="AIzaSyDhLViwByDYVOICDO_CJb--YexgYHjNLrw")
global MasterMap
MasterMap = Map(
    identifier="view-side",
    lat=latCenter,
    lng=longCenter,
    markers=cluster(df),
    style="height:480px;width:850px;margin:0;"
)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/user', methods=['POST', 'GET'])
def user():
    global df, Notif
    print(df)
    return render_template('user.html', map=MasterMap, Notification=Notif)

@app.route('/userrecorded', methods=['POST', 'GET'])
def userrecorded():
    global df, Notif
    if request.method == 'POST':
        if request.form.get('SOS'):
            SOSlat = float(request.form['SOSlat'])
            SOSlng = float(request.form['SOSlng'])
            df = df.append(pd.DataFrame([[1, SOSlat, SOSlng, 1, 0, 0]], columns=df.columns), ignore_index=True)

            fn()
        elif request.form.get('Unsafe'):
            Unsafelat = float(request.form['Unsafelat'])
            Unsafelng = float(request.form['Unsafelng'])
            df = df.append(pd.DataFrame([[1, Unsafelat, Unsafelng, 0, 0, 0]], columns=df.columns), ignore_index=True)

            fn()
        elif request.form.get('Mark'):
            Marklat = float(request.form['Marklat'])
            Marklng = float(request.form['Marklng'])
            df = df.append(pd.DataFrame([[1, Marklat, Marklng, 0, 0, 1]], columns=df.columns), ignore_index=True)

            fn()

    return render_template('userrecorded.html')

@app.route('/rescueops')
def rescueops():
    return render_template('rescueops.html', map=MasterMap)

@app.route('/rescueopsrecorded', methods=['POST', 'GET'])
def rescueopsrecorded():
    global df, Notif
    if request.method == 'POST':
        if request.form.get('Camp'):
            Camplat = float(request.form['Camplat'])
            Camplng = float(request.form['Camplng'])
            df = df.append(pd.DataFrame([[1, Camplat, Camplng, 0, 1, 0]], columns=df.columns), ignore_index=True)

            fn()
        elif request.form.get('Notif'):
            Notif = request.form['Notif']

        elif request.form.get('Mark'):
            Marklat = float(request.form['Marklat'])
            Marklng = float(request.form['Marklng'])
            df = df.append(pd.DataFrame([[1, Marklat, Marklng, 0, 0, 1]], columns=df.columns), ignore_index=True)

            fn()

    return render_template('rescueopsrecorded.html')