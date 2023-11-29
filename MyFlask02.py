from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from collections import OrderedDict
import pandas as pd
import mysql.connector
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Wriothesley@localhost/flight_game?charset=utf8mb4&collation=utf8mb4_general_ci'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Airport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ident = db.Column(db.String(4), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    latitude_deg = db.Column(db.Float, nullable=False)
    longitude_deg = db.Column(db.Float, nullable=False)
    elevation_ft = db.Column(db.Integer)
    municipality = db.Column(db.String(50))
    scheduled_service = db.Column(db.String(10))
    iata_code = db.Column(db.String(3))
    local_code = db.Column(db.String(10))

def add_database():
    df = pd.read_csv('airports.csv')
    df.to_sql('airport', con=db.engine, if_exists='replace', index=False)

@app.route('/airport/<ident>', methods=['GET'])
def get_airport_info(ident):
    airport = Airport.query.filter_by(ident=ident).first()
    if airport:
        airport_info = OrderedDict([
            ("ICAO", airport.ident),
            ("Name", airport.name),
            ("Location", airport.municipality if airport.municipality else "Unknown")
        ])
        return json.dumps(airport_info)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(use_reloader=True, host='127.0.0.1', port=5000)