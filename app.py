from flask_sqlalchemy import SQLAlchemy
from .models import *
from flask import Flask, render_template, request, jsonify
import pandas as pd

def predict(input_song):
    output input_song.to_json(orient='columns')

def create_app():
    app = Flask(__name__)
    # server name is specified in proc file
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///MedCabinet.db"
    DB.init_app(app)

    #Base landing page
    @app.route('/', methods=['GET', 'POST'])
    def root():
        return "Spotify song selector API"

    #Reset will drop all tables, including those not in models
    @app.route('/song', method=['POST'])
    def song():
        song_selected = request.get_json(force=True)
        song_id = song_selected['input']
        assert isinstance(song_id, str)
        output = predict(song_id)
        return output

    return app
