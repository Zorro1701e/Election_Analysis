from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# database set up
engine = create_engine("sqlite:///hawaii.sqlite")

# reflecting database
Base = automap_base()

# reflecting the tables
Base.prepare(engine, reflect=True)

#save feference to table to call in LATER. (measurement and station)
measurement = Base.classes.measurement
station = Base.classes.station

# Create session link
session = Session(engine)

app = Flask(__name__)

@app.route('/')

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

if __name__ =="__main__":
    app.run(debug=True)