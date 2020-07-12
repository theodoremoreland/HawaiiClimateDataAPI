from scripts.utility import calc_temps, calc_temps2, prcp_df, station_df, tobs_df2, last_date
import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/v1.0/precipitation")
def prcp():
    return jsonify(prcp_df.to_dict())

@app.route("/api/v1.0/stations")
def stations():
    return jsonify(station_df.to_dict())

@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(tobs_df2.to_dict())

@app.route("/api/v1.0/<start>")
def start_(start):
    start = str(start)
    return jsonify(calc_temps2(start, last_date))

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    start = str(start)
    end = str(end)
    return jsonify(calc_temps2(start, end))


if __name__ == '__main__':
    app.run()