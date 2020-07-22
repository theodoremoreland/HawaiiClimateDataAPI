#!/usr/bin/env python
# coding: utf-8

# Native library
import json
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

# Third party
import numpy as np
import pandas as pd

# sqlite path is relative to app.py caller.
engine = create_engine("sqlite:///resources/hawaii.sqlite", connect_args={'check_same_thread': False})
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

# References to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
one_year_ago = str(int(last_date[0:4]) - 1) + last_date[4:8] + str(int(last_date[8:10]) + 1)

prcp_last_12_months = session.query(Measurement.date, Measurement.prcp)\
    .order_by(Measurement.date.desc())\
        .filter(func.strftime("%Y-%m-%d", Measurement.date) >= one_year_ago)\
            .all()
prcp_last_12_months_df = pd.DataFrame(prcp_last_12_months).set_index("date")
prcp_last_12_months_df.fillna(value=0, inplace=True)
prcp_last_12_months_df = prcp_last_12_months_df.sort_values("date", ascending=True).iloc[0:]
prcp_last_12_months_df.reset_index(inplace=True)


station_count = session.query(func.count(Station.station)).all()
station_activity = session.query(Measurement.station, func.count(Measurement.station))\
    .group_by(Measurement.station)\
        .order_by(func.count(Measurement.station).desc())\
            .all()
station_df = pd.DataFrame([station_activity])


top_station_stats = session.query(func.min(Measurement.tobs)
    , func.max(Measurement.tobs)
    , func.avg(Measurement.tobs))\
        .filter(Measurement.station == station_activity[0][0])\
            .all()
top_year = session.query(Measurement.station
    , Measurement.date
    , Measurement.tobs
    , Measurement.prcp)\
        .order_by(Measurement.date.asc())\
            .filter(func.strftime("%Y-%m-%d", Measurement.date) >= one_year_ago)\
                .filter(Measurement.station == station_activity[0][0])\
                    .all()
top_year_df = pd.DataFrame(top_year)
top_tobs_df = top_year_df[["tobs"]]
tobs_last_12_months = session.query(Measurement.date, Measurement.tobs)\
    .order_by(Measurement.date.desc())\
        .filter(func.strftime("%Y-%m-%d", Measurement.date) >= one_year_ago)\
            .all()
tobs_df = pd.DataFrame(tobs_last_12_months)
tobs_df_clean = tobs_df.copy().fillna(value=0)
tobs_df_sorted = tobs_df_clean.sort_values("date", ascending=True).iloc[0:]


def calc_prcp(start_date, end_date):
    """Calculates the total amount of rainfall per weather station for between dates specified.
    Sorts in descending order by precipitation amount and lists the station, name, latitude, longitude, and elevation
    """
    station_prcp = session.query(Measurement.station, func.sum(Measurement.prcp))\
        .group_by(Measurement.station).order_by(func.sum(Measurement.prcp).desc())\
            .filter(Measurement.date >= start_date)\
                .filter(Measurement.date <= end_date)\
                    .all()
    
    for i in station_prcp:
        station = i[0]
        value = session.query(Station.station
            , Station.name
            , Station.latitude
            , Station.longitude
            , Station.elevation
            , func.sum(Measurement.prcp))\
                .filter(Measurement.date >= start_date)\
                    .filter(Measurement.date <= end_date)\
                        .filter(Measurement.station == station)\
                            .filter(Station.station == station)\
                                .all()
        print(value)


def calc_temps(start_date, end_date):
    """Returns the minimum, average, and maximum temperatures for that range of dates
    This function will accept start date and end date in the format '%Y-%m-%d' 
    """
    value = session.query(func.min(Measurement.tobs)
        , func.avg(Measurement.tobs)
        , func.max(Measurement.tobs))\
            .filter(Measurement.date >= start_date)\
                .filter(Measurement.date <= end_date)\
                    .all()
    return value


def calc_temps_dict(start_date, end_date):
    """The same as "calc_temps", but returns value(s) in Dictionary format.
    """
    x = session.query(func.min(Measurement.tobs)
        , func.avg(Measurement.tobs)
        , func.max(Measurement.tobs))\
            .filter(Measurement.date >= start_date)\
                .filter(Measurement.date <= end_date)\
                    .all()
    y = pd.DataFrame([x])
    z = y.to_dict()
    return z