# Third party
import pandas as pd
from flask import Flask, render_template, jsonify

# Custom
from scripts.utility import (calc_temps_dict
                            , prcp_last_12_months_df, station_df
                            , tobs_df_sorted
                            , last_date)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/v1.0/precipitation")
def precipitation_endpoint():
    return jsonify(prcp_last_12_months_df.to_dict())


@app.route("/api/v1.0/stations")
def stations_endpoint():
    return jsonify(station_df.to_dict())


@app.route("/api/v1.0/tobs")
def tobs_endpoint():
    return jsonify(tobs_df_sorted.to_dict())


@app.route("/api/v1.0/<start>", defaults={'end': last_date}, methods=['GET'])
@app.route("/api/v1.0/<start>/<end>", methods=['GET'])
def date_range_endpoint(start, end):
    start = str(start)
    end = str(end)
    return jsonify(calc_temps_dict(start, end))


if __name__ == '__main__':
    app.run()