from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify
import pandas as pd
import requests

APP = Flask(__name__)
FLASK_DEBUG=1
# server name is specified in proc file
APP.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///MedCabinet.db"
#DB.init_app(app)

def predict(input_song):
    return input_song

@APP.route('/', methods=['GET', 'POST'])
def root():
    song_id = ''
    if request.method == "POST":
        song_id = request.form['song_id']
        output = predict(song_id)
    return render_template('base.html', song_id=output)

@APP.route('/song', methods=['GET', 'POST'])
def song():
    return render_template('index.html')

if __name__ == "__main__":
    APP.run()
