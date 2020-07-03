#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import datetime as dt
import json

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False})

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

inspector = inspect(engine)

columns_tbl1 = inspector.get_columns('measurement') #id(int), station(txt), date(txt), prcp(flt), tobs(flt)
columns_tbl2 = inspector.get_columns('station') #id(int), station(txt), name(txt), latitude(flt), longitude(flt), elevation(flt)

# Calculate the date 1 year ago from the last data point in the database
last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
one_year_ago = str(int(last_date[0:4]) - 1) + last_date[4:8] + str(int(last_date[8:10]) + 1)

prcp_last_12_months = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date.desc())    .filter(func.strftime("%Y-%m-%d", Measurement.date) >= one_year_ago).all()

df = pd.DataFrame(prcp_last_12_months).set_index("date")

df2 = df.copy().fillna(value=0)
df3 = df2.sort_values("date", ascending=True).iloc[0:]
high = df3.groupby(["date"]).max()

station_count = session.query(func.count(Station.station)).all()

station_activity = session.query(Measurement.station, func.count(Measurement.station))    .group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()

top_station_stats = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs))    .filter(Measurement.station == station_activity[0][0]).all()


# Choose the station with the highest number of temperature observations.
# Query the last 12 months of temperature observation data for this station and plot the results as a histogram
top_year = session.query(Measurement.station, Measurement.date, Measurement.tobs, Measurement.prcp)    .order_by(Measurement.date.asc())    .filter(func.strftime("%Y-%m-%d", Measurement.date) >= one_year_ago)    .filter(Measurement.station == station_activity[0][0]).all()

top_year_df = pd.DataFrame(top_year)#.set_index("date")
top_tobs_df = top_year_df[["tobs"]]



# This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for that range of dates
def calc_temps(start_date, end_date):    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()




# Calculate the total amount of rainfall per weather station for your trip dates using the previous year's matching dates.
# Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation
def calc_prcp(start_date, end_date):

    station_prcp = session.query(Measurement.station, func.sum(Measurement.prcp))                       .group_by(Measurement.station).order_by(func.sum(Measurement.prcp).desc())                       .filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    
    list1 = []
    for i in station_prcp:
        station = i[0]
        print(session.query(Station.station, Station.name, Station.latitude,                         Station.longitude, Station.elevation, func.sum(Measurement.prcp)).                         filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).                         filter(Measurement.station == station).                         filter(Station.station == station).all())
        

tobs_last_12_months = session.query(Measurement.date, Measurement.tobs).order_by(Measurement.date.desc())    .filter(func.strftime("%Y-%m-%d", Measurement.date) >= one_year_ago).all()

# Save the query results as a Pandas DataFrame and set the index to the date column
tobs_df = pd.DataFrame(tobs_last_12_months)

# Sort the dataframe by date
tobs_df_clean = tobs_df.copy().fillna(value=0)
tobs_df_sort = tobs_df_clean.sort_values("date", ascending=True).iloc[0:]


station_df = pd.DataFrame([station_activity])
prcp_df = df3.reset_index()
tobs_df2 = tobs_df_sort

def calc_temps2(start_date, end_date):
    # the same as "calc_temps", but returns value(s) in Dictionary format.
    x = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    y = pd.DataFrame([x])
    z = y.to_dict()
    return z

from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()