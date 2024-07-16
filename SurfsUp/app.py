import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import os

#################################################
# Database Setup
#################################################
current_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(current_dir, 'Resources', 'hawaii.sqlite')

engine = create_engine(f"sqlite:///{database_path}")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"  
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"

        
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations"""
    # Query all measurements
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    # Convert the query results to a dictionary using date as the key and prcp as the value
    all_precipitation = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        all_precipitation.append(precipitation_dict)

    return jsonify(all_precipitation)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations"""
    # Query all stations
    results = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
   # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of temperature observations (tobs) for the previous year for the most active station"""
    # Get the most active station
    
    active_stations = session.query(Measurement.station, func.count(Measurement.station).label('count')).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.station).desc()).all()

    most_active_station = active_stations[0][0]
    print(f"Most Active Station: {most_active_station}")
    

    # Get the most recent date in the dataset
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    print(f"Latest Date: {most_recent_date}")

    # Calculate the date one year ago from the most recent date
    one_year_ago = func.date(most_recent_date, '-1 year')

    # Query for the dates and temperature observations from the most active station for the last year
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station).filter(Measurement.date >= one_year_ago).all()

    session.close()

    # Convert list of tuples into normal list
    tobs_data = list(np.ravel(results))

    return jsonify(tobs_data)

@app.route("/api/v1.0/<start>")
def start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range."""
    # Query for the minimum, average, and maximum temperature from the start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()

    session.close()

    # Convert the query results to a list
    temps = list(np.ravel(results))

    return jsonify(temps)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start-end range."""
    # Query for the minimum, average, and maximum temperature between the start and end dates
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    session.close()

    # Convert the query results to a list
    temps = list(np.ravel(results))

    return jsonify(temps)

if __name__ == '__main__':
    app.run(debug=True) 

