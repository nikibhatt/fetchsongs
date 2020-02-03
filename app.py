from flask_sqlalchemy import SQLAlchemy
from .models import *
from flask import Flask, render_template, request, jsonify
import pandas as pd

APP = Flask(__name__)
# server name is specified in proc file
APP.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///MedCabinet.db"
DB.init_app(app)

def predict(input_song):
    return input_song.to_json(orient='columns')

@APP.route('/', methods=['GET', 'POST'])
def root():
    return "Spotify song selector API"

@APP.route('/song', method=['POST'])
def song():
    song_selected = request.get_json(force=True)
    song_id = song_selected['input']
    assert isinstance(song_id, str)
    output = predict(song_id)
    return output

if __name == "__main":
    APP.run()
