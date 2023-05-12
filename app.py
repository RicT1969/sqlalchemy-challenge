# Python SQL toolkit and Object Relational Mapper
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# Create connection to Hawaii.sqlite file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)


# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

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
        f'<h2>Hi, welcome to the homepage for the SQLAlchemy Challenge API where you can access climate records for Hawaii.</h2>'
        f'<p><ul><h3>Available Routes for Hawaian Climate Data:</h3><ol></br>'
        f'<li>Daily Rainfall (mm) record set:  /api/v1.0/precipitation</li>'
        f'<li>Weather Stations:  /api/v1.0/stations</li>'
        f'<li>Daily Temperatures for the Year Between 23/08/16 and 23/08/2017 (Station USC00519281):  /api/v1.0/temperatures</li>'
        f'<li>Summary temperatures from a specified start date (yyyy-mm-dd): /api/v1.0/start<start><br/></li>'
        f'<li>Summary temperatures - from a specified start date (yyyy-mm-dd) / end date (yyyy-mm-dd): /api/v1.0/start_end/<start>/<end><br/></li></ol></ul></br>'
        f'<p><b>Note:</b> When you enter the start date only, you will receive all results from that date until the last record</p>'
        f'<p><b>Note:</b> Our record set is from 2010-01-01 until 2017-08-23</p>'
        )
    
#################################################
# Return rainfall data
#################################################

@app.route("/api/v1.0/precipitation")
def precipitation():

    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    #Return a list of rainfall observations
    results = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date >= '2016-08-23').all()
       
    session.close()

    #create dictionary
    all_rainfall = []
    for date, prcp in results:
        rainfall_dict = {}
        rainfall_dict["date"] = date
        rainfall_dict["prcp"] = prcp
        all_rainfall.append(rainfall_dict)
    
    return jsonify(all_rainfall)

#################################################
# Return a JSON list of stations from the dataset.
#################################################

@app.route("/api/v1.0/stations")
def stations():

    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    #Return a list of all stations
    results = session.query(station.station).all()
       
    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))
    
        
    return jsonify(all_stations)



###########################################################################
# Dates and Temperature observations for most-active station for 
# previous year of data and return JSON list of temperatures for previous year.
# USING RESULTS FROM climate.ipynb FOR MOST-ACTIVE STATION AND PREVIOUS YEAR.
###########################################################################


@app.route("/api/v1.0/temperatures")
def temperatures():

    # Create our session (link) from Python to the DB
    session = Session(engine)
    
     
    sel = [measurement.date, measurement.tobs, measurement.station]
    active_station = session.query(*sel).\
    filter(func.strftime(measurement.date) >= '2016-08-23').\
        filter(measurement.station == 'USC00519281').all()
            
    #active_station
               
    session.close()

    #create dictionary
    all_temps = []
    for date, tobs, station in active_station:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["tobs"] = tobs
        temp_dict["station"] = station
        all_temps.append(temp_dict)
    
    return jsonify(all_temps)



##########################################################################
# Return minimum, average and maximum temperature for a specified start date.
###########################################################################

@app.route("/api/v1.0/start/<start>")
def summary_by_start(start=None):



    # Create our session (link) from Python to the DB
    session = Session(engine)
    
     #Fetch the temperatures from the start# date that matches
     #the path variable supplied by the user, or a 404 if not."""

    sel = [func.min(measurement.tobs),
          func.avg(measurement.tobs),
          func.max(measurement.tobs)]
    start_tobs = session.query(*sel).filter(measurement.date >= start).all()
       
    first_date = session.query(func.min(measurement.date)).scalar()
    # print(first_date)
             
    session.close()
    # if not start_tobs:
    #     return jsonify({"error": "Date not found."}), 404

    #start_tobs = list(np.ravel(start_tobs))
    
    #print(start_tobs)
    #create dictionary
    s_temps = []
    for min, avg, max in start_tobs:
        s_temp_dict = {}
        s_temp_dict["Tmin"] = min
        s_temp_dict["Taverage"] = avg
        s_temp_dict["Tmax"] = max
        s_temps.append(s_temp_dict)
    
    #Find first date for error message
    first_date = session.query(func.min(measurement.date)).scalar()
    #print(first_date)
    
    # If the query returned non-null values return the results, otherwise return an error message. \
    # return an error message if the date is before the first record date
    
    if first_date > start:
        return jsonify({"error": f"Date {start} is too early, our records begin {first_date}."}), 404      
    
    elif s_temp_dict["min"]: 
        return jsonify(s_temps)
    
    else:
        return jsonify({"error": f"Date {start} does not exist or is not formatted yyyy-mm-dd."}), 404
    
########################################################################################################
# Return minimum, average and maximum temperature for a period between a specified start date and end date
########################################################################################################

@app.route("/api/v1.0/start_end/<start>/<end>")
def summary_by_range(start=None,end=None):

    # Create our session (link) from Python to the DB
    session = Session(engine)
    
#Fetch the temperatures from the start and end dates that match
#the path variable supplied by the user, or a 404 if not.

    sel = [func.min(measurement.tobs),
          func.avg(measurement.tobs),
          func.max(measurement.tobs)]
    start_end_tobs = session.query(*sel).filter(measurement.date >= start).filter(measurement.date <= end).all()
       
                
    session.close()
   
    #Find first date for error message
    first_date = session.query(func.min(measurement.date)).scalar()
    last_date = session.query(func.max(measurement.date)).scalar()

    #create dictionary
    se_temps = []
    for min, avg, max in start_end_tobs:
        se_temp_dict = {}
        se_temp_dict["min"] = min
        se_temp_dict["average"] = avg
        se_temp_dict["max"] = max
        se_temps.append(se_temp_dict)
    
    # If the query returned non-null values return the results,
    # otherwise return an error message
    if first_date > start:
        return jsonify({"error": f"Date {start} is too early, our records begin {first_date}."}), 404      
    
    elif last_date < end:
        return jsonify({"error": f"Date {end} is too recent, our records end {last_date}."}), 404  

    elif se_temp_dict["min"]: 
        return jsonify(se_temps)
    
    else:
        return jsonify({"error": f"Date(s) are not formatted yyyy-mm-dd."}), 404
    


if __name__ == '__main__':
    app.run(debug=True)
